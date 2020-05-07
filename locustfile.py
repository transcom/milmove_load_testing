# -*- coding: utf-8 -*-
from locust import HttpLocust, between

# from apps.internal import AnonBehavior
from apps.internal import ServiceMemberUserBehavior
# from apps.internal import OfficeUserBehavior

from apps.prime import PrimeClientBehavior

# class AnonUser(HttpLocust):
#     host = "http://milmovelocal:8080"
#     # host = "https://my.experimental.move.mil"
#     # weight = 5  # 5x more likely than other users
#     weight = 1
#     task_set = AnonBehavior
#     wait_time = between(2, 5)


class ServiceMemberUser(HttpLocust):
    host = "http://milmovelocal:8080"
    # host = "https://my.experimental.move.mil"
    weight = 1
    task_set = ServiceMemberUserBehavior
    wait_time = between(2, 5)


# class OfficeUser(HttpLocust):
#     host = "http://officelocal:8080"
#     # host = "https://office.experimental.move.mil"
#     weight = 1
#     task_set = OfficeUserBehavior
#     wait_time = between(2, 5)

# class PrimeClient(HttpLocust):
#     # host = "https://primelocal:9443"
#     # host = "https://primelocal:9443"
#     host = "https://api.experimental.move.mil"
#     weight = 1
#     task_set = PrimeClientBehavior
#     wait_time = between(1,2)
