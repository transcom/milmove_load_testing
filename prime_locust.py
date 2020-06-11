# -*- coding: utf-8 -*-
import json
from locust import HttpUser, task, between
from utils import MilMoveUserMixin, MilMoveDomain

PRIME_CERT_KWARGS = {"certs": ("certs/devlocal-mtls.cer", "certs/devlocal-mtls.key"), "verify": False}


# class PrimeTasks(TaskSet):
#
#     @task
#     def index_page(self):
#         self.client.get("/hello")
#         self.client.get("/world")
#
#     @task(3)
#     def view_item(self):
#         item_id = random.randint(1, 10000)
#         self.client.get(f"/item?id={item_id}", name="/item")
#         self.client.post("/login", {"username": "foo", "password": "bar"})


class PrimeUser(MilMoveUserMixin, HttpUser):
    """

    """

    local_port = 9443
    domain = MilMoveDomain.PRIME
    host_path = "/prime/v1"
    is_api = True

    wait_time = between(1, 9)
    # task_set = PrimeTasks

    @task
    def fetch_mto_updates(self):
        resp = self.client.get("/move-task-orders", **PRIME_CERT_KWARGS)
        print("🏵", resp.status_code)  # todo log this?

        try:
            json_body = json.loads(resp.content)
        except json.JSONDecodeError:
            print("😥 Non-JSON response")  # todo log
        else:
            print(f"Num MTOs returned: {len(json_body)}")

    def on_start(self):
        print("🐞")
