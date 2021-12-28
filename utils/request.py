# -*- coding: utf-8 -*-
"""
This file is to hold request-related code, meaning code that help make api requests, such as
url-forming functions.
"""
import os
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from typing import Union

from locust import User

from utils.base import ImplementationError, MilMoveEnv, convert_host_string_to_milmove_env, is_local
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS


@dataclass
class MilMoveURLCreator:
    """
    Class to manage MilMove URLs based on the target environment
    """

    # The environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv

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
        :param local_subdomain: subdomain to target when running locally, e.g. MilMoveSubdomain.PRIME.
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
    env: MilMoveEnv

    url_creator: MilMoveURLCreator

    def __init__(self: Union[User, "MilMoveRequestMixin"], *args, **kwargs) -> None:
        """
        Sets up the env based on value from the --host flag. Note that the `self.host` value is set
        on the class from the command line flag BEFORE initialization.
        """
        self.set_milmove_env()
        self.set_up_url_creator()

        super().__init__(*args, **kwargs)

    def set_milmove_env(self: Union[User, "MilMoveRequestMixin"]) -> None:
        """
        Sets the env attribute for the class. Takes in a string and sets the MilMoveEnv in self.env.
        """
        self.env = convert_host_string_to_milmove_env(host=self.host)

    def set_up_url_creator(self: Union[User, "MilMoveRequestMixin"]) -> None:
        """
        Sets up a URL creator that can be used later to form proper endpoint URLs
        """
        self.url_creator = MilMoveURLCreator(env=self.env)

    def get_ghc_path(self, endpoint: str) -> str:
        """
        Wrapper for `url_creator.form_ghc_path`.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        return self.url_creator.form_ghc_path(endpoint=endpoint)

    def get_internal_path(self, endpoint: str) -> str:
        """
        Wrapper for `url_creator.form_internal_path`.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        return self.url_creator.form_internal_path(endpoint=endpoint)

    def get_prime_path(self, endpoint: str) -> str:
        """
        Wrapper for `url_creator.form_prime_path`.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        return self.url_creator.form_prime_path(endpoint=endpoint)

    def get_support_path(self, endpoint: str) -> str:
        """
        Wrapper for `url_creator.form_support_path`.
        :param endpoint: Endpoint to target, e.g. "/moves"
        :return: fully formed path to endpoint.
        """
        return self.url_creator.form_support_path(endpoint=endpoint)

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
