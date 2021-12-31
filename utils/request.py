# -*- coding: utf-8 -*-
"""
This file is to hold request-related code, meaning code that help make api requests, such as
url-forming functions.
"""
import os
from copy import deepcopy
from dataclasses import dataclass
from typing import Union

from locust import User

from utils.base import ImplementationError, MilMoveEnv, is_local
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.rest import get_json_headers
from utils.types import RequestKwargsType


@dataclass
class MilMoveRequestPreparer:
    """
    Class to help prepare for making requests to MilMove APIs based on the target environment.
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv

    def get_request_kwargs(self, certs_required: bool = False) -> RequestKwargsType:
        """
        Grabs request kwargs that will be needed for the endpoint.

        :param certs_required: Boolean indicating if certs will be required. These will point to the
            paths for the TLS cert/key files, which change based on the environment being targetted.
            Possibly also includes a value that is either a boolean that indicates if the TLS certs
            should be verified, or a path to certs to use for verification.
        :return: kwargs that can be passed to the request.
        """
        kwargs = {"headers": get_json_headers()}

        if certs_required:
            if is_local(env=self.env):
                kwargs.update(deepcopy(LOCAL_TLS_CERT_KWARGS))
            else:
                kwargs["cert"] = DP3_CERT_KEY_PEM

        return kwargs

    def form_base_domain(
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

        if not is_local(env=self.env):
            # NOTE: deployed protocol is always https
            return f"https://{deployed_subdomain}.loadtest.dp3.us"

        port = str(local_port)  # just in case an int was passed in

        if not (port.isdigit() and len(port) == 4):
            raise ImplementationError("The local port must be a string of 4 digits.")

        return f"{local_protocol}://{local_subdomain}:{port}"

    def form_ghc_path(self, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the GHC API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port="8080",
                local_protocol="http",
                local_subdomain="officelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="office")

        return f"{base_domain}/ghc/v1{endpoint}"

    def prep_ghc_request(self, endpoint: str) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the GHC API.
        :param endpoint: endpoint to target, e.g. "/moves"
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_ghc_path(endpoint=endpoint)

        kwargs = self.get_request_kwargs()

        return url, kwargs

    def form_internal_path(self, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the Internal API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port="8080",
                local_protocol="http",
                local_subdomain="milmovelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="my")

        return f"{base_domain}/internal{endpoint}"

    def prep_internal_request(self, endpoint: str) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Internal API.
        :param endpoint: endpoint to target, e.g. "/moves"
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_internal_path(endpoint=endpoint)

        kwargs = self.get_request_kwargs()

        return url, kwargs

    def form_prime_path(self, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the Prime API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port="9443",
                local_protocol="https",
                local_subdomain="primelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="api")

        return f"{base_domain}/prime/v1{endpoint}"

    def prep_prime_request(self, endpoint: str) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Prime API.
        :param endpoint: endpoint to target, e.g. "/moves"
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_prime_path(endpoint=endpoint)

        kwargs = self.get_request_kwargs(certs_required=True)

        return url, kwargs

    def form_support_path(self, endpoint: str) -> str:
        """
        Returns a url pointing at the requested endpoint for the Support API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port="9443",
                local_protocol="https",
                local_subdomain="primelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="api")

        return f"{base_domain}/support/v1{endpoint}"

    def prep_support_request(self, endpoint: str) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Support API.
        :param endpoint: endpoint to target, e.g. "/moves"
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_support_path(endpoint=endpoint)

        kwargs = self.get_request_kwargs(certs_required=True)

        return url, kwargs


class MilMoveRequestMixin:
    """
    Mixin for a Locust User class/subclass that provides helper functions to form urls based on the
    host (as passed in the --host flag) and .
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv

    request_preparer: MilMoveRequestPreparer

    def __init__(self: Union[User, "MilMoveRequestMixin"], *args, **kwargs) -> None:
        """
        Sets up the env based on value from the --host flag. Note that the `self.host` value is set
        on the class from the command line flag BEFORE initialization.
        """
        self.set_milmove_env()
        self.set_up_request_preparer()

        super().__init__(*args, **kwargs)

    def set_milmove_env(self: Union[User, "MilMoveRequestMixin"]) -> None:
        """
        Sets the env attribute for the class. Takes in a string and sets the MilMoveEnv in self.env.
        """
        self.env = MilMoveEnv(value=self.host)

    def set_up_request_preparer(self: Union[User, "MilMoveRequestMixin"]) -> None:
        """
        Sets up a URL creator that can be used later to form proper endpoint URLs
        """
        self.request_preparer = MilMoveRequestPreparer(env=self.env)
