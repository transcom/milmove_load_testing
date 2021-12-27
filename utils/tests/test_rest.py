# -*- coding: utf-8 -*-
"""
Tests for utils/rest.py
"""
import json
from json import JSONDecodeError
from typing import NoReturn, Optional
from unittest.mock import patch

from utils.rest import format_failure_msg_from_exception, get_json_headers, parse_response_json
from utils.types import ExceptionType


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


class TestFormatTraceBackToErrorMessage:
    """
    Tests for format_failure_msg_from_exception
    """

    def test_puts_exception_class_in_msg(self) -> None:
        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert formatted_message.startswith("AttributeError")

    def test_puts_exception_message_in_msg(self) -> None:
        error_text = "Task has no attribute 'run'"

        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert error_text in formatted_message

    def test_puts_traceback_info_in_msg(self) -> None:
        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        assert formatted_message.count(__file__) == 1
        assert str(exc.__traceback__.tb_lineno) in formatted_message

    def test_puts_nested_traceback_in_msg(self) -> None:
        error_text = "Task has no attribute 'run'"

        def nested_func() -> NoReturn:
            """
            Nested function that just raises an exception.
            """
            raise AttributeError(error_text)

        # Initializing it in this one so that the IDE doesn't think we might reference it before it
        # is set. For some reason, the IDE doesn't know that the nested_func always raises an
        # exception...
        exc: ExceptionType = AttributeError("This should be overwritten by the exception raised later...")

        try:
            nested_func()
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc)

        # Expect the filename twice because we're running a func in the same file so both the
        assert formatted_message.count(__file__) == 2

        traceback_obj = exc.__traceback__

        assert str(traceback_obj.tb_lineno) in formatted_message
        assert str(traceback_obj.tb_next.tb_lineno) in formatted_message

        # Double check that we are in fact getting the correct message in there
        assert error_text in formatted_message

    def test_puts_some_response_text_in_msg(self) -> None:
        response_text = "Server Error"

        exc: ExceptionType

        try:
            raise AttributeError("Task has no attribute 'run'")
        except AttributeError as e:
            exc = e

        formatted_message = format_failure_msg_from_exception(exc=exc, response_text=response_text)

        assert response_text in formatted_message
