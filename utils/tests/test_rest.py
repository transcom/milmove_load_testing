# -*- coding: utf-8 -*-
"""
Tests for utils/rest.py
"""
from utils.rest import (
    get_json_headers,
)


class TestGetJSONHeaders:
    """
    Tests for get_json_headers
    """

    def test_returns_expected_headers(self) -> None:
        assert {"Content-Type": "application/json", "Accept": "application/json"} == get_json_headers()
