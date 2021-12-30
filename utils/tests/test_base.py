# -*- coding: utf-8 -*-
"""
Tests for utils/base.py
"""
from typing import Union

import pytest

from utils.base import ValueEnum


class MyValueEnum(ValueEnum):
    """
    Fake value enum for testing
    """

    CHOCOLATE = "chocolate"
    MARSHMALLOW = "marshmallow"
    CANDY_CANE = "candy cane"


class Pet(ValueEnum):
    """
    Other fake enum for testing
    """

    CAT = "cat"
    DOG = "dog"
    BIRD = "bird"
    SNAKE = "snake"


class TestValueEnum:
    """
    Tests for ValueEnum
    """

    def test_values_returns_list_of_member_values(self) -> None:
        assert MyValueEnum.values() == ["chocolate", "marshmallow", "candy cane"]

    def test_names_returns_list_of_member_names(self) -> None:
        assert MyValueEnum.names() == ["CHOCOLATE", "MARSHMALLOW", "CANDY_CANE"]

    @pytest.mark.parametrize(
        "value_to_validate,value_is_valid",
        [
            ("chocolate", True),
            (MyValueEnum.CHOCOLATE, True),
            ("pancake", False),
            (Pet.CAT, False),
        ],
    )
    def test_validate_can_properly_check_for_enum_members_and_member_values(
        self, value_to_validate: Union[str, ValueEnum], value_is_valid: bool
    ) -> None:
        assert MyValueEnum.validate(value=value_to_validate) == value_is_valid

    @pytest.mark.parametrize(
        "value_to_match,expected_member",
        [
            ("chocolate", MyValueEnum.CHOCOLATE),
            (MyValueEnum.CHOCOLATE, MyValueEnum.CHOCOLATE),
        ],
    )
    def test_match_will_return_enum_member_if_found(
        self, value_to_match: Union[str, ValueEnum], expected_member: bool
    ) -> None:
        assert MyValueEnum.match(value=value_to_match) == expected_member

    @pytest.mark.parametrize(
        "value_to_match",
        ["cat", Pet.CAT],
    )
    def test_match_raise_an_error_if_member_not_found(self, value_to_match: Union[str, ValueEnum]) -> None:
        with pytest.raises(IndexError):
            MyValueEnum.match(value=value_to_match)
