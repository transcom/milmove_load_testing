# -*- coding: utf-8 -*-
"""
Tests for utils/rest.py
"""
import json
from json import JSONDecodeError
from typing import Optional
from unittest.mock import patch

from utils.rest import get_json_headers, parse_response_json


class TestGetJSONHeaders:
    """
    Tests for get_json_headers
    """

    def test_returns_expected_headers(self) -> None:
        assert {"Content-Type": "application/json", "Accept": "application/json"} == get_json_headers()


@patch("utils.rest.RestResponseContextManager", autospec=True)
class TestParseResponseToDict:
    """
    Tests for parse_response_json
    """

    def test_returns_proper_error_message_if_response_text_is_none(self, mock_response):
        mock_response.text = None

        response_time = 10.35153  # In seconds
        mock_response.request_meta.__getitem__.return_value = response_time * 1000  # Needs to be in ms

        response_error = "Server Error"
        mock_response.error = response_error

        response_status_code = 500
        mock_response.status_code = response_status_code

        parsed_json, error_message = parse_response_json(mock_response)

        assert not parsed_json

        assert str(response_time) not in error_message
        assert str(round(response_time, 1)) in error_message
        assert response_error in error_message
        assert str(response_status_code) in error_message

    def test_returns_empty_dict_and_err_msg_if_no_error_and_no_text(self, mock_response):
        mock_response.text = ""

        parsed_json, error_message = parse_response_json(mock_response)

        assert not parsed_json
        assert not error_message

    def test_returns_proper_error_message_if_response_text_is_not_json(self, mock_response):
        mock_response.text = "Not Authorized"

        response_status_code = 403
        mock_response.status_code = response_status_code

        exc: Optional[JSONDecodeError] = None

        try:
            json.loads(mock_response.text)
        except JSONDecodeError as e:
            exc = e

        mock_response.json.side_effect = exc
        parsed_json, error_message = parse_response_json(mock_response)

        assert not parsed_json

        assert "Could not parse response as JSON." in error_message
        assert mock_response.text in error_message
        assert str(response_status_code) in error_message
        assert str(exc) in error_message
