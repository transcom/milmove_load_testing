# -*- coding: utf-8 -*-
""" This file tests the classes and functions in tasks/base.py """

from requests import Response
from tasks.base import check_response


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
def test_check_response_non_json():
    """
    This tests checks that a response content is NONE and a False bool are returned when there is no JSON and a non-2xx status code
    """
    non_json_response = Response()
    non_json_response.status_code = 500
    non_json_response._content = "non-json"

    assert check_response(non_json_response) == (None, False)


def test_check_response_bad_status_code():
    """
    This tests checks that a response content is JSON and a False bool are returned when there is valid JSON but a non-2xx status code
    """
    bad_status_code = Response()
    bad_status_code.status_code = 400
    bad_status_code._content = '{"this_is": "ok"}'

    assert check_response(bad_status_code) == ({"this_is": "ok"}, False)
