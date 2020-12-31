# -*- coding: utf-8 -*-
from tasks.base import check_response
from requests import Response

# import logging


# def test_check_response_logged():


def test_check_response_happy_path():
    response = Response()
    response.status_code = 200
    response._content = '{"field": "value"}'

    # Happy Path:
    assert check_response(response) == ({"field": "value"}, True)


# Unhappy Paths:
def test_check_response_non_json():
    non_json_response = Response()
    non_json_response.status_code = 500
    non_json_response._content = "non-json"

    assert check_response(non_json_response) == (None, False)


def test_check_response_bad_status_code():
    bad_status_code = Response()
    bad_status_code.status_code = 400
    bad_status_code._content = '{"this_is": "ok"}'

    assert check_response(bad_status_code) == ({"this_is": "ok"}, False)
