# -*- coding: utf-8 -*-
"""
This file should contain our custom users that can then be used in locust files.
"""
from contextlib import contextmanager
from typing import Union

from locust import FastHttpUser, HttpUser

from utils.hosts import MilMoveRequestMixin
from utils.rest import RestMixin, RestResponseContextManager


class RestCertMixin(MilMoveRequestMixin, RestMixin):
    """
    Mixin that enables passing in certs whenever needed.
    """

    # Indicates if certs should be included with requests
    certs_needed: bool = False

    @contextmanager
    def rest(
        self: Union[HttpUser, FastHttpUser, MilMoveRequestMixin, RestMixin, "RestCertMixin"],
        method: str,
        url: str,
        **kwargs,
    ) -> RestResponseContextManager:
        """
        Adds cert kwargs to kwargs for request
        :param method: method for request, e.g. "GET"
        :param url: url to make request to, e.g. https://primelocal:9443/prime/v1/moves
        :param kwargs: other kwargs to pass on to `self.client.request`,
            e.g. name="prime/v1/mto-service-items/{mtoServiceItemID}"
        :return: a context manager that can be used ot examine the response data or to mark the
            test as a success or failure.
        """
        if self.certs_needed:
            for k, v in self.cert_kwargs.items():
                kwargs.setdefault(k, v)

        with super().rest(method, url, **kwargs) as resp:
            resp: RestResponseContextManager
            yield resp


class RestHttpUser(RestCertMixin, HttpUser):
    """
    A convenience class for testing REST JSON endpoints.
    """

    abstract = True
