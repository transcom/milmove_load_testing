# -*- coding: utf-8 -*-
"""
This file is to hold request-related code, meaning code that help make api requests, such as
url-forming functions.

The main difference between the code here and in utils/rest.py is that that code is based on some
open source code, and we might contribute our changes back to that repo. This is our own stuff that
we'll keep for this repo.
"""
import inspect
import json
import logging
import os
from copy import deepcopy
from dataclasses import dataclass
from typing import Union

from locust import TaskSet
from requests import PreparedRequest, Response

from utils.base import ImplementationError, MilMoveEnv, is_local
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.rest import RestResponseContextManager, get_json_headers, parse_response_json
from utils.types import RequestKwargsType


logger = logging.getLogger(__name__)


@dataclass
class MilMoveRequestPreparer:
    """
    Class to help prepare for making requests to MilMove APIs based on the target environment.
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv

    GHC_PATH_PREFIX = "/ghc/v1"
    INTERNAL_PATH_PREFIX = "/internal"
    PRIME_PATH_PREFIX = "/prime/v1"
    SUPPORT_PATH_PREFIX = "/support/v1"

    def get_request_kwargs(self, certs_required: bool = False, endpoint_name: str = "") -> RequestKwargsType:
        """
        Grabs request kwargs that will be needed for the endpoint.

        :param certs_required: Boolean indicating if certs will be required. These will point to the
            paths for the TLS cert/key files, which change based on the environment being targetted.
            Possibly also includes a value that is either a boolean that indicates if the TLS certs
            should be verified, or a path to certs to use for verification.
        :param endpoint_name: name of endpoint, for locust request grouping
        :return: kwargs that can be passed to the request.
        """
        kwargs = {"headers": get_json_headers()}

        if certs_required:
            if is_local(env=self.env):
                kwargs.update(deepcopy(LOCAL_TLS_CERT_KWARGS))
            else:
                kwargs["cert"] = DP3_CERT_KEY_PEM

        if endpoint_name:
            kwargs["name"] = endpoint_name

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

    def form_ghc_path(self, endpoint: str, include_prefix: bool = True) -> str:
        """
        Returns a url pointing at the requested endpoint for the GHC API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :param include_prefix: Indicate if the GHC prefix should be included or not
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port=os.getenv("LOCAL_PORT", "8080"),
                local_protocol="http",
                local_subdomain="officelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="office")

        ghc_path = base_domain

        if include_prefix:
            ghc_path += self.GHC_PATH_PREFIX

        return f"{ghc_path}{endpoint}"

    def prep_ghc_request(
        self, endpoint: str, endpoint_name: str = "", include_prefix: bool = True
    ) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the GHC API.

        :param endpoint: endpoint to target, e.g. "/moves"
        :param endpoint_name: name of endpoint, for locust request grouping
        :param include_prefix: Indicate if the GHC prefix should be included or not
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_ghc_path(endpoint=endpoint, include_prefix=include_prefix)

        if endpoint_name:
            endpoint_name = f"{self.GHC_PATH_PREFIX}{endpoint_name}"

        kwargs = self.get_request_kwargs(endpoint_name=endpoint_name)

        return url, kwargs

    def form_internal_path(self, endpoint: str, include_prefix: bool = True) -> str:
        """
        Returns a url pointing at the requested endpoint for the Internal API.

        :param endpoint: Endpoint to target, e.g. "/moves"
        :param include_prefix: Indicate if the internal prefix should be included or not
        :return: full url to use in requests
        """
        if is_local(env=self.env):
            base_domain = self.form_base_domain(
                local_port=os.getenv("LOCAL_PORT", "8080"),
                local_protocol="http",
                local_subdomain="milmovelocal",
            )
        else:
            base_domain = self.form_base_domain(deployed_subdomain="my")

        internal_path = base_domain

        if include_prefix:
            internal_path += self.INTERNAL_PATH_PREFIX

        return f"{internal_path}{endpoint}"

    def prep_internal_request(
        self, endpoint: str, endpoint_name: str = "", include_prefix: bool = True
    ) -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Internal API.

        :param endpoint: endpoint to target, e.g. "/moves"
        :param endpoint_name: name of endpoint, for locust request grouping
        :param include_prefix: Indicate if the internal prefix should be included or not
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_internal_path(endpoint=endpoint, include_prefix=include_prefix)

        if endpoint_name:
            endpoint_name = f"{self.INTERNAL_PATH_PREFIX}{endpoint_name}"

        kwargs = self.get_request_kwargs(endpoint_name=endpoint_name)

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

        return f"{base_domain}{self.PRIME_PATH_PREFIX}{endpoint}"

    def prep_prime_request(self, endpoint: str, endpoint_name: str = "") -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Prime API.

        :param endpoint: endpoint to target, e.g. "/moves"
        :param endpoint_name: name of endpoint, for locust request grouping
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_prime_path(endpoint=endpoint)

        if endpoint_name:
            endpoint_name = f"{self.PRIME_PATH_PREFIX}{endpoint_name}"

        kwargs = self.get_request_kwargs(certs_required=True, endpoint_name=endpoint_name)

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

        return f"{base_domain}{self.SUPPORT_PATH_PREFIX}{endpoint}"

    def prep_support_request(self, endpoint: str, endpoint_name: str = "") -> tuple[str, RequestKwargsType]:
        """
        Prepares a request URL and the request kwargs for making a request to the Support API.

        :param endpoint: endpoint to target, e.g. "/moves"
        :param endpoint_name: name of endpoint, for locust request grouping
        :return: tuple of the full url to the endpoint and the kwargs to pass to the request
        """
        url = self.form_support_path(endpoint=endpoint)

        if endpoint_name:
            endpoint_name = f"{self.SUPPORT_PATH_PREFIX}{endpoint_name}"

        kwargs = self.get_request_kwargs(certs_required=True, endpoint_name=endpoint_name)

        return url, kwargs


class MilMoveRequestMixin:
    """
    Mixin for a Locust TaskSet class/subclass that provides access to a helper for forming request
    URLs and preparing request kwargs.
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv

    request_preparer: MilMoveRequestPreparer

    def __init__(self: Union[TaskSet, "MilMoveRequestMixin"], *args, **kwargs) -> None:
        """
        Sets up the env and request_preparer based on the input locust host. Note that the
        `self.user.host` value is set on the user class BEFORE initialization. This can be either
        the value set on the command line (via the --host flag) on the one set in the locust UI form
        field.
        """
        super().__init__(*args, **kwargs)

        self.set_milmove_env()
        self.set_up_request_preparer()

    def set_milmove_env(self: Union[TaskSet, "MilMoveRequestMixin"]) -> None:
        """
        Sets the env attribute for the class. Takes in a string and sets the MilMoveEnv in self.env.
        """
        self.env = MilMoveEnv(value=self.user.host)

    def set_up_request_preparer(self: Union[TaskSet, "MilMoveRequestMixin"]) -> None:
        """
        Sets up a URL creator that can be used later to form proper endpoint URLs
        """
        self.request_preparer = MilMoveRequestPreparer(env=self.env)


def log_response_info(response: Union[Response, RestResponseContextManager], task_name: str = "") -> None:
    """
    Function to uniformly log responses.

    :param response: response object
    :param task_name: optional task name to use in logging. Will default to calling function name.
    """
    if not task_name:
        task_name = inspect.stack()[1].function

    logger.info(f"ℹ️ {task_name} status code: {response.status_code} {response.reason}")


def format_response_display_message(response: Union[Response, RestResponseContextManager]) -> str:
    """
    Take a response and format text for displaying.

    :param response: response object.
    :return: text to display, e.g. in a log.
    """
    response_display = "No content found."  # Default that will get overwritten if content is found.

    if hasattr(response, "js"):
        response_json = response.js
    else:
        response_json, error_msg = parse_response_json(response=response)

        if error_msg:
            response_display = error_msg

    if response_json:
        response_display = json.dumps(response_json, indent=4)

    response_display = f"Response:\n\n{response_display}\n"

    return response_display


def format_request_display_message(request: PreparedRequest) -> str:
    """
    Take a request and format text for displaying.

    :param request: request object
    :return: text to display, e.g. in a log.
    """
    base_display_msg = f"Request:\n\n{request.method} {request.url}\n"

    if not request.body:
        return f"{base_display_msg}No content found."

    # Want to display the body a little nicer so we'll convert back to JSON so we can take advantage
    # of `json.dumps` formatting.

    # In case it fails to parse.
    raw_request_display = f"Error parsing body so here it is raw:\n{request.body}"

    try:
        body_json = json.loads(request.body)
    except json.JSONDecodeError:
        request_display = raw_request_display
    else:
        try:
            request_display = json.dumps(body_json, indent=4)
        except TypeError:
            request_display = raw_request_display

    return f"{base_display_msg}{request_display}\n"


def log_response_failure(response: Union[Response, RestResponseContextManager], task_name: str = "") -> None:
    """
    Function to uniformly log info if we decide a response should be considered a failure.

    :param response: response object
    :param task_name: optional task name to use in logging. Will default to calling function name.
    """
    if not task_name:
        task_name = inspect.stack()[1].function

    response_display = format_response_display_message(response=response)
    request_display = format_request_display_message(request=response.request)

    logger.error(f"\n⚠️ {task_name} failed.\n{response_display}\n{request_display}\n")
