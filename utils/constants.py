# -*- coding: utf-8 -*-
""" utils/constants.py is for constant values useful throughout the codebase. """
from pathlib import Path

from .base import ValueEnum

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES = BASE_DIR / "static"

TEST_PDF = STATIC_FILES / "test_upload.pdf"

STATIC_TLS_FILES = STATIC_FILES / "tls"

DOD_CA_BUNDLE = STATIC_TLS_FILES / "dod-ca-60-61-bundle.pem"

LOCAL_MTLS_CERT = str(STATIC_TLS_FILES / "devlocal-mtls.cer")
LOCAL_MTLS_KEY = str(STATIC_TLS_FILES / "devlocal-mtls.key")

LOCAL_TLS_CERT_KWARGS = {"cert": (LOCAL_MTLS_CERT, LOCAL_MTLS_KEY), "verify": False}

DP3_CERT_KEY_PEM_FILENAME = "dp3_tls_cert_key.pem"
DP3_CERT_KEY_PEM = str(STATIC_TLS_FILES / DP3_CERT_KEY_PEM_FILENAME)

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
    """
    Swagger data types that we expect to deal with. The latest pattern uses camelCase, while the older pattern uses snake_case.
    """

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
    CITY_STATE_ZIP = "city_state_zip"  # a virtual field to find valid combinations of city, state, and zip
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
