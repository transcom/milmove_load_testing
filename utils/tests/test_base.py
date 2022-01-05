# -*- coding: utf-8 -*-
"""
Tests for utils/base.py
"""
import pytest

from utils.base import MilMoveEnv, is_local


@pytest.mark.parametrize("env,expected_result", ((MilMoveEnv.LOCAL, True), (MilMoveEnv.DP3, False)))
def test_is_local(env: MilMoveEnv, expected_result: bool) -> None:
    assert is_local(env=env) == expected_result
