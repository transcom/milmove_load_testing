# -*- coding: utf-8 -*-
""" tasks/base.py is for code used internally within the tasks package. """

import json
import logging
from typing import Union

from requests import Response

from utils.rest import RestResponseContextManager


logger = logging.getLogger(__name__)


def check_response(
    response: Union[Response, RestResponseContextManager],
    task_name="Task",
    request=None,
    expected_status_code: str = "2",
):
    """
    Logs the status code from the response and converts it from JSON into a python dictionary we can work with. If the
    status code doesn't match (by default 2xx), it can also log any request data that was sent in for the sake of debugging.
    Returns the dictionary representation of the response content and a boolean indicating success or failure.

    :param response: HTTP Response class from the Python requests framework
    :param task_name: str, optional name of the tasks
    :param request: any type, optional data to print for debugging a failed response
    :param expected_status_code: str, expected code of response if no value is provided expects 2xx
    :return: tuple(dict, bool)
    """
    logger.info(f"ℹ️ {task_name} status code: {response.status_code} {response.reason}")

    # TODO: Temporary hacky workaround while I think about how check_response should work with the new changes
    if not hasattr(response, "js"):
        try:
            json_response = json.loads(response.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response.")
            return None, False
    else:
        json_response = response.js

    if not str(response.status_code).startswith(expected_status_code):
        logger.error(f"⚠️ {task_name} failed.\n{json.dumps(json_response, indent=4)}")
        if request:
            try:
                logger.error(
                    f"Request data:\n{response.request.method} {response.request.url}\n{json.dumps(request, indent=4)}"
                )
            except (json.JSONDecodeError, TypeError):
                logger.error(f"Request data:\n{response.request.method} {response.request.url}\n{request}")

        return json_response, False

    return json_response, True
