# -*- coding: utf-8 -*-
from json import JSONDecodeError
from typing import Any, Dict, Tuple

from locust.clients import ResponseContextManager

from utils.types import ExceptionType, JSONType


def get_json_headers() -> dict[str, str]:
    """
    Returns default headers needed for JSON requests that expect to send and receive json.
    :return: dict of headers to include with json requests
    """
    return {"Content-Type": "application/json", "Accept": "application/json"}


class RestResponseContextManager(ResponseContextManager):
    """
    Add a js and error attributes to ResponseContextManager to support the functionality in
    RestHttpUser.

    In particular this makes it so that type checking is happier rather than the original way it was
    done in the plugin which just added the attribute to the context manager instance rather than
    the class.
    """

    error: ExceptionType = None
    js: JSONType = None
    request_meta: Dict[str, Any] = None


def parse_response_json(response: RestResponseContextManager) -> Tuple[JSONType, str]:
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
