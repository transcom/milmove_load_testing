# -*- coding: utf-8 -*-
"""
Tests for utils/request.py
"""
import os
from copy import deepcopy
from unittest.mock import patch

import pytest

from utils.base import ImplementationError, MilMoveEnv
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.request import MilMoveRequestPreparer, RequestHost
from utils.types import RequestKwargsType


class TestRequestHost:
    """
    Tests for RequestHost
    """

    @pytest.mark.parametrize(
        "request_host,local_subdomain",
        (
            (RequestHost.MY, "milmovelocal"),
            (RequestHost.OFFICE, "officelocal"),
            (RequestHost.PRIME, "primelocal"),
        ),
    )
    def test_local_subdomain(self, request_host: RequestHost, local_subdomain: str):
        assert request_host.local_subdomain() == local_subdomain


class TestMilMoveRequestPreparer:
    """
    Tests for MilMoveRequestPreparer
    """

    @pytest.mark.parametrize(
        "milmove_env,expected_kwargs",
        (
            (
                MilMoveEnv.LOCAL,
                {
                    **deepcopy(LOCAL_TLS_CERT_KWARGS),
                },
            ),
            (
                MilMoveEnv.DP3,
                {
                    "cert": DP3_CERT_KEY_PEM,
                },
            ),
        ),
    )
    def test_returns_expected_request_kwargs(self, milmove_env: MilMoveEnv, expected_kwargs: RequestKwargsType) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert request_preparer.get_cert_kwargs() == expected_kwargs

    @pytest.mark.parametrize(
        "milmove_env,deployed_subdomain,local_port,local_protocol,local_subdomain,expected_base_domain",
        (
            (MilMoveEnv.LOCAL, "", "8080", "http", "officelocal", "http://officelocal:8080"),
            (MilMoveEnv.LOCAL, "", "8080", "http", "milmovelocal", "http://milmovelocal:8080"),
            (MilMoveEnv.LOCAL, "", "9443", "https", "primelocal", "https://primelocal:9443"),
            (MilMoveEnv.DP3, "office", "", "", "", "https://office.loadtest.dp3.us"),
            (MilMoveEnv.DP3, "my", "", "", "", "https://my.loadtest.dp3.us"),
            (MilMoveEnv.DP3, "api", "", "", "", "https://api.loadtest.dp3.us"),
        ),
    )
    def test_returns_expected_form_base_url_for_each_env(
        self,
        milmove_env: MilMoveEnv,
        deployed_subdomain: str,
        local_port: str,
        local_protocol: str,
        local_subdomain: str,
        expected_base_domain: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert (
            request_preparer._form_base_url(
                deployed_subdomain=deployed_subdomain,
                local_port=local_port,
                local_protocol=local_protocol,
                local_subdomain=local_subdomain,
            )
            == expected_base_domain
        )

    @pytest.mark.parametrize("invalid_port", ("0", "12", "123", "12345", "123456", "hi"))
    def test_raises_implementation_error_if_invalid_local_port_is_passed_in(self, invalid_port: str) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env=MilMoveEnv.LOCAL)

        with pytest.raises(ImplementationError, match="The local port must be a string of 4 digits."):
            request_preparer._form_base_url(local_port=invalid_port)

    @patch.dict(os.environ, {"BASE_DOMAIN": "https://localhost:8080/"})
    @pytest.mark.parametrize("milmove_env", (MilMoveEnv.LOCAL, MilMoveEnv.DP3))
    def test_can_override_base_domain_with_env_var_regardless_of_env(self, milmove_env: MilMoveEnv) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert request_preparer._form_base_url() == "https://localhost:8080/"

    @pytest.mark.parametrize(
        "milmove_env,endpoint,include_prefix,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", True, "http://officelocal:8080/ghc/v1/moves"),
            (
                MilMoveEnv.LOCAL,
                "/internal/users/logged_in",
                False,
                "http://officelocal:8080/internal/users/logged_in",
            ),
            (MilMoveEnv.LOCAL, "/queue", True, "http://officelocal:8080/ghc/v1/queue"),
            (MilMoveEnv.DP3, "/moves", True, "https://office.loadtest.dp3.us/ghc/v1/moves"),
            (
                MilMoveEnv.DP3,
                "/internal/users/logged_in",
                False,
                "https://office.loadtest.dp3.us/internal/users/logged_in",
            ),
        ),
    )
    def test_can_form_expected_ghc_path(
        self,
        milmove_env: MilMoveEnv,
        endpoint: str,
        include_prefix: bool,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert (
            request_preparer.form_ghc_path(
                request_host=RequestHost.OFFICE, endpoint=endpoint, include_prefix=include_prefix
            )
            == expected_path
        )

    @pytest.mark.parametrize(
        "milmove_env,endpoint,include_prefix,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", True, "http://milmovelocal:8080/internal/moves"),
            (MilMoveEnv.LOCAL, "/devlocal-auth/login", False, "http://milmovelocal:8080/devlocal-auth/login"),
            (MilMoveEnv.LOCAL, "/mto-shipments", True, "http://milmovelocal:8080/internal/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", True, "https://my.loadtest.dp3.us/internal/moves"),
            (MilMoveEnv.DP3, "/devlocal-auth/login", False, "https://my.loadtest.dp3.us/devlocal-auth/login"),
        ),
    )
    def test_can_form_expected_internal_path(
        self,
        milmove_env: MilMoveEnv,
        endpoint: str,
        include_prefix: bool,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert (
            request_preparer.form_internal_path(
                request_host=RequestHost.MY, endpoint=endpoint, include_prefix=include_prefix
            )
            == expected_path
        )

    @pytest.mark.parametrize(
        "milmove_env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "https://primelocal:9443/prime/v1/moves"),
            (MilMoveEnv.LOCAL, "/mto-shipments", "https://primelocal:9443/prime/v1/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", "https://api.loadtest.dp3.us/prime/v1/moves"),
        ),
    )
    def test_can_form_expected_prime_path(
        self,
        milmove_env: MilMoveEnv,
        endpoint: str,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(milmove_env)

        assert request_preparer.form_prime_path(endpoint=endpoint) == expected_path
