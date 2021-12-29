# -*- coding: utf-8 -*-
"""
Place to store auth-related code, e.g. for dealing with certs or session tokens.
"""
import logging
import os

from utils.base import ImplementationError, MilMoveEnv
from utils.constants import DP3_CERT_KEY_PEM


logger = logging.getLogger(__name__)


def set_up_certs(host: str) -> None:
    """
    Sets up certs for making requests to the mymove server
    :param host: host that the target server is running in, e.g. dp3
    :return: None
    """
    if host == MilMoveEnv.LOCAL.value:
        return  # We don't need to set up certs for a local run because they already exist

    host_upper = host.upper()

    try:
        deployed_tls_cert = os.environ[f"MOVE_MIL_{host_upper}_TLS_CERT"]
        deployed_tls_key = os.environ[f"MOVE_MIL_{host_upper}_TLS_KEY"]
    except KeyError:
        logger.debug(f"Unable to find cert and key values for environment: {host}")

        raise ImplementationError(
            "Cannot run load testing in a deployed environment without the matching certificate and key."
        ) from None

    with open(DP3_CERT_KEY_PEM, "w") as f:
        f.write(deployed_tls_cert)
        f.write("\n")
        f.write(deployed_tls_key)


def remove_certs(host: str) -> None:
    """
    Removes certs that were set up for making requests to the mymove server
    :param host: host that the target server is running in, e.g. dp3
    :return: None
    """
    if host == MilMoveEnv.LOCAL.value:
        return  # We don't need to delete local certs since they're part of the repo

    try:
        os.remove(DP3_CERT_KEY_PEM)
    except FileNotFoundError:
        # FileNotFoundError means the file was already removed.
        pass
