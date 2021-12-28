# -*- coding: utf-8 -*-
"""
This file is for generic utilities or helpers that don't merit having their own file yet.
"""

import logging
from enum import Enum


logger = logging.getLogger(__name__)


class ImplementationError(Exception):
    """Base exception when a utility hasn't been implemented correctly."""


class ValueEnum(Enum):
    @classmethod
    def values(cls):
        return [c.value for c in cls]

    @classmethod
    def names(cls):
        return [c.name for c in cls]

    @classmethod
    def validate(cls, value):
        return isinstance(value, cls) or value in cls.values()

    @classmethod
    def match(cls, value):
        """Returns the first literal that matches the value - throws an IndexError if not found."""
        return [c for c in cls if c == value or c.value == value][0]


class MilMoveEnv(ValueEnum):
    """
    Valid MilMove Environments that we will target to run load tests against.
    """

    LOCAL = "local"
    DP3 = "dp3"


def convert_host_string_to_milmove_env(host: str) -> MilMoveEnv:
    """
    Takes a host string and return the corresponding MilMoveEnv, if found.
    :param host: host string, e.g. "local"
    :return: MilMoveEnv matching the passed in host string, e.g. MilMoveEnv.LOCAL
    """
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
