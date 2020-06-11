# -*- coding: utf-8 -*-
import logging
from enum import Enum

logger = logging.getLogger(__name__)


class ImplementationError(Exception):
    """ Base exception when a util hasn't been implemented correctly. """


class ListEnum(Enum):
    @classmethod
    def values(cls):
        return [c.value for c in cls]

    @classmethod
    def names(cls):
        return [c.name for c in cls]


class MilMoveEnv(ListEnum):
    LOCAL = "local"
    STAGING = "staging"
    EXPERIMENTAL = "experimental"


class MilMoveDomain(ListEnum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"

    @property
    def local_value(self):
        return f"{self.value}local"

    @property
    def deployed_value(self):
        value = self.value

        if self.value == self.MILMOVE.value:
            value = "my"

        return value

    def host_name(self, env, is_api=False, port=3000):
        """
        Returns the host name for this domain based on the environment, whether or not it is in the API domain, and the
        port (for local envs).
        :param env: str (MilMoveEnv)
        :param is_api: bool
        :param port: int, 4 digits
        :return: str host
        """
        if env not in MilMoveEnv.values():
            logger.debug(f"bad env value: {env}")
            raise ImplementationError("Environment for determining host name must be in MilMoveEnv constants.")

        if env == MilMoveEnv.LOCAL.value:
            return f"https://{self.local_value}:{port}"

        return f"https://{'api' if is_api else self.deployed_value}.{env}.move.mil"


class MilMoveUserMixin:
    """
    Mixin to set a host value based on the environment passed in as the --host flag.
    """

    local_port = 8080
    domain = MilMoveDomain.MILMOVE  # any MilMoveDomain value
    host_path = ""  # appended to the end of the host name, ex. /prime/v1
    is_api = False  # if True, defaults to using the api.<env>.move.mil domain for deployed envs

    def __init__(self, *args, **kwargs):
        """
        Sets host based on environment value from --host flag in command.
        """
        if self.host in MilMoveEnv.values():
            self.host = self.set_host_name()

        super().__init__(*args, **kwargs)

    def set_host_name(self):
        """
        Gets the host name based on the domain, environment, and API status.
        """
        # check for the enum constant or the string value:
        if self.domain not in MilMoveDomain and self.domain not in MilMoveDomain.values():
            logger.debug(f"bad domain value: {self.domain}")
            raise ImplementationError("Domain for MilMoveUser must be one of the constants in MilMoveDomain.")

        host = self.domain.host_name(self.host, self.is_api, self.local_port)

        return f"{host}{self.host_path}"
