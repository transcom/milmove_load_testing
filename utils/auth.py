# -*- coding: utf-8 -*-
"""
Place to store auth-related code, e.g. for dealing with certs or session tokens.
"""
import logging
import os
from enum import Enum

from requests import Session

from utils.base import ImplementationError, MilMoveEnv, is_local
from utils.constants import DP3_CERT_KEY_PEM
from utils.request import MilMoveRequestPreparer, RequestHost


logger = logging.getLogger(__name__)


def set_up_certs(env: MilMoveEnv) -> None:
    """
    Sets up certs for making requests to the mymove server
    :param env: MilMoveEnv that the target server is running in, e.g. MilMoveEnv.DP3
    :return: None
    """

    if is_local(env=env):
        return  # We don't need to set up certs for a local run because they already exist

    host_upper = env.value.upper()

    try:
        deployed_tls_cert = os.environ[f"MOVE_MIL_{host_upper}_TLS_CERT"]
        deployed_tls_key = os.environ[f"MOVE_MIL_{host_upper}_TLS_KEY"]
    except KeyError:
        logger.debug(f"Unable to find cert and key values for environment: {MilMoveEnv}")

        raise ImplementationError(
            "Cannot run load testing in a deployed environment without the matching certificate and key."
        ) from None

    with open(DP3_CERT_KEY_PEM, "w") as f:
        f.write(deployed_tls_cert)
        f.write("\n")
        f.write(deployed_tls_key)


def remove_certs(env: MilMoveEnv) -> None:
    """
    Removes certs that were set up for making requests to the mymove server
    :param env: MilMoveEnv that the target server is running in, e.g. MilMoveEnv.DP3
    :return: None
    """
    if is_local(env=env):
        return  # We don't need to delete local certs since they're part of the repo

    try:
        os.remove(DP3_CERT_KEY_PEM)
    except FileNotFoundError:
        # FileNotFoundError means the file was already removed.
        pass


class UserType(Enum):
    """
    Holds user types that can be used for creating new users
    """

    MILMOVE = "milmove"
    SERVICE_COUNSELOR = "Services Counselor office"
    TOO = "TOO office"
    TIO = "TIO office"


def create_user(request_preparer: MilMoveRequestPreparer, session: Session, user_type: UserType) -> bool:
    """
    Creates a user. Since this works with sessions, the session should have the cookies set in it
    for follow-up requests.

    :param request_preparer: Initialized request preparer, needed to form proper urls.
    :param session: Session to use and store cookies in, e.g. self.client or requests.Session()
    :param user_type: UserType to log in as.
    :return: boolean indicating if user creation was successful or not.
    """
    # Hacky workaround for now...not sure if this should really be added to the
    # MilMoveRequestPreparer class since it's only needed for this.

    # go to /sign-in instead of /devlocal-auth/login because the
    # latter hits the DB pretty hard in a way that differs from how
    # things would work in the real world
    endpoint = "/sign-in"
    request_host = RequestHost.MY
    if user_type == UserType.MILMOVE:
        # ensure we start with a fresh session for service members
        session.cookies.clear()
        url = request_preparer.form_api_path(request_host=request_host, api_path_prefix="", endpoint=endpoint)
    else:
        request_host = RequestHost.OFFICE
        url = request_preparer.form_api_path(request_host=request_host, api_path_prefix="", endpoint=endpoint)

    resp = session.get(url=url)
    if resp.status_code != 200:
        return False

    csrf_token = session.cookies.get("masked_gorilla_csrf")

    session.headers.update({"x-csrf-token": csrf_token})

    payload = {
        "userType": user_type.value,
        "gorilla.csrf.Token": csrf_token,
    }

    endpoint = "/devlocal-auth/create"
    url = request_preparer.form_api_path(request_host=request_host, api_path_prefix="", endpoint=endpoint)

    resp = session.post(url=url, data=payload)
    return resp.status_code == 200 or resp.status_code == 201
