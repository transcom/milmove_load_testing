# -*- coding: utf-8 -*-
from locust import TaskSet, task


class AnonBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")
