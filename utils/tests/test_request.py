# -*- coding: utf-8 -*-
"""
Tests for utils/request.py
"""
import os
from copy import deepcopy
from unittest.mock import MagicMock, patch

import pytest
from locust import HttpUser

from utils.base import ImplementationError, MilMoveEnv
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.request import MilMoveRequestMixin, MilMoveRequestPreparer
from utils.rest import get_json_headers
from utils.types import RequestKwargsType


class TestMilMoveRequestPreparer:
    """
    Tests for MilMoveRequestPreparer
    """

    @pytest.mark.parametrize(
        "env,certs_required,expected_kwargs",
        (
            (MilMoveEnv.LOCAL, False, {"headers": get_json_headers()}),
            (MilMoveEnv.LOCAL, True, {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)}),
            (MilMoveEnv.DP3, False, {"headers": get_json_headers()}),
            (MilMoveEnv.DP3, True, {"headers": get_json_headers(), "cert": DP3_CERT_KEY_PEM}),
        ),
    )
    def test_returns_expected_request_kwargs(
        self, env: MilMoveEnv, certs_required: bool, expected_kwargs: RequestKwargsType
    ) -> None:

        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.get_request_kwargs(certs_required=certs_required) == expected_kwargs

    @pytest.mark.parametrize(
        "env,deployed_subdomain,local_port,local_protocol,local_subdomain,expected_base_domain",
        (
            (MilMoveEnv.LOCAL, "", "8080", "http", "officelocal", "http://officelocal:8080"),
            (MilMoveEnv.LOCAL, "", "8080", "http", "milmovelocal", "http://milmovelocal:8080"),
            (MilMoveEnv.LOCAL, "", "9443", "https", "primelocal", "https://primelocal:9443"),
            (MilMoveEnv.DP3, "office", "", "", "", "https://office.loadtest.dp3.us"),
            (MilMoveEnv.DP3, "my", "", "", "", "https://my.loadtest.dp3.us"),
            (MilMoveEnv.DP3, "api", "", "", "", "https://api.loadtest.dp3.us"),
        ),
    )
    def test_returns_expected_base_domain_for_each_env(
        self,
        env: MilMoveEnv,
        deployed_subdomain: str,
        local_port: str,
        local_protocol: str,
        local_subdomain: str,
        expected_base_domain: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert (
            request_preparer.form_base_domain(
                deployed_subdomain=deployed_subdomain,
                local_port=local_port,
                local_protocol=local_protocol,
                local_subdomain=local_subdomain,
            )
            == expected_base_domain
        )

    @pytest.mark.parametrize("invalid_port", ("0", "12", "123", "12345", "123456", "hi"))
    def test_raises_implementation_error_if_invalid_local_port_is_passed_in(self, invalid_port: str) -> None:
        request_preparer = MilMoveRequestPreparer(env=MilMoveEnv.LOCAL)

        with pytest.raises(ImplementationError, match="The local port must be a string of 4 digits."):
            request_preparer.form_base_domain(local_port=invalid_port)

    @patch.dict(os.environ, {"BASE_DOMAIN": "https://localhost:8080/"})
    @pytest.mark.parametrize("env", (MilMoveEnv.LOCAL, MilMoveEnv.DP3))
    def test_can_override_base_domain_with_env_var_regardless_of_env(self, env: MilMoveEnv) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_base_domain() == "https://localhost:8080/"

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "http://officelocal:8080/ghc/v1/moves"),
            (MilMoveEnv.LOCAL, "/queue", "http://officelocal:8080/ghc/v1/queue"),
            (MilMoveEnv.DP3, "/moves", "https://office.loadtest.dp3.us/ghc/v1/moves"),
        ),
    )
    def test_can_form_expected_ghc_path(
        self,
        env: MilMoveEnv,
        endpoint: str,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_ghc_path(endpoint=endpoint) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "http://officelocal:8080/ghc/v1/moves"),
            (MilMoveEnv.LOCAL, "/queue", "http://officelocal:8080/ghc/v1/queue"),
            (MilMoveEnv.DP3, "/moves", "https://office.loadtest.dp3.us/ghc/v1/moves"),
        ),
    )
    def test_returns_values_needed_for_making_a_ghc_request(
        self, env: MilMoveEnv, endpoint: str, expected_path: str
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_ghc_request(endpoint=endpoint) == (expected_path, {"headers": get_json_headers()})

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "http://milmovelocal:8080/internal/moves"),
            (MilMoveEnv.LOCAL, "/mto-shipments", "http://milmovelocal:8080/internal/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", "https://my.loadtest.dp3.us/internal/moves"),
        ),
    )
    def test_can_form_expected_internal_path(
        self,
        env: MilMoveEnv,
        endpoint: str,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_internal_path(endpoint=endpoint) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "http://milmovelocal:8080/internal/moves"),
            (MilMoveEnv.LOCAL, "/mto-shipments", "http://milmovelocal:8080/internal/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", "https://my.loadtest.dp3.us/internal/moves"),
        ),
    )
    def test_returns_values_needed_for_making_an_internal_request(
        self, env: MilMoveEnv, endpoint: str, expected_path: str
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_internal_request(endpoint=endpoint) == (
            expected_path,
            {"headers": get_json_headers()},
        )

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "https://primelocal:9443/prime/v1/moves"),
            (MilMoveEnv.LOCAL, "/mto-shipments", "https://primelocal:9443/prime/v1/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", "https://api.loadtest.dp3.us/prime/v1/moves"),
        ),
    )
    def test_can_form_expected_prime_path(
        self,
        env: MilMoveEnv,
        endpoint: str,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_prime_path(endpoint=endpoint) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,expected_path,expected_request_kwargs",
        (
            (
                MilMoveEnv.LOCAL,
                "/moves",
                "https://primelocal:9443/prime/v1/moves",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.LOCAL,
                "/mto-shipments",
                "https://primelocal:9443/prime/v1/mto-shipments",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.DP3,
                "/moves",
                "https://api.loadtest.dp3.us/prime/v1/moves",
                {"headers": get_json_headers(), "cert": DP3_CERT_KEY_PEM},
            ),
        ),
    )
    def test_returns_values_needed_for_making_a_prime_request(
        self, env: MilMoveEnv, endpoint: str, expected_path: str, expected_request_kwargs: RequestKwargsType
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_prime_request(endpoint=endpoint) == (expected_path, expected_request_kwargs)

    @pytest.mark.parametrize(
        "env,endpoint,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", "https://primelocal:9443/support/v1/moves"),
            (MilMoveEnv.LOCAL, "/mto-shipments", "https://primelocal:9443/support/v1/mto-shipments"),
            (MilMoveEnv.DP3, "/moves", "https://api.loadtest.dp3.us/support/v1/moves"),
        ),
    )
    def test_can_form_expected_support_path(self, env: MilMoveEnv, endpoint: str, expected_path: str) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_support_path(endpoint=endpoint) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,expected_path,expected_request_kwargs",
        (
            (
                MilMoveEnv.LOCAL,
                "/moves",
                "https://primelocal:9443/support/v1/moves",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.LOCAL,
                "/mto-shipments",
                "https://primelocal:9443/support/v1/mto-shipments",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.DP3,
                "/moves",
                "https://api.loadtest.dp3.us/support/v1/moves",
                {"headers": get_json_headers(), "cert": DP3_CERT_KEY_PEM},
            ),
        ),
    )
    def test_returns_values_needed_for_making_a_support_request(
        self, env: MilMoveEnv, endpoint: str, expected_path: str, expected_request_kwargs: RequestKwargsType
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_support_request(endpoint=endpoint) == (expected_path, expected_request_kwargs)


class TestMilMoveRequestMixin:
    """
    Tests for MilMoveRequestMixin
    """

    @pytest.mark.parametrize(
        "user_host,env",
        (
            ("local", MilMoveEnv.LOCAL),
            ("dp3", MilMoveEnv.DP3),
        ),
    )
    def test_sets_milmove_env_on_init(self, user_host: str, env: MilMoveEnv) -> None:
        mock_locust_env = MagicMock()  # All users need to be initialized with an environment.

        class SampleUser(MilMoveRequestMixin, HttpUser):
            """
            User to use for unit tests
            """

            host = user_host  # Need to manually set here since it would normally be set by the CLI.

        assert not hasattr(SampleUser, "env")

        user = SampleUser(environment=mock_locust_env)

        assert hasattr(user, "env")

        assert user.env == env

    @pytest.mark.parametrize(
        "user_host,env",
        (
            ("local", MilMoveEnv.LOCAL),
            ("dp3", MilMoveEnv.DP3),
        ),
    )
    def test_sets_up_request_preparer_on_init(self, user_host: str, env: MilMoveEnv) -> None:
        mock_locust_env = MagicMock()  # All users need to be initialized with an environment.

        class SampleUser(MilMoveRequestMixin, HttpUser):
            """
            User to use for unit tests
            """

            host = user_host  # Need to manually set here since it would normally be set by the CLI.

        assert not hasattr(SampleUser, "request_preparer")

        user = SampleUser(environment=mock_locust_env)

        assert hasattr(user, "request_preparer")

        assert user.request_preparer == MilMoveRequestPreparer(env=env)
