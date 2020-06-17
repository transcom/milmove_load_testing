# -*- coding: utf-8 -*-
""" utils/base.py is for generic utilities that don't deserve their own file and may only be used in utils. """
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
