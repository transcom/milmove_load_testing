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
