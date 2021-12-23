# -*- coding: utf-8 -*-
"""
Place to house any custom types we need for our code.
"""
from typing import Iterator, Protocol, Type, TypeVar, Union

from locust.runners import Runner

# We can get different subclasses of the Runner class depending on how we run things so to indicate
# that, we use this variable (R) with `Type`, e.g. Type[R]
R = TypeVar("R", bound=Runner)

LOCUST_RUNNER_TYPE = Type[R]

ExceptionType = TypeVar("ExceptionType", bound=BaseException)

# Turns out that getting the correct type for JSON is hard...
# Python typing GH issue: https://github.com/python/typing/issues/182
# The above talks about how this won't really be supported easily until mypy supports recursive
# definitions. Here is the mypy recursive GH issue: https://github.com/python/mypy/issues/731
# So based on what I found others using until a better solution is available, we can use this:

JSONValue = Union[str, int, float, bool, None, "JSONObject", "JSONArray"]


# Mapping with string as keys, and JSONValue as values
class JSONObject(Protocol):
    def __setitem__(self, k: str, v: JSONValue) -> None:
        ...

    def __delitem__(self, v: str) -> None:
        ...

    def __getitem__(self, k: str) -> JSONValue:
        ...

    def __iter__(self) -> Iterator[str]:
        ...


# Array is List with keys of type `int`
class JSONArray(Protocol):
    def insert(self, index: int, value: JSONValue) -> None:
        ...

    def __getitem__(self, i: int) -> JSONValue:
        ...

    def __setitem__(self, i: int, o: JSONValue) -> None:
        ...

    def __delitem__(self, i: int) -> None:
        ...


JSONType = Union[JSONValue, JSONObject, JSONArray]
