# -*- coding: utf-8 -*-
""" utils/hosts.py is for the tools that handle setting the MilMove hostnames and setting up TLS certs. """
import logging

from .base import ImplementationError, ListEnum

logger = logging.getLogger(__name__)


class MilMoveEnv(ListEnum):
    LOCAL = "local"
    EXP = "exp"
    STG = "stg"


class MilMoveDomain(ListEnum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"

    @property
    def local_value(self):
        return f"{self.value}local"

    @property
    def deployed_value(self):
        if self.value == self.MILMOVE.value:
            return "my"

        return self.value

    def host_name(self, env, is_api=False, port="3000", protocol="https"):
        """
        Returns the host name for this domain based on the environment, whether or not it is in the API domain, and the
        port and protocol (for local envs).
        :param env: str MilMoveEnv
        :param is_api: bool
        :param port: str containing 4 digits
        :param protocol: str "https" or "http"
        :return: str host
        """
        if isinstance(env, MilMoveEnv):
            env = env.value  # ensure that we're using the value string instead of the Enum literal

        if env not in MilMoveEnv.values():
            raise ImplementationError("The environment for determining the host name must be included in MilMoveEnv.")

        if env == MilMoveEnv.LOCAL.value:
            port = str(port)  # in case an int was passed in
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"{protocol}://{self.local_value}:{port}"

        # NOTE: deployed protocol is always https
        return f"https://{'api' if is_api else self.deployed_value}.{env}.move.mil"


class MilMoveHostMixin:
    """
    Mixin for Locust's HttpUser class that sets a host value based on the environment passed in as the --host flag.
    """

    domain = MilMoveDomain.MILMOVE  # any MilMoveDomain value
    local_protocol = "https"
    local_port = "8080"
    is_api = False  # if True, defaults to using the api.<env>.move.mil domain for deployed envs

    cert_kwargs = None  # TODO

    def __init__(self, *args, **kwargs):
        """
        Sets host based on environment value from --host flag in command. Note that the self.host attribute is set on
        the User class by the locust CLI utility BEFORE initialization.
        """
        # Check if the host value is one of our accepted environments, then set the correct hostname:
        if MilMoveEnv.validate(self.host):
            self.env = self.host  # preserve the original environment value that was passed in on the command line
            self.host = self.set_host_name()  # set the actual host based on the env

        # If the host was not a MilMoveEnv value, we'll continue with the host the user entered as-is and skip all
        # customization of the hostname

        super().__init__(*args, **kwargs)

    def set_host_name(self):
        """
        Gets the host name based on the domain, environment, and API status.
        """
        if not MilMoveDomain.validate(self.domain):
            logger.debug(f"Bad domain value: {self.domain}")
            raise ImplementationError("Domain for MilMoveHostMixin must match one of the values in MilMoveDomain.")

        return MilMoveDomain.match(self.domain).host_name(self.env, self.is_api, self.local_port, self.local_protocol)
