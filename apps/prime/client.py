# -*- coding: utf-8 -*-
from locust import TaskSet
from locust import seq_task

from .base import BaseTaskSequence


class PrimeEndpoints(BaseTaskSequence):
    def move_task_orders(self):
        # local_cert = (
        #     "./config/tls/devlocal-mtls.cer",
        #     "./config/tls/devlocal-mtls.key",
        # )
        my_cert = (
            "./tmp/piv.cer",
            "./tmp/piv.key",
        )
        cert = "./tmp/piv.pem"
        url = "https://api.experimental.move.mil/prime/v1/move-task-orders"
        # self.client.get(url, verify=cert, cert=cert)
        self.client.get(url, verify=cert)

    @seq_task(1)
    def fetch_move_task_orders(self):
        self.move_task_orders()


class PrimeClientBehavior(TaskSet):
    tasks = {PrimeEndpoints: 1}
