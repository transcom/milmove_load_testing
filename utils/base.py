# -*- coding: utf-8 -*-
""" utils/base.py is for generic utilities that don't deserve their own file and may only be used in utils. """
from enum import Enum


class ImplementationError(Exception):
    """ Base exception when a util hasn't been implemented correctly. """


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
        """ Returns the first literal that matches the value - throws an IndexError if not found. """
        return [c for c in cls if c == value or c.value == value][0]
