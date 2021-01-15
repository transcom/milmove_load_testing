# -*- coding: utf-8 -*-
""" tasks/base.py is for code used internally within the tasks package. """
from utils.base import ImplementationError

import json
from locust import TaskSet
import logging
from requests import Response


logger = logging.getLogger(__name__)


def check_response(response: Response, task_name="Task", request=None):
    """
    Logs the status code from the response and converts it from JSON into a python dictionary we can work with. If the
    status code wasn't a success (2xx), it can also log any request data that was sent in for the sake of debugging.
    Returns the dictionary representation of the response content and a boolean indicating success or failure.

    :param response: HTTP Response class from the Python requests framework
    :param task_name: str, optional name of the tasks
    :param request: any type, optional data to print for debugging a failed response
    :return: tuple(dict, bool)
    """
    logger.info(f"ℹ️ {task_name} status code: {response.status_code}")

    try:
        json_response = json.loads(response.content)
    except (json.JSONDecodeError, TypeError):
        logger.exception("Non-JSON response.")
        return None, False

    if not str(response.status_code).startswith("2"):
        logger.error(f"⚠️ {task_name} failed.\n{json.dumps(json_response, indent=4)}")
        if request:
            try:
                logger.error(
                    f"Request data:\n{response.request.method} {response.request.url}\n{json.dumps(request, indent=4)}"
                )
            except (json.JSONDecodeError, TypeError):
                logger.error(f"Request data:\n{response.request.method} {response.request.url}\n{request}")

        return json_response, False

    logger.info(f"ℹ️ {task_name} successfully completed!")

    return json_response, True


class CertTaskMixin:
    """
    TaskSet mixin class that uses a cert_kwargs dictionary set in the User class calling the tasks. Set up for local
    mTLS in particular. Client calls in this TaskSet should look like:

    `self.client.get('url', **self.user.cert_kwargs)`

    NOTE: MUST BE PLACED BEFORE TaskSet IN MRO INHERITANCE
    """

    def __init__(self, parent):
        super().__init__(parent)  # sets self._user to the right User class

        # Check that the User class calling these tasks implements cert_kwargs:
        if not hasattr(self.user, "cert_kwargs"):
            setattr(self.user, "cert_kwargs", {})  # set an empty dict to avoid attribute errors later on


class ParserTaskMixin:
    """
    TaskSet mixin class that needs an APIParser class to be connected to the User calling the tasks. MUST have a parser
    defined.

    NOTE: MUST BE PLACED BEFORE TaskSet IN MRO INHERITANCE
    """

    def __init__(self, parent):
        super().__init__(parent)

        # MUST have parser defined, not an option attribute
        if not hasattr(self.user, "parser"):
            raise ImplementationError("The user for a TaskSet using ParserTaskSet mixin must have a parser attribute.")

    def fake_request(self, path, method, overrides=None, require_all=False):
        """
        Wraps the parser's generate_fake_request method for ease of use.
        """
        return self.user.parser.generate_fake_request(path, method, overrides, require_all)


class LoginTaskSet(TaskSet):
    """
    TaskSet that grabs the CSRF and session tokens for the user and creates a fake logon for making requests.
    """

    def __init__(self, parent):
        self.csrf_token = None
        self.session_token = None

        super().__init__(parent)

    def _set_csrf_token(self):
        """
        Pull the CSRF token from the website by hitting the root URL.
        This token is set as a cookie with the name `masked_gorilla_csrf`.
        """
        self.client.get("/")
        self.csrf_token = self.client.cookies.get("masked_gorilla_csrf")

    def _create_login(self, user_type, session_token_name):
        """
        Creates a login for the given user type and grabs the session cookie for later use.
        :param user_type: str
        :param session_token_name: str
        :return: response
        """
        resp = self.client.post("/devlocal-auth/create", data={"userType": user_type})
        self.session_token = self.client.cookies.get(session_token_name)

        return resp

    def _logout(self):
        """
        Logs the current user out of the session. Can be followed by an interrupt or by logging in again.
        """
        self.client.post("/auth/logout")
        self.session_token = None

    def on_start(self):
        """
        Grab the CSRF token from the base url and update the headers with that value before any tasks execute.
        """
        self._set_csrf_token()
        self.client.headers.update({"x-csrf-token": self.csrf_token})
