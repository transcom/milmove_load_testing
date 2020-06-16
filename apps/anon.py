# -*- coding: utf-8 -*-
from locust import TaskSet, task


class AnonBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")
