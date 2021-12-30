# -*- coding: utf-8 -*-
"""
This file is for generic utilities or helpers that don't merit having their own file yet.
"""

import logging
from enum import Enum

logger = logging.getLogger(__name__)


class ImplementationError(Exception):
    """Base exception when a utility hasn't been implemented correctly."""


class MilMoveEnv(Enum):
    """
    Valid MilMove Environments that we will target to run load tests against.
    """

    LOCAL = "local"
    DP3 = "dp3"


def is_local(env: MilMoveEnv) -> bool:
    """
    Indicates if this user is using the local environment.
    :return: bool indicating if we are running in the local env or not
    """
    return env == MilMoveEnv.LOCAL
