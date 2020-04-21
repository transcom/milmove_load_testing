# -*- coding: utf-8 -*-
import time

from locust import TaskSequence
from locust import task
from locust import events

from bravado.swagger_model import load_file
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from bravado_core.formatter import SwaggerFormat
from bravado_core.exception import SwaggerMappingError
from bravado.exception import HTTPError


def get_swagger_config():
    """
    Generate the config used in generating the swagger client from the spec
    """

    # MilMove uses custom formats for some fields. Without wanting to duplicate them here but
    # still wanting to not get warnings about them being undefined the UDFs are created here.
    # See https://bravado-core.readthedocs.io/en/stable/formats.html
    milmove_formats = []
    string_fmt_list = [
        "basequantity",
        "cents",
        "edipi",
        "millicents",
        "mime-type",
        "ssn",
        "telephone",
        "uri",
        "uuid",
        "x-email",
        "zip",
    ]
    for fmt in string_fmt_list:
        swagger_fmt = SwaggerFormat(
            format=fmt,
            to_wire=str,
            to_python=str,
            validate=lambda x: x,
            description="Converts [wire]string:string <=> python string",
        )
        milmove_formats.append(swagger_fmt)
    swagger_config = {
        # Validate our own requests to catch any problems with python type conversions
        "validate_requests": True,
        # Many of our payloads have invalid responses per the spec because of OpenAPI 2.0 issues
        "validate_responses": False,
        "formats": milmove_formats,
        "use_models": False,
    }
    return swagger_config


class BaseTaskSequence(TaskSequence):
    local_cert = (
        "./config/tls/devlocal-mtls.cer",
        "./config/tls/devlocal-mtls.key",
    )