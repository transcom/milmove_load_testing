# -*- coding: utf-8 -*-
""" utils/constants.py is for constant values useful throughout the codebase. """
import os

from .base import ImplementationError, ListEnum

STATIC_FILES = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static")
LOCAL_MTLS_CERT = os.path.join(STATIC_FILES, "certs/devlocal-mtls.cer")
LOCAL_MTLS_KEY = os.path.join(STATIC_FILES, "certs/devlocal-mtls.key")

PRIME_CERT_KWARGS = {"cert": (LOCAL_MTLS_CERT, LOCAL_MTLS_KEY), "verify": False}


class MilMoveEnv(ListEnum):
    LOCAL = "local"
    STAGING = "staging"
    EXPERIMENTAL = "experimental"


class MilMoveDomain(ListEnum):
    PRIME = "prime"
    OFFICE = "office"
    MILMOVE = "milmove"

    @property
    def local_value(self):
        return f"{self.value}local"

    @property
    def deployed_value(self):
        if self.value == self.MILMOVE.value:
            return "my"

        return self.value

    def host_name(self, env, is_api=False, port="3000", protocol="https"):
        """
        Returns the host name for this domain based on the environment, whether or not it is in the API domain, and the
        port and protocol (for local envs).
        :param env: str MilMoveEnv
        :param is_api: bool
        :param port: str containing 4 digits
        :param protocol: str "https" or "http"
        :return: str host
        """
        if isinstance(env, MilMoveEnv):
            env = env.value  # ensure that we're using the value string instead of the Enum literal

        if env not in MilMoveEnv.values():
            raise ImplementationError("The environment for determining the host name must be included in MilMoveEnv.")

        if env == MilMoveEnv.LOCAL.value:
            port = str(port)  # in case an int was passed in
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"{protocol}://{self.local_value}:{port}"

        # NOTE: deployed protocol is always https
        return f"https://{'api' if is_api else self.deployed_value}.{env}.move.mil"


class DataType(ListEnum):
    """ Swagger data types that we expect to deal with. Uses camelcase in values to match. """

    FIRST_NAME = "firstName"
    LAST_NAME = "lastName"
    PHONE = "phone"
    EMAIL = "email"
    STREET_ADDRESS = "streetAddress"
    CITY = "city"
    STATE = "state"
    POSTAL_CODE = "postalCode"
    COUNTRY = "country"
    DATE = "date"
    DATE_TIME = "date-time"  # inconsistent, but matches the swagger format name
    TIME_MILITARY = "timeMilitary"
    SENTENCE = "sentence"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    UUID = "uuid"

    # These data type options are structural:
    ENUM = "enum"
    ARRAY = "array"
    OBJECT = "object"
