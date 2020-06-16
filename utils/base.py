# -*- coding: utf-8 -*-
""" utils/base.py is for generic utilities that don't deserve their own file """
from enum import Enum


class ImplementationError(Exception):
    """ Base exception when a util hasn't been implemented correctly. """


class ListEnum(Enum):
    @classmethod
    def values(cls):
        return [c.value for c in cls]

    @classmethod
    def names(cls):
        return [c.name for c in cls]

    @classmethod
    def validate(cls, value):
        return value in cls or value in cls.values()


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
        if self.value == self.MILMOVE.value:
            return "my"

        return self.value

    def host_name(self, env, is_api=False, port="3000"):
        """
        Returns the host name for this domain based on the environment, whether or not it is in the API domain, and the
        port (for local envs).
        :param env: str MilMoveEnv
        :param is_api: bool
        :param port: str containing 4 digits
        :return: str host
        """
        if env in MilMoveEnv:
            env = env.value  # ensure that we're using the value string instead of the Enum literal

        if env not in MilMoveEnv.values():
            raise ImplementationError("The environment for determining the host name must be included in MilMoveEnv.")

        if env == MilMoveEnv.LOCAL.value:
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"https://{self.local_value}:{port}"

        return f"https://{'api' if is_api else self.deployed_value}.{env}.move.mil"
