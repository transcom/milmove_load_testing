# -*- coding: utf-8 -*-
""" Locust test for the MilMove Office interface. """
from locust import HttpUser, between

from tasks import ServicesCounselorTasks, TOOTasks


class ServicesCounselorUser(HttpUser):
    """
    Tests the MilMove Office app with the Services Counselor role.
    """

    tasks = {ServicesCounselorTasks: 1}
    wait_time = between(0.25, 9)


class TOOUser(HttpUser):
    """
    Tests the MilMove Office app with the TOO role.
    """

    tasks = {TOOTasks: 1}
    wait_time = between(0.25, 9)
