# -*- coding: utf-8 -*-
""" tasks/base.py is for code used internally within the tasks package. """
from locust import TaskSet


class CertTaskSet(TaskSet):
    """
    TaskSet that uses a cert_kwargs dictionary set in the User class calling the tasks. Set up for local mTLS in
    particular. Client calls in this TaskSet should look like:

    `self.client.get('url', **self.user.cert_kwargs)`
    """

    def __init__(self, parent):
        super().__init__(parent)  # sets self._user to the right User class

        # Check that the User class calling these tasks implements cert_kwargs:
        if not hasattr(self.user, "cert_kwargs"):
            setattr(self.user, "cert_kwargs", {})  # set an empty dict to avoid attribute errors later on


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
