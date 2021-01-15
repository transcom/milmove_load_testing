# -*- coding: utf-8 -*-
""" utils/hosts.py is for the tools that handle setting the MilMove hostnames and setting up TLS certs. """
import logging
import os
from typing import Optional

from locust.env import Environment

from .base import ImplementationError, ListEnum
from .constants import LOCAL_MTLS_CERT, LOCAL_MTLS_KEY, DOD_CA_BUNDLE, STATIC_TLS_FILES

logger = logging.getLogger(__name__)


class MilMoveEnv(ListEnum):
    LOCAL = "local"
    EXP = "exp"
    STG = "stg"


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

    def host_name(self, env, is_api=False, port="0000", protocol="https"):
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
            port = str(port)  # just in case an int was passed in
            if not port.isdigit() or len(port) != 4:
                raise ImplementationError("The local port must be a string of 4 digits.")

            return f"{protocol}://{self.local_value}:{port}"

        # NOTE: deployed protocol is always https
        return f"https://{'api' if is_api else self.deployed_value}.{env}.move.mil"


class MilMoveHostMixin:
    """
    Mixin for Locust's HttpUser class that sets a host value based on the environment passed in as the --host flag.
    """

    # The abbreviated domain name for the host. Can be any of the values in MilMoveDomain.
    domain: MilMoveDomain = None

    # The abbreviated name of the environment the host is running in (ex. locally or deployed).
    # Can be any of the values in MilMoveEnv.
    env: MilMoveEnv = None

    # The HTTP protocol and port used for a local host:
    local_protocol: str = "https"
    local_port: str = "0000"

    # A boolean indicating whether or not the host belongs to an API on the server.
    # For deployed environments only, this will change the host to use api.<env>.move.mil instead of the standard
    # domain name.
    is_api: bool = False

    # The set of kwargs that will be used to authenticate an HTTP request, in the format:
    # {"cert": <cert/key file path(s)>, "verify": <False or the CA bundle file path>}
    cert_kwargs: Optional[dict] = None

    @classmethod
    def set_milmove_env(cls, env: str):
        """
        Sets the environment attribute for the class. Takes in a string and sets a MilMoveEnv literal to cls.env.
        """
        # Check if we already have a value set (this would be purposeful):
        if cls.env:
            return

        try:
            cls.env = MilMoveEnv.match(env)
        except IndexError:  # means MilMoveEnv could not find a match for the value passed in
            logger.debug(f"Bad env value: {env}")
            raise ImplementationError("Environment for MilMoveHostMixin must match one of the values in MilMoveEnv.")

    @classmethod
    def set_host_name(cls):
        """
        Sets the hostname based on the domain, environment, and whether or not it is an API.

        Applies to every instance of the class (or subclass), which reduces the number of times this value will be
        calculated for users with the exact same attributes to only once during a load test.
        """
        # Check if we already have a value set (this would be purposeful):
        if cls.host:
            return

        try:
            cls.host = MilMoveDomain.match(cls.domain).host_name(
                cls.env.value, cls.is_api, cls.local_port, cls.local_protocol
            )
        except IndexError:  # means MilMoveDomain could not find a match for the value passed in
            logger.debug(f"Bad domain value: {cls.domain}")
            raise ImplementationError("Domain for MilMoveHostMixin must match one of the values in MilMoveDomain.")

    @classmethod
    def set_cert_kwargs(cls):
        """
        Sets the certificate kwargs that will be used for validating the HTTPS request from this user. These will point
        to the file paths for the TLS cert/key files and the DoD's CA bundle file. The files used will change based on
        the environment.

        Applies to every instance of the class (or subclass), which reduces the number of times this value will be
        calculated for users with the exact same attributes to only once during a load test.
        """
        # Check if we already have a value set (this would be purposeful) and skip the logic to create it again:
        if cls.cert_kwargs:
            return

        if cls.env == MilMoveEnv.LOCAL:
            cls.cert_kwargs = {"cert": (LOCAL_MTLS_CERT, LOCAL_MTLS_KEY), "verify": False}
            return

        # We now know we're in a deployed environment, so let's make a deployed cert/key file:
        cert_key = cls.create_deployed_cert_file()

        # We also need to use the DoD's specific CA bundle for SSL verification in deployed envs:
        cls.cert_kwargs = {"cert": cert_key, "verify": DOD_CA_BUNDLE}

    @classmethod
    def create_deployed_cert_file(cls) -> str:
        """
        Grabs the certificate and key values for this environment from the relevant environment variables (which must be
        set for this function to work), and then creates a new .pem file that contains both the certificate and the key
        TLS request validation. This is only called for deployed MilMove environments.

        :return: str, the path to the newly created cert file
        """
        deployed_tls_cert = os.getenv(f"MOVE_MIL_{cls.env.value.upper()}_TLS_CERT")
        deployed_tls_key = os.getenv(f"MOVE_MIL_{cls.env.value.upper()}_TLS_KEY")

        if not (deployed_tls_cert and deployed_tls_key):
            logger.debug(f"Unable to find cert and key values for environment: {cls.env.value}")
            raise ImplementationError(
                "Cannot run load testing in a deployed environment without the matching certificate and key."
            )

        cert_key_file = os.path.join(STATIC_TLS_FILES, f"{cls.env.value}_tls_cert_key.pem")
        with open(cert_key_file, "w") as f:
            f.write(deployed_tls_cert)
            f.write("\n")
            f.write(deployed_tls_key)

        return cert_key_file

    @classmethod
    def remove_deployed_cert_file(cls):
        """
        Removes the .pem cert/key file that was created for running load tests against a deployed environment.
        """
        try:
            os.remove(cls.cert_kwargs["cert"])
        except (KeyError, FileNotFoundError):
            # If there was a KeyError, that means "cert" wasn't in the cert_kwargs dict - it may have been cleard out.
            # If there was a FileNotFoundError, whatever path was in the "cert" kwarg was incorrect or the file was
            # already removed.

            # In either case, let's try again to remove the file using the custom filename to be extra sure we're
            # cleaning up after ourselves:
            try:
                os.remove(os.path.join(STATIC_TLS_FILES, f"{cls.env.value if cls.env else ''}_tls_cert_key.pem"))
            except FileNotFoundError:
                # The file is gone, huzzah!
                pass

        # Finally, clear out all traces of the deployed cert file:
        cls.cert_kwargs = None


def setup_milmove_host_users(locust_env: Environment):
    """
    Sets the Users' host based on environment value from --host flag in command. This should be called in the
    "test_start" event for a locustfile/load test.

    To do this, we're going to iterate over all the User classes defined in this locust environment (which is the
    equivalent of all the User classes defined in the locustfile for the test that calls this function), and if the User
    is a subclass of MilMoveHostMixin, we'll run all the relevant class-level setup functions.
    """
    # Check if the host value is one of our accepted environments. If not, we'll continue with the host entered as-is
    # and skip the rest of the custom setup.
    if not MilMoveEnv.validate(locust_env.host):
        return

    for user_class in locust_env.user_classes:
        if issubclass(user_class, MilMoveHostMixin):
            user_class.set_milmove_env(locust_env.host)
            user_class.set_host_name()
            user_class.set_cert_kwargs()


def clean_milmove_host_users(locust_env: Environment):
    """
    Cleans up the Users' cert/key settings if the User is a subclass of MilMoveHostMixin. This should be called in the
    "test_stop" event for a locustfile/load test.
    """
    for user_class in locust_env.user_classes:
        if issubclass(user_class, MilMoveHostMixin):
            user_class.remove_deployed_cert_file()
