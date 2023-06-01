# -*- coding: utf-8 -*-
"""
This file is to hold request-related code, meaning code that help make api requests, such as
url-forming functions.

The main difference between the code here and in utils/rest.py is that that code is based on some
open source code, and we might contribute our changes back to that repo. This is our own stuff that
we'll keep for this repo.
"""
import logging
import os
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
import urllib3

from utils.base import ImplementationError, MilMoveEnv, is_local
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.types import RequestKwargsType


logger = logging.getLogger(__name__)


class RequestHost(Enum):
    """
    Holds host subdomains
    """

    MY = "my"
    OFFICE = "office"
    PRIME = "api"

    def local_subdomain(self):
        if self == RequestHost.MY:
            return "milmovelocal"
        elif self == RequestHost.OFFICE:
            return "officelocal"
        elif self == RequestHost.PRIME:
            return "primelocal"
        else:
            raise Exception(f"Unknown request host: {self}")


@dataclass
class MilMoveRequestPreparer:
    """
    Class to help prepare for making requests to MilMove APIs based on the target environment.
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    milmove_env: MilMoveEnv

    GHC_PATH_PREFIX = "/ghc/v1"
    INTERNAL_PATH_PREFIX = "/internal"
    PRIME_PATH_PREFIX = "/prime/v1"
    SUPPORT_PATH_PREFIX = "/support/v1"

    def get_cert_kwargs(self) -> RequestKwargsType:
        """
        Grabs request kwargs that will be needed for the endpoint.

        :param certs_required: Boolean indicating if certs will be required. These will point to the
            paths for the TLS cert/key files, which change based on the environment being targetted.
            Possibly also includes a value that is either a boolean that indicates if the TLS certs
            should be verified, or a path to certs to use for verification.
        :param endpoint_name: name of endpoint, for locust request grouping
        :return: kwargs that can be passed to the request.
        """
        kwargs: RequestKwargsType = {}

        if is_local(env=self.milmove_env):
            kwargs.update(deepcopy(LOCAL_TLS_CERT_KWARGS))
        else:
            kwargs["cert"] = DP3_CERT_KEY_PEM

        if "verify" in kwargs and not kwargs["verify"]:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        return kwargs

    def base_url(self, request_host: RequestHost) -> str:
        if base_domain := os.getenv("BASE_DOMAIN"):
            return base_domain

        default_local_protocol = "http"
        default_local_port = "8080"
        if request_host == RequestHost.PRIME:
            default_local_protocol = "https"
            default_local_port = "9443"

        if is_local(env=self.milmove_env):
            return self._form_base_url(
                local_port=os.getenv("LOCAL_PORT", default_local_port),
                local_protocol=default_local_protocol,
                local_subdomain=request_host.local_subdomain(),
            )
        else:
            return self._form_base_url(deployed_subdomain=request_host.value)

    def _form_base_url(
        self,
        deployed_subdomain: str = "",
        local_port: str = "",
        local_protocol: str = "",
        local_subdomain: str = "",
    ) -> str:
        """
        Sets up the base domain for a request based on the environment we're running against and
        the subdomain we're targeting.

        Con optionally be overridden by setting an environment variable called BASE_DOMAIN that
        points to where you want it to point.

        :param deployed_subdomain: subdomain to target when deployed, e.g. "api" or "my".
        :param local_port: Port to use when running locally.
        :param local_protocol: local protocol to run against, e.g. "https"
        :param local_subdomain: subdomain to target when running locally, e.g. "primelocal"
        :return: base domain to use for requests, e.g. https://api.loadtest.dp3.us
        """
        if base_domain := os.getenv("BASE_DOMAIN"):
            return base_domain

        if not is_local(env=self.milmove_env):
            # NOTE: deployed protocol is always https
            return f"https://{deployed_subdomain}.loadtest.dp3.us"

        port = str(local_port)  # just in case an int was passed in

        if not (port.isdigit() and len(port) == 4):
            raise ImplementationError("The local port must be a string of 4 digits.")

        return f"{local_protocol}://{local_subdomain}:{port}"

    def form_api_path(self, request_host: RequestHost, api_path_prefix: str, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the API.

        :param request_host: host to target, e.g. "my"
        :param api_path_prefix: prefix for the api, e.g. "/ghc/v1"
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """

        api_url = self.base_url(request_host)

        if api_path_prefix:
            api_url += api_path_prefix

        return f"{api_url}{endpoint}"

    def form_ghc_path(self, request_host: RequestHost, endpoint: str, include_prefix: bool = True) -> str:
        """
        Returns a url pointing at the requested endpoint for the GHC API.

        :param request_host: host to target, e.g. "my"
        :param endpoint: Endpoint to target, e.g. "/moves"
        :param include_prefix: Indicate if the GHC prefix should be included or not
        :return: full url to use in requests
        """

        path_prefix = self.GHC_PATH_PREFIX
        if not include_prefix:
            path_prefix = ""

        return self.form_api_path(request_host, path_prefix, endpoint)

    def form_internal_path(self, request_host: RequestHost, endpoint: str, include_prefix: bool = True) -> str:
        """
        Returns a url pointing at the requested endpoint for the Internal API.

        :param request_host: host to target, e.g. "my"
        :param endpoint: Endpoint to target, e.g. "/moves"
        :param include_prefix: Indicate if the internal prefix should be included or not
        :return: full url to use in requests
        """

        path_prefix = self.INTERNAL_PATH_PREFIX
        if not include_prefix:
            path_prefix = ""

        return self.form_api_path(request_host, path_prefix, endpoint)

    def form_prime_path(self, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the Prime API.

        :param request_host: host to target, e.g. "my"
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """

        path_prefix = self.PRIME_PATH_PREFIX

        return self.form_api_path(RequestHost.PRIME, path_prefix, endpoint)
