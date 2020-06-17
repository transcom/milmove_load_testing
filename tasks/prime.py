# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging

from locust import tag

from .base import CertTaskSet

logger = logging.getLogger(__name__)


def prime_path(url):
    return f"/prime/v1{url}"


def support_path(url):
    return f"/support/v1{url}"


@tag("prime")
class PrimeTasks(CertTaskSet):
    """
    Set of the tasks that can be called on the Prime API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier. Ex:

    @tag('fetch', 'mtos')
    @task
    def fetch_mtos(self):
        self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
    """


@tag("support")
class SupportTasks(CertTaskSet):
    """
    Set of the tasks that can be called on the Support API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier. Ex:

    @tag('status_updates', 'shipments')
    @task
    def update_mto_shipment_status(self):
        # etc.
    """
