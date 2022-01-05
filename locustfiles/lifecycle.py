# -*- coding: utf-8 -*-
"""
This example shows the various ways to run things before/outside the normal task execution
flow, which is very useful for fetching test data.

This was copied from https://github.com/locustio/locust/blob/master/examples/test_data_management.py
and put in this repo for ease of use and to add some missing numbers in print statements.

Copyright (c) 2009-2010, Carl Byström, Jonatan Heyman
From: https://github.com/locustio/locust/blob/master/LICENSE

1. Locustfile parse time
2. Locust start
3. Test start
4. User start
5. Inside a task
...
6. User stop
7. Test run stop
8. Locust quit

try it out by running:
    locust -f locustfiles/lifecycle.py --headless -u 1 -r 1 -t 1s
"""
import datetime

import requests
from locust import HttpUser, events, task
from locust.env import Environment
from locust.runners import MasterRunner
from locust.user.wait_time import constant


def timestring():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, "%m:%S.%f")[:-5]


print("1. Parsing locustfile, happens before anything else")

# If you want to get something over HTTP at this time you can use `requests` directly:
global_test_data = requests.post(
    "https://postman-echo.com/post",
    data="global_test_data_" + timestring(),
).json()["data"]

test_run_specific_data = None


@events.init.add_listener
def _(environment: Environment, **_kwargs):
    print("2. Initializing locust, happens after parsing the locustfile but before test start.")
    print(f"\n{environment.__dict__=}\n{_kwargs=}\n")


@events.quitting.add_listener
def _(environment: Environment, **_kwargs):
    print("8. locust is shutting down")
    print(f"\n{environment.__dict__=}\n{_kwargs=}\n")


@events.test_start.add_listener
def _(environment: Environment, **_kwargs):
    # happens only once in headless runs, but can happen multiple times in web ui-runs
    global test_run_specific_data
    print("3. Starting test run")
    print(f"\n{environment.__dict__=}\n{_kwargs=}\n")
    # in a distributed run, the master does not typically need any test data
    if not isinstance(environment.runner, MasterRunner):
        test_run_specific_data = requests.post(
            "https://postman-echo.com/post",
            data="test-run-specific_" + timestring(),
        ).json()["data"]


@events.test_stop.add_listener
def _(environment: Environment, **_kwargs):
    print("7. stopping test run")
    print(f"\n{environment.__dict__=}\n{_kwargs=}\n")


class MyUser(HttpUser):
    host = "https://postman-echo.com"
    wait_time = constant(180)  # be nice to postman-echo

    def on_start(self):
        print("4. A user was started")
        # This is a good place to fetch user-specific test data. It is executed once per User
        # If you do not want the request logged, you can replace self.client.<method> with
        # requests.<method>
        self.user_specific_testdata = self.client.post(
            "https://postman-echo.com/post",
            data="user-specific_" + timestring(),
        ).json()["data"]

    @task
    def t(self):
        self.client.get(f"/get?{global_test_data}")
        self.client.get(f"/get?{test_run_specific_data}")
        self.client.get(f"/get?{self.user_specific_testdata}")

        print("5. Getting task-run-specific testdata")
        # If every iteration is meant to use new test data this is the most common way to do it
        task_run_specific_testdata = self.client.post(
            "https://postman-echo.com/post",
            data="task_run_specific_testdata_" + timestring(),
        ).json()["data"]
        self.client.get(f"/get?{task_run_specific_testdata}")

    def on_stop(self):
        # this is a good place to clean up/release any user-specific test data
        print("6. a user was stopped")
