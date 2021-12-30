# -*- coding: utf-8 -*-
"""
This file is for generic utilities or helpers that don't merit having their own file yet.
"""

import logging
from enum import Enum
from typing import Union

from utils.types import ValueEnumValueType

logger = logging.getLogger(__name__)


class ImplementationError(Exception):
    """Base exception when a utility hasn't been implemented correctly."""


class ValueEnum(Enum):
    """
    Enum with some extra methods to allow validating values and other helpers.
    """

    @classmethod
    def values(cls) -> list[ValueEnumValueType]:
        """
        Returns the values of all the enum members.

        :return: list of enum member values
        """
        return [c.value for c in cls]

    @classmethod
    def names(cls) -> list[str]:
        """
        Returns the names of all enum members

        :return: list of enum member names
        """
        return [c.name for c in cls]

    @classmethod
    def validate(cls, value: Union["ValueEnum", ValueEnumValueType]) -> bool:
        """
        Determines if the value passed in is either a member of the enum, or if it is the value of
        one of the members.

        :param value: value to check
        :return: boolean indicating if the value passed in is a valid member or member value.
        """
        return isinstance(value, cls) or value in cls.values()

    @classmethod
    def match(cls, value: Union["ValueEnum", ValueEnumValueType]) -> "ValueEnum":
        """
        Returns the first enum member that matches the input value. Will check if it is an enum
        member already, or if it matches an enum member value.

        Throws an IndexError if not found.

        :param value: value to check
        :return: matching enum member
        """
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
