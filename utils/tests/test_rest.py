# -*- coding: utf-8 -*-
"""
Tests for utils/rest.py
"""
import json
from json import JSONDecodeError
from typing import NoReturn, Optional
from unittest.mock import MagicMock, create_autospec, patch

import pytest
from requests import Response

from utils.rest import (
    RestMixin,
    RestResponseContextManager,
    format_failure_msg_from_exception,
    get_json_headers,
    parse_response_json,
)
from utils.types import ExceptionType


class TestGetJSONHeaders:
    """
    Tests for get_json_headers
    """

    def test_returns_expected_headers(self) -> None:
        assert {"Content-Type": "application/json", "Accept": "application/json"} == get_json_headers()


def get_mock_response(basic_response: bool = False) -> MagicMock:
    """
    Creates a RestMixin with a mocked out client attr to mimic if we'd actually used the mixin
    with a User or TaskSet class.

    :param basic_response: whether to make a basic response
    :return: mock response
    """
    if basic_response:
        return create_autospec(Response)
    else:
        return create_autospec(RestResponseContextManager)


class TestParseResponseToJSON:
    """
    Tests for parse_response_json
    """

    def test_returns_proper_error_message_for_rest_response_if_response_text_is_none(self):
        mock_response = get_mock_response()

        mock_response.text = None

        response_time = 10.35153  # In seconds
        mock_response.request_meta.__getitem__.return_value = response_time * 1000  # Needs to be
        # in ms

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

    def test_returns_proper_error_message_for_base_response_if_response_text_is_none(self):
        mock_response = get_mock_response(basic_response=True)

        mock_response.text = None

        response_error = "Server Error"
        mock_response.error = response_error

        response_status_code = 500
        mock_response.status_code = response_status_code

        parsed_json, error_message = parse_response_json(mock_response)

        assert not parsed_json

        assert response_error in error_message
        assert str(response_status_code) in error_message

    @pytest.mark.parametrize("mock_response", (get_mock_response(), get_mock_response(basic_response=True)))
    def test_returns_empty_dict_and_err_msg_if_no_error_and_no_text(self, mock_response: MagicMock):
        mock_response.text = ""

        parsed_json, error_message = parse_response_json(mock_response)

        assert not parsed_json
        assert not error_message

    @pytest.mark.parametrize("mock_response", (get_mock_response(), get_mock_response(basic_response=True)))
    def test_returns_proper_error_message_if_response_text_is_not_json(self, mock_response: MagicMock):
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


@pytest.fixture()
def rest_parent() -> RestMixin:
    """
    Creates a RestMixin with a mocked out client attr to mimic if we'd actually used the mixin
    with a User or TaskSet class.

    :return: initialized mixin
    """
    parent = RestMixin()

    # We only really need to mock out client to be on our way.
    parent.client = MagicMock()

    yield parent

    parent.client.reset_mock()


class TestRestMixin:
    """
    Tests for RestMixin
    """

    def test_inserts_expected_kwargs_into_request(self, rest_parent: RestMixin) -> None:
        # In particular, expecting the catch_response=True, and the JSON headers.

        request_method = "GET"
        fake_url = "https://localhost:8080"

        expected_headers = get_json_headers()

        with rest_parent.rest(method=request_method, url=fake_url):
            rest_parent.client.request.assert_called_once_with(
                request_method, fake_url, catch_response=True, headers=expected_headers
            )

    def test_will_not_override_custom_headers(self, rest_parent: RestMixin) -> None:
        request_method = "GET"
        fake_url = "https://localhost:8080"

        expected_headers = {"Content-Type": "multipart/form-data"}

        with rest_parent.rest(method=request_method, url=fake_url, headers=expected_headers):
            rest_parent.client.request.assert_called_once_with(
                request_method, fake_url, catch_response=True, headers=expected_headers
            )

    @patch("utils.rest.parse_response_json", autospec=True)
    def test_parses_response_json(self, mock_parse_response_json: MagicMock, rest_parent: RestMixin) -> None:
        mock_parse_response_json.return_value = ({}, "")

        with rest_parent.rest(method="GET", url="https://localhost:8080") as resp:
            resp: MagicMock

            mock_parse_response_json.assert_called_once_with(response=resp)

            assert resp.js == mock_parse_response_json.return_value

    @patch("utils.rest.parse_response_json", autospec=True)
    def test_if_there_is_an_error_parsing_response_json_then_marks_response_as_failure(
        self, mock_parse_response_json: MagicMock, rest_parent: RestMixin
    ) -> None:
        error_msg = "Invalid JSON!"

        mock_parse_response_json.return_value = ({}, error_msg)

        with rest_parent.rest(method="GET", url="https://localhost:8080") as resp:
            resp: MagicMock

            mock_parse_response_json.assert_called_once_with(response=resp)

            assert resp.js is None
            resp.failure.assert_called_once_with(error_msg)

    @patch("utils.rest.parse_response_json", autospec=True)
    @patch("utils.rest.format_failure_msg_from_exception", autospec=True)
    def test_if_exception_is_raised_in_context_manager_then_response_is_failed(
        self, mock_failure_format_func: MagicMock, mock_parse_response_json: MagicMock, rest_parent: RestMixin
    ) -> None:
        exception = Exception("Something broke!")

        mock_parse_response_json.return_value = ({}, "")

        mock_resp: MagicMock

        with rest_parent.rest(method="GET", url="https://localhost:8080") as resp:
            resp: MagicMock

            # This is an easy way to access this mock later. Otherwise, we would have to dig in to
            # the call stack, e.g. rest_parent.client.request.return_value (and a few more levels).
            mock_resp = resp

            raise exception

        mock_failure_format_func.assert_called_once_with(exc=exception, response_text=mock_resp.text)
        mock_resp.failure.assert_called_once_with(mock_failure_format_func.return_value)
