# -*- coding: utf-8 -*-
"""
This file should contain our custom TaskSets that can then be used in our tasks files.
"""
from locust import TaskSet

from utils.request import MilMoveRequestMixin
from utils.rest import RestMixin


class RestTaskSet(MilMoveRequestMixin, RestMixin, TaskSet):
    """
    A convenience class for testing REST JSON endpoints.
    """
