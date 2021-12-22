# -*- coding: utf-8 -*-
""" utils/hosts.py is for the tools that handle setting the MilMove hostnames and setting up TLS certs. """
import logging
import os
from copy import deepcopy
from enum import Enum
from typing import Optional, Union

from locust import User

from .base import ImplementationError, ValueEnum
from .constants import DOD_CA_BUNDLE, DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS

logger = logging.getLogger(__name__)


class MilMoveEnv(ValueEnum):
    LOCAL = "local"
    DP3 = "dp3"


class MilMoveDomain(ValueEnum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"

    @property
    def local_value(self) -> str:
        return f"{self.value}local"

    def host_name(self, env: str, port: str = "0000", protocol: str = "https") -> str:
        """
        Returns the host name for this domain based on the environment, port, and protocol
         (for local envs).
        :param env: MilMoveEnv, e.g. local
        :param port: 4 digit port to point at
        :param protocol: "https" or "http"
        :return: host, e.g. https://api.loadtest.dp3.us
        """
        if isinstance(env, MilMoveEnv):
            env = env.value  # ensure that we're using the value string instead of the Enum literal

        if env not in MilMoveEnv.values():
            raise ImplementationError("The environment for determining the host name must be included in MilMoveEnv.")

        if env == MilMoveEnv.LOCAL.value:
            port = str(port)  # just in case an int was passed in
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"{protocol}://{self.local_value}:{port}"

        # allow us to point to another domain if we need to
        base_domain = os.getenv("BASE_DOMAIN", "loadtest.dp3.us")
        # NOTE: deployed protocol is always https
        return f"https://api.{base_domain}"


class MilMoveHostMixin:
    """
    Mixin for Locust's HttpUser class that sets a host value based on the environment passed in as the --host flag.
    """

    # The abbreviated domain name for the host. Can be any of the values in MilMoveDomain.
    domain: MilMoveDomain = None

    # The abbreviated name of the environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv = None

    # The HTTP protocol and port used for a local host:
    local_protocol: str = "https"
    local_port: str = "0000"

    # The set of kwargs that will be used to authenticate an HTTP request, in the format:
    # {"cert": <cert/key file path(s)>, "verify": <False or the CA bundle file path>}
    cert_kwargs: Optional[dict] = None

    # domain name for the MILMOVE/customer portion of the app
    alternative_host = None

    def __init__(self, *args, **kwargs):
        """
        Sets the Users' host based on environment value from --host flag in command. Note that the self.host value is
        set on the class from the command line flag BEFORE initialization. Also sets the env and cert_kwargs, the input
        needed for TLS requests, values.

        These attributes are set on the CLASS-level. This is important because we do not want to repeat this process for
        thousands of Users with the exact same settings.
        """
        # Check if the host value is one of our accepted environments. If not, we'll continue with the host entered
        # as-is and skip the rest of the custom setup.
        if MilMoveEnv.validate(self.host):
            type(self).set_milmove_env(self.host)
            type(self).host = None
            type(self).set_host_name()
            type(self).set_cert_kwargs()

        super().__init__(*args, **kwargs)

    @classmethod
    def set_milmove_env(cls, env: str):
        """
        Sets the environment attribute for the class. Takes in a string and sets a MilMoveEnv literal to cls.env.
        """
        # Check if we already have a value set (this would be purposeful):
        if cls.env:
            return

        try:
            cls.env = MilMoveEnv.match(env)
        except IndexError:  # means MilMoveEnv could not find a match for the value passed in
            logger.debug(f"Bad env value: {env}")
            raise ImplementationError("Environment for MilMoveHostMixin must match one of the values in MilMoveEnv.")

    @classmethod
    def set_host_name(cls: Union[User, "MilMoveHostMixin"]):
        """
        Sets the hostname based on the domain, environment, and whether or not it is an API.

        Applies to every instance of the class (or subclass), which reduces the number of times this value will be
        calculated for users with the exact same attributes to only once during a load test.
        """
        # Check if we already have a value set (this would be purposeful):
        if cls.host:
            return

        try:
            cls.host = MilMoveDomain.match(cls.domain).host_name(
                env=cls.env.value, port=cls.local_port, protocol=cls.local_protocol
            )
            cls.alternative_host = MilMoveDomain.MILMOVE.host_name(env=cls.env.value, port="8080", protocol="http")
        except IndexError:  # means MilMoveDomain could not find a match for the value passed in
            logger.debug(f"Bad domain value: {cls.domain}")
            raise ImplementationError("Domain for MilMoveHostMixin must match one of the values in MilMoveDomain.")

    @classmethod
    def set_cert_kwargs(cls):
        """
        Sets the certificate kwargs that will be used for validating the HTTPS request from this user. These will point
        to the file paths for the TLS cert/key files and the DoD's CA bundle file. The files used will change based on
        the environment.

        Applies to every instance of the class (or subclass), which reduces the number of times this value will be
        calculated for users with the exact same attributes to only once during a load test.
        """
        # Check if we already have a value set (this would be purposeful) and skip the logic to create it again:
        if cls.cert_kwargs:
            return

        if cls.env == MilMoveEnv.LOCAL:
            cls.cert_kwargs = deepcopy(LOCAL_TLS_CERT_KWARGS)
            return

        verify_path = DOD_CA_BUNDLE
        # DP3 certs are issued by CAs that are well known and so we
        # don't need any special verification
        if cls.env == MilMoveEnv.DP3:
            verify_path = None

        # We also need to use the DoD's specific CA bundle for SSL verification in deployed envs:
        cls.cert_kwargs = {"cert": DP3_CERT_KEY_PEM, "verify": verify_path}

    @property
    def is_local(self):
        """Indicates if this user is using the local environment."""
        return self.env == MilMoveEnv.LOCAL

    @property
    def is_deployed(self):
        """Indicates if this user is running in a deployed environment."""
        return self.env != MilMoveEnv.LOCAL


class MilMoveSubdomain(Enum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"
    SUPPORT = "support"


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
        Sets the env attribute for the class. Takes in a string and sets the MilMoveEnv in cls.env.
        """
        try:
            self.env = MilMoveEnv.match(self.host)
        except IndexError:  # means MilMoveEnv could not find a match for the value passed in
            logger.debug(f"Bad host value: {self.host}")

            raise ImplementationError("Environment for MilMoveHostMixin must match one of the values in MilMoveEnv.")

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
        base_domain = self.get_base_domain(local_subdomain=MilMoveSubdomain.SUPPORT)

        return form_support_path(base_domain=base_domain, endpoint=endpoint)

    @property
    def cert_kwargs(self) -> dict[str, Union[str, bool]]:
        """
        Wrapper for `get_cert_kwargs`, using the env for this user.
        :return: dict with cert kwargs
        """
        return get_cert_kwargs(env=self.env)


def set_up_certs(host: str) -> None:
    """
    Sets up certs for making requests to the mymove server
    :param host: host that the target server is running in, e.g. dp3
    :return: None
    """
    if host == MilMoveEnv.LOCAL.value:
        return  # We don't need to set up certs for a local run because they already exist

    host_upper = host.upper()

    try:
        deployed_tls_cert = os.environ[f"MOVE_MIL_{host_upper}_TLS_CERT"]
        deployed_tls_key = os.environ[f"MOVE_MIL_{host_upper}_TLS_KEY"]
    except KeyError:
        logger.debug(f"Unable to find cert and key values for environment: {host}")

        raise ImplementationError(
            "Cannot run load testing in a deployed environment without the matching certificate and key."
        ) from None

    with open(DP3_CERT_KEY_PEM, "w") as f:
        f.write(deployed_tls_cert)
        f.write("\n")
        f.write(deployed_tls_key)


def remove_certs(host: str) -> None:
    """
    Removes certs that were set up for making requests to the mymove server
    :param host: host that the target server is running in, e.g. dp3
    :return: None
    """
    if host == MilMoveEnv.LOCAL.value:
        return  # We don't need to delete local certs since they're part of the repo

    try:
        os.remove(DP3_CERT_KEY_PEM)
    except FileNotFoundError:
        # FileNotFoundError means the file was already removed.
        pass


def convert_host_string_to_milmove_env(host: str) -> MilMoveEnv:
    try:
        return MilMoveEnv.match(host)
    except IndexError:  # means MilMoveEnv could not find a match for the value passed in
        logger.debug(f"Bad host value: {host}")

        raise ImplementationError(
            "Environment for MilMoveHostMixin must match one of the values in MilMoveEnv."
        ) from None


def is_local(env: MilMoveEnv) -> bool:
    """
    Indicates if this user is using the local environment.
    :return: bool indicating if we are running in the local env or not
    """
    return env == MilMoveEnv.LOCAL


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
    return f"{base_domain}/ghc/v1{endpoint}"


def form_internal_path(base_domain: str, endpoint: str) -> str:
    return f"{base_domain}/internal{endpoint}"


def form_prime_path(base_domain: str, endpoint: str) -> str:
    return f"{base_domain}/prime/v1{endpoint}"


def form_support_path(base_domain: str, endpoint: str) -> str:
    return f"{base_domain}/support/v1{endpoint}"
