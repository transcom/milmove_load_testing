# -*- coding: utf-8 -*-
""" utils/constants.py is for constant values useful throughout the codebase. """
import os

from .base import ValueEnum

STATIC_FILES = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static")
TEST_PDF = os.path.join(STATIC_FILES, "test_upload.pdf")

STATIC_TLS_FILES = os.path.join(STATIC_FILES, "tls")
DOD_CA_BUNDLE = os.path.join(STATIC_TLS_FILES, "dod-ca-60-61-bundle.pem")
LOCAL_MTLS_CERT = os.path.join(STATIC_TLS_FILES, "devlocal-mtls.cer")
LOCAL_MTLS_KEY = os.path.join(STATIC_TLS_FILES, "devlocal-mtls.key")

LOCAL_TLS_CERT_KWARGS = {"cert": (LOCAL_MTLS_CERT, LOCAL_MTLS_KEY), "verify": False}

PRIME_API_KEY = "prime"
SUPPORT_API_KEY = "support"
INTERNAL_API_KEY = "internal"

ARRAY_MIN = 1
ARRAY_MAX = 5

ZERO_UUID = "00000000-0000-0000-0000-000000000000"

CUSTOMER = "customer"
MOVE = "move"
MOVE_TASK_ORDER = "mto"
MTO_AGENT = "mtoAgent"
MTO_SHIPMENT = "mtoShipment"
MTO_SERVICE_ITEM = "mtoServiceItem"
ORDER = "order"
PAYMENT_REQUEST = "paymentRequest"
QUEUES = "queues"


class DataType(ValueEnum):
    """Swagger data types that we expect to deal with. Uses camelcase in values to match."""

    FIRST_NAME = "firstName"
    FIRST_NAME_VARIANT = "first_name"  # matches older swagger format
    LAST_NAME = "lastName"
    LAST_NAME_VARIANT = "last_name"  # matches older swagger format
    PHONE = "phone"
    EMAIL = "email"
    STREET_ADDRESS = "streetAddress"
    CITY = "city"
    STATE = "state"
    POSTAL_CODE = "postalCode"
    POSTAL_CODE_VARIANT = "postal_code"
    COUNTRY = "country"
    DATE = "date"
    DATE_TIME = "date-time"  # inconsistent, but matches the swagger format name
    TIME_MILITARY = "timeMilitary"
    SENTENCE = "sentence"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    UUID = "uuid"
    TAC = "tac"

    # These data type options are structural:
    ENUM = "enum"
    ARRAY = "array"
    OBJECT = "object"
