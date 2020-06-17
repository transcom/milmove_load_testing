# -*- coding: utf-8 -*-
from locust import HttpUser, between

from tasks import AnonBehavior
from tasks.fixme import OfficeQueue, ServiceMemberSignupFlow


class AnonUser(HttpUser):
    host = "http://milmovelocal:8080"
    # host = "https://my.experimental.move.mil"
    tasks = {AnonBehavior: 1}
    wait_time = between(2, 9)


class ServiceMemberUser(HttpUser):
    host = "http://milmovelocal:8080"
    # host = "https://my.experimental.move.mil"
    tasks = {ServiceMemberSignupFlow: 1}
    wait_time = between(2, 9)


class OfficeUser(HttpUser):
    host = "http://officelocal:8080"
    # host = "https://office.experimental.move.mil"
    tasks = {OfficeQueue: 1}
    wait_time = between(2, 9)
