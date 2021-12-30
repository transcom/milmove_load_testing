# -*- coding: utf-8 -*-
""" utils/hosts.py is for the tools that handle setting the MilMove hostnames and setting up TLS certs. """
import logging
import os
from copy import deepcopy
from enum import Enum
from typing import Optional, Union

from locust import User

from utils.base import (
    ImplementationError,
    MilMoveEnv,
    is_local,
)
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS

logger = logging.getLogger(__name__)


class MilMoveDomain(Enum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"

    @property
    def local_value(self) -> str:
        return f"{self.value}local"

    def host_name(
        self,
        env: str,
        port: str = "0000",
        protocol: str = "https",
        deployed_subdomain: str = "",
    ) -> str:
        """
        Returns the host name for this domain based on the environment, port, and protocol
         (for local envs).

        :param env: MilMoveEnv, e.g. local
        :param port: 4 digit port to point at
        :param protocol: "https" or "http"
        :param deployed_subdomain: API subdomain when deployed, e.g. "api" or "my"
        :return: host, e.g. https://api.loadtest.dp3.us
        """
        if isinstance(env, MilMoveEnv):
            env = env.value  # ensure that we're using the value string instead of the Enum literal

        milmove_env = MilMoveEnv(value=env)

        if milmove_env == MilMoveEnv.LOCAL:
            port = str(port)  # just in case an int was passed in
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"{protocol}://{self.local_value}:{port}"

        # allow us to point to another domain if we need to
        base_domain = os.getenv("BASE_DOMAIN", "loadtest.dp3.us")
        # NOTE: deployed protocol is always https
        return f"https://{deployed_subdomain}.{base_domain}"


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

    # The subdomain to use when deployed, e.g. "api" or "my"
    deployed_subdomain: str = "api"

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
        try:
            type(self).set_milmove_env(self.host)
        except ValueError:
            pass
        else:
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

        cls.env = MilMoveEnv(value=env)

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
            cls.host = MilMoveDomain(cls.domain).host_name(
                env=cls.env.value,
                port=cls.local_port,
                protocol=cls.local_protocol,
                deployed_subdomain=cls.deployed_subdomain,
            )

            cls.alternative_host = MilMoveDomain.MILMOVE.host_name(
                env=cls.env.value,
                port="8080",
                protocol="http",
                deployed_subdomain=cls.deployed_subdomain,
            )
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

        if is_local(env=cls.env):
            cls.cert_kwargs = deepcopy(LOCAL_TLS_CERT_KWARGS)
        else:
            cls.cert_kwargs = {"cert": DP3_CERT_KEY_PEM}

    @property
    def is_local(self):
        """Indicates if this user is using the local environment."""
        return is_local(env=self.env)

    @property
    def is_deployed(self):
        """Indicates if this user is running in a deployed environment."""
        return not is_local(env=self.env)
