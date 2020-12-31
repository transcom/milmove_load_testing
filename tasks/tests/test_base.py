# -*- coding: utf-8 -*-
""" This file tests the classes and functions in tasks/base.py """
import logging
from requests import Response
from tasks.base import check_response

# tasks.base logger for mocking
logger = logging.getLogger("tasks.base")


def test_check_response_happy_path():
    """
    This tests checks that a response content and True bool are returned as expected when there is valid JSON and 2xx status code
    """
    response = Response()
    response.status_code = 200
    response._content = '{"field": "value"}'

    # Happy Path:
    assert check_response(response) == ({"field": "value"}, True)


# Unhappy Paths:


def test_check_response_non_json(mocker):
    """
    This tests checks that a response content is NONE and a False bool are returned when there is no JSON and a non-2xx status code.
    This test will mock an exception and then test that that exception is logged.
    """
    non_json_response = Response()
    non_json_response.status_code = 500
    non_json_response._content = "non-json"

    mocker.patch.object(logger, "exception")
    assert check_response(non_json_response) == (None, False)
    logger.exception.assert_called_once_with("Non-JSON response.")


def test_check_response_bad_status_code(mocker):
    """
    This tests checks that a response content is JSON and a False bool are returned when there is valid JSON but a non-2xx status code
    This test will mock an error, check that the error is logged, and test how many times the error is logged.
    """
    bad_status_code = Response()
    bad_status_code.status_code = 400
    bad_status_code._content = '{"this_is": "ok"}'

    mocker.patch.object(logger, "error")
    assert check_response(bad_status_code, "Task", '{ "a":1 }') == ({"this_is": "ok"}, False)
    assert logger.error.call_count == 2
    expected_calls = [
        mocker.call('⚠️\n{\n    "this_is": "ok"\n}'),
        mocker.call('Request data:\n"{ \\"a\\":1 }"'),
    ]
    assert logger.error.call_args_list == expected_calls
