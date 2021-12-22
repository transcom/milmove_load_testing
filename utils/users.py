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
from json.decoder import JSONDecodeError
from typing import Any, Dict, Tuple

from locust import HttpUser
from locust.clients import ResponseContextManager

from utils.constants import E, get_json_headers


def format_failure_msg_from_exception(exc: E, response_text: str = "") -> str:
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


class RestResponseContextManager(ResponseContextManager):
    """
    Add a js and error attributes to ResponseContextManager to support the functionality in
    RestHttpUser.

    In particular this makes it so that type checking is happier rather than the original way it was
    done in the plugin which just added the attribute to the context manager instance rather than
    the class.
    """

    error: E = None
    js: Dict[str, Any] = None
    request_meta: Dict[str, Any] = None


def parse_response_json(response: RestResponseContextManager) -> Tuple[Dict[str, Any], str]:
    """
    Takes a response object and tries to parse its text content into a dictionary. Returns a tuple
    with the first item being the parsed response text as a dictionary (defaults to an empty dict)
    and the second being an error message, if any (defaults to an empty string).

    :param response: response object, like the one you get with a line like this:
        with self.client.request(method, url, **kwargs) as response:
    :return: Tuple, first item is a dict containing parsed response text, second contains an error
        message.
    """
    data = {}
    error_message = ""

    if response.text is None:
        # round the response time to the nearest second to improve error grouping. request_meta
        # contains the time in milliseconds, so we need to convert to seconds, and then round.
        response_time = round(response.request_meta["response_time"] / 1000, 1)

        error_message = (
            f"response body None, error {response.error}, response code {response.status_code}, "
            f"response time ~{response_time}s."
        )

        return data, error_message

    # Might just have an empty body.
    if not response.text:
        return data, error_message

    try:
        data = response.json()
    except JSONDecodeError as e:
        error_message = (
            f"Could not parse response as JSON. {response.text[:250]}, response code "
            f"{response.status_code}, error {e}"
        )

    return data, error_message


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
