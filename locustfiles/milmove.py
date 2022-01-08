# -*- coding: utf-8 -*-
""" Locust test for the MilMove Customer Signup interface. """
from locust import HttpUser, between

from tasks import MilMoveTasks


class MilMoveUser(HttpUser):
    """
    Tests the MilMove app.
    """

    tasks = {MilMoveTasks: 1}
    wait_time = between(1, 9)
