# -*- coding: utf-8 -*-
""" utils/hosts.py is for the tools that handle setting the MilMove hostnames and setting up TLS certs. """
import logging
import os
from typing import Optional

from locust.env import Environment

from .base import ImplementationError, ValueEnum
from .constants import LOCAL_MTLS_CERT, LOCAL_MTLS_KEY, DOD_CA_BUNDLE, STATIC_TLS_FILES

logger = logging.getLogger(__name__)


class MilMoveEnv(ValueEnum):
    LOCAL = "local"
    EXP = "exp"
    DOD = "dod"
    DP3 = "dp3"


class MilMoveDomain(ValueEnum):
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

        # allow us to point to another domain if we need to
        base_domain = os.getenv("BASE_DOMAIN", "loadtest.dp3.us")
        # NOTE: deployed protocol is always https
        return f"https://{'api' if is_api else self.deployed_value}.{base_domain}"


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

    def __init__(self, *args, **kwargs):
        """
        Sets the Users' host based on environment value from --host flag in command. Note that the self.host value is
        set on the class from the command line flag BEFORE initialization. Also sets the env and cert_kwargs, the input
        needed for TLS requests, values.

        These attributes are set on the CLASS-level. This is important because we do not want to repeat this process for
        thousands of Users with the exact same settings.
        """
        # Check if the host value is one of our accepted environments. If not, we'll continue with the host entered
        # as-is and skip the rest of the custom setup.
        if MilMoveEnv.validate(self.host):
            type(self).set_milmove_env(self.host)
            type(self).host = None
            type(self).set_host_name()
            type(self).set_cert_kwargs()

        super().__init__(*args, **kwargs)

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

        verify_path = DOD_CA_BUNDLE
        # DP3 certs are issued by CAs that are well known and so we
        # don't need any special verification
        if cls.env == MilMoveEnv.DP3:
            verify_path = None

        # We also need to use the DoD's specific CA bundle for SSL verification in deployed envs:
        cls.cert_kwargs = {"cert": cert_key, "verify": verify_path}

    @classmethod
    def create_deployed_cert_file(cls) -> Optional[str]:
        """
        Grabs the TLS certificate and key values for this environment from the relevant environment variables (which
        must be set for this function to work), and then creates a new .pem file that contains both the certificate and
        the key for request validation. This is only called for deployed MilMove environments.

        :return: str, the path to the newly created cert file
        """
        if cls.env == MilMoveEnv.LOCAL:
            return  # can't complete this logic with local certs

        deployed_tls_cert = os.environ.get(f"MOVE_MIL_{cls.env.value.upper()}_TLS_CERT")
        deployed_tls_key = os.environ.get(f"MOVE_MIL_{cls.env.value.upper()}_TLS_KEY")

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
        if cls.env == MilMoveEnv.LOCAL:
            return  # can't complete this logic with local certs

        try:
            os.remove(cls.cert_kwargs["cert"])
        except (KeyError, TypeError, FileNotFoundError):
            # KeyError means "cert" wasn't in the cert_kwargs dict - it may have been cleared out.
            # TypeError means self.cert_kwargs["cert"] did not resolve to a string - also means we may have already
            # removed this file.
            # FileNotFoundError means whatever path was in the "cert" kwarg was incorrect or the file was already
            # removed.

            # In any case, let's try again to remove the file using the custom filename to be extra sure we're
            # cleaning up after ourselves:
            try:
                os.remove(os.path.join(STATIC_TLS_FILES, f"{cls.env.value if cls.env else ''}_tls_cert_key.pem"))
            except FileNotFoundError:
                # The file is gone, huzzah!
                pass

        # Finally, clear out all traces of the deployed cert file:
        cls.cert_kwargs = {}

    @property
    def is_local(self):
        """ Indicates if this user is using the local environment. """
        return self.env == MilMoveEnv.LOCAL

    @property
    def is_deployed(self):
        """ Indicates if this user is running in a deployed environment. """
        return self.env != MilMoveEnv.LOCAL


def clean_milmove_host_users(locust_env: Environment):
    """
    Cleans up the Users' cert/key settings if the User is a subclass of MilMoveHostMixin. This should be called in the
    "test_stop" event for a locustfile/load test.
    """
    if locust_env.host == MilMoveEnv.LOCAL.value:
        return  # we don't need to remove any cert files for a local test run

    for user_class in locust_env.user_classes:
        if issubclass(user_class, MilMoveHostMixin):
            user_class.remove_deployed_cert_file()

    logger.info("Cleaned up User SSL/TLS certificates.")
