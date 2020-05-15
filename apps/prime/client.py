# -*- coding: utf-8 -*-
from locust import TaskSet
from locust import seq_task

from ..common.base import BaseTaskSequence


class PrimeEndpoints(BaseTaskSequence):
    def move_task_orders(self):
        local_cert = (
            "./config/tls/devlocal-mtls.cer",
            "./config/tls/devlocal-mtls.key",
        )
        url = "https://primelocal:9443/prime/v1/move-task-orders"
        self.client.get(url, verify=False, cert=local_cert)

    @seq_task(1)
    def fetch_move_task_orders(self):
        self.move_task_orders()


class PrimeClientBehavior(TaskSet):
    tasks = {PrimeEndpoints: 1}
