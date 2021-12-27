# -*- coding: utf-8 -*-
"""
This file should contain our custom users that can then be used in locust files.
"""

from locust import HttpUser

from utils.rest import (
    RestMixin,
)


class RestHttpUser(RestMixin, HttpUser):
    """
    A convenience class for testing REST JSON endpoints.
    """

    abstract = True
