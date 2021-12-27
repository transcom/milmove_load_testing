# -*- coding: utf-8 -*-
"""
This file is to hold request-related code, meaning code that help make api requests, such as
url-forming functions.
"""
import os
from copy import deepcopy
from enum import Enum
from typing import Optional, Union

from locust import User

from utils.base import ImplementationError, MilMoveEnv, convert_host_string_to_milmove_env, is_local
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS


class MilMoveSubdomain(Enum):
    """
    Valid subdomains
    """

    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"


class MilMoveRequestMixin:
    """
    Mixin for a Locust User class/subclass that provides helper functions to form urls based on the
    host (as passed in the --host flag) and .
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv = None

    # The HTTP protocol and port used for a local host:
    local_protocol: str = "https"
    local_port: str = "0000"

    def __init__(self: Union[User, "MilMoveRequestMixin"], *args, **kwargs) -> None:
        """
        Sets up the env based on value from the --host flag. Note that the `self.host` value is set
        on the class from the command line flag BEFORE initialization.
        """
        self.set_milmove_env()

        super().__init__(*args, **kwargs)

    def set_milmove_env(self: Union[User, "MilMoveRequestMixin"]) -> None:
        """
        Sets the env attribute for the class. Takes in a string and sets the MilMoveEnv in self.env.
        """
        self.env = convert_host_string_to_milmove_env(host=self.host)

    def get_base_domain(self, local_subdomain: MilMoveSubdomain) -> str:
        """
        Wrapper for `form_base_domain` that passes in the appropriate kwargs for this user.
        :param local_subdomain: subdomain to use when running locally, e.g. MilMoveSubdomain.PRIME
        :return: base domain to use for requests.
        """
        return form_base_domain(
            running_against_local=is_local(env=self.env),
            local_protocol=self.local_protocol,
            local_subdomain=local_subdomain,
            local_port=self.local_port,
        )

    def get_ghc_path(self, endpoint: str) -> str:
        """
        Wrapper for `form_ghc_path`, using the domain that this user should use.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        base_domain = self.get_base_domain(local_subdomain=MilMoveSubdomain.OFFICE)

        return form_ghc_path(base_domain=base_domain, endpoint=endpoint)

    def get_internal_path(self, endpoint: str) -> str:
        """
        Wrapper for `form_internal_path`, using the domain that this user should use.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        base_domain = self.get_base_domain(local_subdomain=MilMoveSubdomain.MILMOVE)

        return form_internal_path(base_domain=base_domain, endpoint=endpoint)

    def get_prime_path(self, endpoint: str) -> str:
        """
        Wrapper for `form_prime_path`, using the domain that this user should use.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        base_domain = self.get_base_domain(local_subdomain=MilMoveSubdomain.PRIME)

        return form_prime_path(base_domain=base_domain, endpoint=endpoint)

    def get_support_path(self, endpoint: str) -> str:
        """
        Wrapper for `form_support_path`, using the domain that this user should use.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        base_domain = self.get_base_domain(local_subdomain=MilMoveSubdomain.PRIME)

        return form_support_path(base_domain=base_domain, endpoint=endpoint)

    @property
    def cert_kwargs(self) -> dict[str, Union[str, bool]]:
        """
        Wrapper for `get_cert_kwargs`, using the env for this user.
        :return: dict with cert kwargs
        """
        return get_cert_kwargs(env=self.env)


def get_cert_kwargs(env: MilMoveEnv) -> dict[str, Union[str, bool]]:
    """
    Get the certificate kwargs that will be used for validating the HTTPS requests. These will point
    to the file paths for the TLS cert/key files. The files used will change based on the
    environment.
    :return: dict with one key/value pair that will point to a cert, and possibly a second that
    either indicates if the TLS certificates should be verified or a path to certs to use.
    """
    if env == MilMoveEnv.LOCAL:
        return deepcopy(LOCAL_TLS_CERT_KWARGS)

    # We now know we're in a deployed environment, so let's make a deployed cert/key file:
    return {"cert": DP3_CERT_KEY_PEM}


def form_base_domain(
    running_against_local: bool,
    local_protocol: str = "http",
    local_subdomain: Optional[MilMoveSubdomain] = None,
    local_port: str = "0000",
) -> str:
    """
    Sets up the base domain for a request based on the environment we're running against and
    the subdomain we're targeting.

    Con optionally be overridden by setting an environment variable called BASE_DOMAIN that
    points to where you want it to point.
    :param running_against_local: boolean indicating if we're running against a local server or not
    :param local_protocol: local protocol to run against, e.g. "https"
    :param local_subdomain: subdomain to target, e.g. MilMoveSubdomain.PRIME. Only needed when
        running locally.
    :param local_port: Port to use when running locally.
    :return: base domain to use for requests, e.g. https://api.loadtest.dp3.us
    """
    if base_domain := os.getenv("BASE_DOMAIN"):
        return base_domain

    if not running_against_local:
        # NOTE: deployed protocol is always https
        return "https://api.loadtest.dp3.us"

    port = str(local_port)  # just in case an int was set

    if not (port.isdigit() and len(port) == 4):
        raise ImplementationError("The local port must be a string of 4 digits.")

    if not isinstance(local_subdomain, MilMoveSubdomain):
        raise ImplementationError("The subdomain must be a valid MilMoveSubdomain.")

    return f"{local_protocol}://{local_subdomain.value}local:{port}"


def form_ghc_path(base_domain: str, endpoint: str) -> str:
    """
    Returns a url pointing at the requested endpoint for the GHC API.
    :param base_domain: Base domain for request, e.g. http://officelocal:8080
    :param endpoint: Endpoint to target, e.g. "/moves"
    :return: full url to use in requests
    """
    return f"{base_domain}/ghc/v1{endpoint}"


def form_internal_path(base_domain: str, endpoint: str) -> str:
    """
    Returns a url pointing at the requested endpoint for the Internal API.
    :param base_domain: Base domain for request, e.g. http://milmovelocal:8080
    :param endpoint: Endpoint to target, e.g. "/moves"
    :return: full url to use in requests
    """
    return f"{base_domain}/internal{endpoint}"


def form_prime_path(base_domain: str, endpoint: str) -> str:
    """
    Returns a url pointing at the requested endpoint for the Prime API.
    :param base_domain: Base domain for request, e.g. https://primelocal:9443
    :param endpoint: Endpoint to target, e.g. "/moves"
    :return: full url to use in requests
    """
    return f"{base_domain}/prime/v1{endpoint}"


def form_support_path(base_domain: str, endpoint: str) -> str:
    """
    Returns a url pointing at the requested endpoint for the Support API.
    :param base_domain: Base domain for request, e.g. https://primelocal:9443
    :param endpoint: Endpoint to target, e.g. "/moves"
    :return: full url to use in requests
    """
    return f"{base_domain}/support/v1{endpoint}"
