# -*- coding: utf-8 -*-
"""
Place to house any custom types we need for our code.
"""
from typing import Type, TypeVar

from locust.runners import Runner

# We can get different subclasses of the Runner class depending on how we run things so to indicate
# that, we use this variable (R) with `Type`, e.g. Type[R]
R = TypeVar("R", bound=Runner)

LOCUST_RUNNER_TYPE = Type[R]

ExceptionType = TypeVar("ExceptionType", bound=BaseException)
