# import locust first because it monkeypatches ssl
from locust.user.users import User
from locust.clients import LocustResponse

from abc import abstractmethod, ABC
from urllib.parse import urlparse

import urllib3
import urllib3.exceptions
import urllib3.response
import ssl

from requests import Request, Response
import requests.exceptions

import time
from typing import Optional

from utils.request import MilMoveRequestPreparer

import internal_client
import ghc_client
import prime_client

from http import HTTPStatus
import requests
import requests.cookies

from utils.auth import create_user, SessionCaller, SessionTracker, UserType
from utils.base import MilMoveEnv


class SetResourcePathMixin(object):
    def set_resource_path(self, *args, **kwargs):
        # if this pool manager has a resource_path attribute, it must
        # be our custom version used for locust stats
        if hasattr(self.rest_client.pool_manager, "resource_path"):
            # calculate resource path with any prefix from host config
            base_resource_path = args[0]
            resource_path = self.configuration.host + base_resource_path
            if "_host" in kwargs:
                resource_path = kwargs.get("_host") + base_resource_path
            u = urlparse(resource_path)
            self.rest_client.pool_manager.resource_path = u.path


class LocustInternalApiClient(internal_client.ApiClient, SetResourcePathMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def call_api(self, *args, **kwargs):
        self.set_resource_path(*args, **kwargs)
        return super().call_api(*args, **kwargs)


class LocustGHCApiClient(ghc_client.ApiClient, SetResourcePathMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def call_api(self, *args, **kwargs):
        self.set_resource_path(*args, **kwargs)
        return super().call_api(*args, **kwargs)


class LocustPrimeApiClient(prime_client.ApiClient, SetResourcePathMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def call_api(self, *args, **kwargs):
        self.set_resource_path(*args, **kwargs)
        return super().call_api(*args, **kwargs)


class PoolManager(ABC):
    @abstractmethod
    def request(self, method, url, **kwargs):
        raise NotImplementedError


class LocustOpenAPIPoolManager(PoolManager):
    """Reimplements the locust tracking from HttpSession for openapi"""

    resource_path: Optional[str]
    user: Optional[User]
    request_preparer: MilMoveRequestPreparer
    pool_manager: urllib3.PoolManager

    def __init__(self, user: Optional[User], pool_manager: urllib3.PoolManager):
        self.user = user
        self.pool_manager = pool_manager
        self.resource_path = None

    def request(self, method, url, **kwargs):
        context = {}
        if self.user:
            context = {**self.user.context(), **context}
        start_time = time.time()
        start_perf_counter = time.perf_counter()
        fake_response = LocustResponse()
        fake_response.request = Request(method, url).prepare()
        response = None
        parsed_url = urlparse(url)
        name = self.resource_path or parsed_url.path
        try:
            response = self.pool_manager.request(method, url, **kwargs)
            # raise for status needs reason and status_code
            fake_response.status_code = response.status
            fake_response.reason = response.reason
        except urllib3.exceptions.HTTPError as e:
            fake_response.error = e
            fake_response.status_code = 0  # with this status_code, content returns None

        response_time = (time.perf_counter() - start_perf_counter) * 1000
        # reset after request
        self.resource_path = None

        request_meta = {
            "request_type": method,
            "response_time": response_time,
            "name": name,
            "context": context,
            "response": fake_response,
            "exception": None,
            "start_time": start_time,
            "url": url,
        }

        if response:
            request_meta["response_length"] = len(response.data or b"")

        try:
            Response.raise_for_status(fake_response)
        except requests.exceptions.RequestException as e:
            while (
                isinstance(
                    e,
                    (
                        requests.exceptions.ConnectionError,
                        urllib3.exceptions.ProtocolError,
                        urllib3.exceptions.MaxRetryError,
                        urllib3.exceptions.NewConnectionError,
                    ),
                )
                and e.__context__  # Not sure if the above exceptions can ever be the lowest level, but it is good to be sure
            ):
                e = e.__context__
            request_meta["exception"] = e

        if self.user:
            request_event = self.user.environment.events.request
            request_event.fire(**request_meta)

        return response


class FlowSessionManager(object):
    request_preparer: MilMoveRequestPreparer
    user: Optional[User]
    session_tracker: SessionTracker

    def __init__(self, milmove_env: MilMoveEnv, user: Optional[User]) -> None:
        self.request_preparer = MilMoveRequestPreparer(env=milmove_env)
        self.user = user

        def locust_session_tracker(method: str, url: str, session_caller: SessionCaller) -> bool:
            start_time = time.time()
            start_perf_counter = time.perf_counter()
            resp = session_caller()
            response_time = (time.perf_counter() - start_perf_counter) * 1000

            if not user:
                return resp.status_code == HTTPStatus.OK

            context = {}
            if user:
                context = {**user.context(), **context}
            request_meta = {
                "request_type": method,
                "name": url,
                "start_time": start_time,
                "response": resp,
                "response_time": response_time,
                "response_length": len(resp.content or b""),
                "context": context,
                "exception": None,
            }

            try:
                resp.raise_for_status()
            except requests.exceptions.RequestException as e:
                while (
                    isinstance(
                        e,
                        (
                            requests.exceptions.ConnectionError,
                            urllib3.exceptions.ProtocolError,
                            urllib3.exceptions.MaxRetryError,
                            urllib3.exceptions.NewConnectionError,
                        ),
                    )
                    and e.__context__  # Not sure if the above exceptions can ever be the lowest level, but it is good to be sure
                ):
                    e = e.__context__
                request_meta["exception"] = e

            user.environment.events.request.fire(**request_meta)

            if request_meta["exception"]:
                return False
            return True

        self.session_tracker = locust_session_tracker

    def internal_api_client(self, user_type: UserType) -> LocustInternalApiClient:
        session = requests.Session()
        if not create_user(self.session_tracker, self.request_preparer, session, user_type):
            raise Exception(f"Cannot create user: {user_type}")

        host = self.request_preparer.form_internal_path("")
        req = requests.Request("GET", host)
        cookie = requests.cookies.get_cookie_header(session.cookies, req)
        configuration = internal_client.Configuration(host=host)
        api_client = LocustInternalApiClient(configuration, cookie=cookie)
        for k, v in session.headers.items():
            api_client.set_default_header(k, v)
        api_client.rest_client.pool_manager = self.new_pool_manager()
        return api_client

    def ghc_api_client(self, user_type: UserType) -> LocustGHCApiClient:
        session = requests.Session()
        if not create_user(self.session_tracker, self.request_preparer, session, user_type):
            raise Exception(f"Cannot create user: {user_type}")

        host = self.request_preparer.form_ghc_path("")
        req = requests.Request("GET", host)
        cookie = requests.cookies.get_cookie_header(session.cookies, req)
        configuration = internal_client.Configuration(host=host)
        api_client = LocustGHCApiClient(configuration, cookie=cookie)
        for k, v in session.headers.items():
            api_client.set_default_header(k, v)
        api_client.rest_client.pool_manager = self.new_pool_manager()
        return api_client

    def prime_api_client(self) -> LocustPrimeApiClient:
        session = requests.Session()

        host = self.request_preparer.form_prime_path("")
        req = requests.Request("GET", host)
        cookie = requests.cookies.get_cookie_header(session.cookies, req)
        configuration = internal_client.Configuration(host=host)
        api_client = LocustPrimeApiClient(configuration, cookie=cookie)
        api_client.rest_client.pool_manager = self.new_pool_manager(certs_required=True)

        return api_client

    def new_pool_manager(self, certs_required=False) -> PoolManager:
        rkwargs = self.request_preparer.get_request_kwargs(certs_required=certs_required)
        cert_reqs = ssl.CERT_REQUIRED
        cert_file = None
        key_file = None
        ssl_ca_cert = None
        if "verify" in rkwargs and not rkwargs["verify"]:
            cert_reqs = ssl.CERT_NONE
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if "cert" in rkwargs:
            if isinstance(rkwargs["cert"], str):
                cert_file = rkwargs["cert"]
            elif isinstance(rkwargs["cert"], tuple):
                cert_file = rkwargs["cert"][0]
                key_file = rkwargs["cert"][1]

        num_users = 10
        if self.user:
            num_users = self.user.environment.parsed_options.num_users

        # as a rough approximation, use a pool size that is 1/3 of the
        # number of users, as we have service members, office users,
        # and the prime, but make sure we have at least 4
        pools_size = max(4, int(num_users / 3))
        maxsize = pools_size
        pool_manager = urllib3.PoolManager(
            num_pools=pools_size,
            maxsize=maxsize,
            cert_reqs=cert_reqs,
            ca_certs=ssl_ca_cert,
            cert_file=cert_file,
            key_file=key_file,
        )
        return LocustOpenAPIPoolManager(self.user, pool_manager)
