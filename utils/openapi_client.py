# import locust first because it monkeypatches ssl
from locust.clients import HttpSession

from abc import abstractmethod, ABC
from urllib.parse import urlparse

from copy import deepcopy
from requests import Session
import requests.exceptions

from typing import Optional

import internal_client
import ghc_client
import prime_client

import requests
import requests.cookies

from utils.auth import UserType
from utils.request import MilMoveRequestPreparer, RequestHost
from utils.types import RequestKwargsType


class PoolManager(ABC):
    resource_path: str

    @abstractmethod
    def request(self, method, url, **kwargs):
        raise NotImplementedError


class AbstractRestClient(ABC):
    """
    Try to document type expectations for ResourcePathMixin
    """

    pool_manager: PoolManager


class AbstractApiConfig(ABC):
    """
    Try to document type expectations for ResourcePathMixin
    """

    host: str


class AbstractApiClient(ABC):
    """
    Try to document type expectations for ResourcePathMixin
    """

    configuration: AbstractApiConfig
    rest_client: AbstractRestClient


class SetResourcePathMixin(AbstractApiClient):
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


def internal_api_client(
    request_preparer: MilMoveRequestPreparer, client: Session, user_type: UserType
) -> LocustInternalApiClient:
    request_host = RequestHost.MY
    if user_type != UserType.MILMOVE:
        request_host = RequestHost.OFFICE

    base_url = request_preparer.form_internal_path(request_host=request_host, endpoint="")
    req = requests.Request("GET", base_url)
    cookie = requests.cookies.get_cookie_header(client.cookies, req)
    configuration = internal_client.Configuration(host=base_url)
    api_client = LocustInternalApiClient(configuration, cookie=cookie)
    for k, v in client.headers.items():
        api_client.set_default_header(k, v)
    api_client.rest_client.pool_manager = LocustOpenAPIPoolManager(client)
    return api_client


def ghc_api_client(
    request_preparer: MilMoveRequestPreparer, client: Session, user_type: UserType
) -> LocustGHCApiClient:
    request_host = RequestHost.MY
    if user_type != UserType.MILMOVE:
        request_host = RequestHost.OFFICE

    base_url = request_preparer.form_ghc_path(request_host=request_host, endpoint="")
    req = requests.Request("GET", base_url)
    cookie = requests.cookies.get_cookie_header(client.cookies, req)
    configuration = ghc_client.Configuration(host=base_url)
    api_client = LocustGHCApiClient(configuration, cookie=cookie)
    for k, v in client.headers.items():
        api_client.set_default_header(k, v)
    api_client.rest_client.pool_manager = LocustOpenAPIPoolManager(client)
    return api_client


def prime_api_client(request_preparer: MilMoveRequestPreparer, client: Session) -> LocustPrimeApiClient:
    host = request_preparer.form_prime_path("")
    # prime doesn't need cookies?
    # req = requests.Request("GET", host)
    # cookie = requests.cookies.get_cookie_header(client.cookies, req)
    configuration = internal_client.Configuration(host=host)
    #    api_client = LocustPrimeApiClient(configuration, cookie=cookie)
    api_client = LocustPrimeApiClient(configuration)
    api_client.rest_client.pool_manager = LocustOpenAPIPoolManager(client, request_preparer.get_cert_kwargs())
    return api_client


class LocustResponseWrapper(object):
    """
    Wraps a requests.Response so it quacks like a urllib3.response.BaseHTTPResponse
    """

    response: requests.Response

    def __init__(self, response: requests.Response):
        self.response = response

    # provide proxy access to regular attributes of wrapped object
    def __getattr__(self, name):
        if name == "status":
            return self.response.status_code
        elif name == "data":
            return self.response.content
        else:
            return getattr(self.response, name)

    def getheader(self, name, default=None) -> Optional[str]:
        return self.response.headers.get(name, default)

    def getheaders(self):
        return self.response.headers

    def json(self, **kwargs):
        return self.response.json(**kwargs)


class LocustOpenAPIPoolManager(PoolManager):
    """Reimplements the locust tracking from HttpSession for openapi"""

    resource_path: Optional[str]
    session: requests.Session
    cert_kwargs: Optional[RequestKwargsType]

    def __init__(self, session: requests.Session, cert_kwargs: Optional[RequestKwargsType] = None):
        self.session = session
        self.resource_path = None
        self.cert_kwargs = cert_kwargs

    def request(self, method, url, **kwargs) -> LocustResponseWrapper:
        """
        Pretend to be a urllib3.PoolManager but instead use the locust
        provided HttpSession (which is itself a wrapper around
        requests.Session) so that all request statistics are reported
        properly to locust

        """
        # requests.Session.request() uses "params" instead of "fields"
        if "fields" in kwargs:
            files = {}
            params = {}
            for field_tuple in kwargs.pop("fields"):
                # if this field looks like it is a file upload, add it
                # to files as that is what requests.Session.request()
                # expects
                #
                # Otherwise, add it to params as that is what
                # requests.Session.request() expects for query params
                if (
                    isinstance(field_tuple[1], tuple)
                    and len(field_tuple[1]) > 1
                    and isinstance(field_tuple[1][1], bytes)
                ):
                    files[field_tuple[0]] = field_tuple[1]
                else:
                    params[field_tuple[0]] = field_tuple[1]
            if files:
                kwargs["files"] = files
                # requests.Session.request() does not support
                # encode_multipart as it handles that itself. Clean up
                # all parameters associated with multipart handling
                if kwargs.pop("encode_multipart"):
                    # remove existing content-type so requests will
                    # add it
                    if kwargs["headers"].get("Content-type"):
                        kwargs["headers"].pop("Content-type")
            if params:
                kwargs["params"] = params
        if "encode_multipart" in kwargs:
            # if somehow encode_multipart was set but we did not find
            # files, something has gone wrong in our translation
            raise Exception("Unhandled encode_multipart")
        # requests.Session.request() does not understand
        # preload_content
        if "preload_content" in kwargs:
            kwargs.pop("preload_content")
        # requests.Session.request() expects data instead of body
        if "body" in kwargs:
            kwargs["data"] = kwargs.pop("body")

        # if this is a locust HttpSession, add a name attribute for
        # tracking requests with parameters. See SetResourcePathMixin
        # above
        if isinstance(self.session, HttpSession):
            parsed_url = urlparse(url)
            name = self.resource_path or parsed_url.path
            kwargs["name"] = name

        if self.cert_kwargs:
            kwargs.update(deepcopy(self.cert_kwargs))

        resp = self.session.request(method=method, url=url, **kwargs)
        return LocustResponseWrapper(resp)
