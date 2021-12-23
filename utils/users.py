# -*- coding: utf-8 -*-
"""
The code in this file is based on `RestUser` from `locust-plugins`:
https://github.com/SvenskaSpel/locust-plugins/blob/master/locust_plugins/users/rest.py

but instead of extending FastHttpUser, it extends HttpUser because we need to be able to provide
certs when we run against a deployed environment.
"""
import re
import traceback
from contextlib import contextmanager

from locust import HttpUser

from utils.rest import RestResponseContextManager, get_json_headers, parse_response_json
from utils.types import ExceptionType


def format_failure_msg_from_exception(exc: ExceptionType, response_text: str = "") -> str:
    """
    Takes a traceback as a string and formats it into a shorter error message. This is useful for
    creating a message that can be used to report a task failure.
    :param exc: Raised exception
    :param response_text: Text from response, e.g. resp.text
    :return: formatted error message
    """
    # Map a few things to be easier to use later
    exception_type = type(exc)
    traceback_obj = exc.__traceback__

    traceback_list = traceback.format_exception(etype=exception_type, value=exc, tb=traceback_obj)

    # We want a shorter message than the full traceback, so we'll just collect some useful tidbits
    # We'll grab file name, line number, and func name for each stack.
    callstack_regex = re.compile(r' {2}File "(?P<file_name>/.[^"]*)", line (?P<line_number>\d*),(?P<func_reference>.*)')

    error_lines = []

    for line in traceback_list:
        if matches := callstack_regex.match(line):
            file_name = matches.group("file_name")
            line_number = matches.group("line_number")
            func_reference = matches.group("func_reference")

            error_lines.append(f"{file_name}:{line_number}{func_reference}")

    # Our base failure message will just be exception info
    failure_msg = f"{exception_type.__name__}: {exc}"

    # If we got traceback info we can add that to the failure message.
    if error_lines:
        error_msg = ", ".join(error_lines)

        failure_msg += f" at {error_msg}."

    # finally, we'll add some response_text, but we'll cap it to not make the final message too big
    # due to this bit.
    short_resp = response_text[:200] if response_text else response_text

    failure_msg += f" Response was {short_resp}"

    return failure_msg


class RestHttpUser(HttpUser):
    """
    A convenience class for testing REST JSON endpoints.
    """

    abstract = True

    @contextmanager
    def rest(self, method: str, url: str, **kwargs) -> RestResponseContextManager:
        """
        This is a wrapper around self.client.request() that:

            * automatically passes catch_response=True
            * automatically sets content-type and accept headers to application/json (unless you
                provide your own headers)
            * automatically checks that the response is valid json, parses it into a dict and saves
                it in a field called `js` in the response object
            * catches any exceptions thrown in your with-block and fails the sample
        :param method: method for request, e.g. "GET"
        :param url: url to make request to, e.g. /prime/v1/moves
        :param kwargs: other kwargs to pass on to `self.client.request`,
            e.g. name="prime/v1/mto-service-items/{mtoServiceItemID}"
        :return: a context manager that can be used ot examine the response data or to mark the
            test as a success or failure.
        """
        default_headers = get_json_headers()
        headers = kwargs.pop("headers", default_headers)

        with self.client.request(method, url, catch_response=True, headers=headers, **kwargs) as resp:
            resp: RestResponseContextManager

            parsed_json, error_msg = parse_response_json(response=resp)

            if error_msg:
                resp.failure(error_msg)

            resp.js = parsed_json

            try:
                yield resp
            except Exception as e:
                failure_msg = format_failure_msg_from_exception(exc=e, response_text=resp.text)

                resp.failure(failure_msg)
