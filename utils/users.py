# -*- coding: utf-8 -*-
"""
The code in this file is based on `RestUser` from `locust-plugins`:
https://github.com/SvenskaSpel/locust-plugins/blob/master/locust_plugins/users/rest.py

but instead of extending FastHttpUser, it extends HttpUser because we need to be able to provide
certs when we run against a deployed environment.
"""
from contextlib import contextmanager

from locust import HttpUser

from utils.rest import (
    RestResponseContextManager,
    format_failure_msg_from_exception,
    get_json_headers,
    parse_response_json,
)


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
