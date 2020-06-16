# -*- coding: utf-8 -*-
from locust import HttpUser, between

from apps import AnonBehavior
from apps import ServiceMemberUserBehavior
from apps import OfficeUserBehavior


class AnonUser(HttpUser):
    host = "http://milmovelocal:8080"
    # host = "https://my.experimental.move.mil"
    # weight = 5  # 5x more likely than other users
    weight = 1
    task_set = AnonBehavior
    wait_time = between(5, 9)


class ServiceMemberUser(HttpUser):
    host = "http://milmovelocal:8080"
    # host = "https://my.experimental.move.mil"
    weight = 1
    task_set = ServiceMemberUserBehavior
    wait_time = between(5, 9)


class OfficeUser(HttpUser):
    host = "http://officelocal:8080"
    # host = "https://office.experimental.move.mil"
    weight = 1
    task_set = OfficeUserBehavior
    wait_time = between(5, 9)
