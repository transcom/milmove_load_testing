# -*- coding: utf-8 -*-
"""
Tests for utils/request.py
"""
import os
from copy import deepcopy
from unittest.mock import MagicMock, patch

import pytest
from locust import TaskSet

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
        "env,certs_required,endpoint_name,expected_kwargs",
        (
            (
                MilMoveEnv.LOCAL,
                False,
                "",
                {
                    "headers": get_json_headers(),
                },
            ),
            (
                MilMoveEnv.LOCAL,
                False,
                "/internal/service_members/{serviceMemberId}",
                {"headers": get_json_headers(), "name": "/internal/service_members/{serviceMemberId}"},
            ),
            (
                MilMoveEnv.LOCAL,
                True,
                "/support/v1/move-task-orders/{moveTaskOrderID}",
                {
                    "name": "/support/v1/move-task-orders/{moveTaskOrderID}",
                    "headers": get_json_headers(),
                    **deepcopy(LOCAL_TLS_CERT_KWARGS),
                },
            ),
            (
                MilMoveEnv.DP3,
                False,
                "/internal/service_members/{serviceMemberId}",
                {"name": "/internal/service_members/{serviceMemberId}", "headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                True,
                "/support/v1/move-task-orders/{moveTaskOrderID}",
                {
                    "name": "/support/v1/move-task-orders/{moveTaskOrderID}",
                    "headers": get_json_headers(),
                    "cert": DP3_CERT_KEY_PEM,
                },
            ),
        ),
    )
    def test_returns_expected_request_kwargs(
        self, env: MilMoveEnv, certs_required: bool, endpoint_name: str, expected_kwargs: RequestKwargsType
    ) -> None:

        request_preparer = MilMoveRequestPreparer(env=env)

        assert (
            request_preparer.get_request_kwargs(certs_required=certs_required, endpoint_name=endpoint_name)
            == expected_kwargs
        )

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
        "env,endpoint,endpoint_name,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/queues/moves",
                "",
                "http://officelocal:8080/ghc/v1/queues/moves",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/queues/counseling",
                "",
                "http://officelocal:8080/ghc/v1/queues/counseling",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/move/1",
                "/move/{locator}",
                "http://officelocal:8080/ghc/v1/move/1",
                {"name": "/ghc/v1/move/{locator}", "headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/queues/moves",
                "",
                "https://office.loadtest.dp3.us/ghc/v1/queues/moves",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/move/1",
                "/move/{locator}",
                "https://office.loadtest.dp3.us/ghc/v1/move/1",
                {"name": "/ghc/v1/move/{locator}", "headers": get_json_headers()},
            ),
        ),
    )
    def test_returns_values_needed_for_making_a_ghc_request(
        self,
        env: MilMoveEnv,
        endpoint: str,
        endpoint_name: str,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_ghc_request(endpoint=endpoint, endpoint_name=endpoint_name) == (
            expected_path,
            expected_headers,
        )

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
        "env,endpoint,endpoint_name,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/users/logged_in",
                "",
                "http://milmovelocal:8080/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/mto_shipments",
                "",
                "http://milmovelocal:8080/internal/mto_shipments",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/service_members/4",
                "/service_members/{serviceMemberId}",
                "http://milmovelocal:8080/internal/service_members/4",
                {"name": "/internal/service_members/{serviceMemberId}", "headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/users/logged_in",
                "",
                "https://my.loadtest.dp3.us/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/service_members/4",
                "/service_members/{serviceMemberId}",
                "https://my.loadtest.dp3.us/internal/service_members/4",
                {"name": "/internal/service_members/{serviceMemberId}", "headers": get_json_headers()},
            ),
        ),
    )
    def test_returns_values_needed_for_making_an_internal_request(
        self,
        env: MilMoveEnv,
        endpoint: str,
        endpoint_name: str,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_internal_request(endpoint=endpoint, endpoint_name=endpoint_name) == (
            expected_path,
            expected_headers,
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
        "env,endpoint,endpoint_name,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/moves",
                "",
                "https://primelocal:9443/prime/v1/moves",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.LOCAL,
                "/mto_shipments",
                "",
                "https://primelocal:9443/prime/v1/mto_shipments",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.LOCAL,
                "/move-task-orders/1234",
                "/move-task-orders/{moveID}",
                "https://primelocal:9443/prime/v1/move-task-orders/1234",
                {
                    "name": "/prime/v1/move-task-orders/{moveID}",
                    "headers": get_json_headers(),
                    **deepcopy(LOCAL_TLS_CERT_KWARGS),
                },
            ),
            (
                MilMoveEnv.DP3,
                "/mto_shipments",
                "",
                "https://api.loadtest.dp3.us/prime/v1/mto_shipments",
                {"headers": get_json_headers(), "cert": DP3_CERT_KEY_PEM},
            ),
            (
                MilMoveEnv.DP3,
                "/move-task-orders/1234",
                "/move-task-orders/{moveID}",
                "https://api.loadtest.dp3.us/prime/v1/move-task-orders/1234",
                {
                    "name": "/prime/v1/move-task-orders/{moveID}",
                    "headers": get_json_headers(),
                    "cert": DP3_CERT_KEY_PEM,
                },
            ),
        ),
    )
    def test_returns_values_needed_for_making_a_prime_request(
        self,
        env: MilMoveEnv,
        endpoint: str,
        endpoint_name: str,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_prime_request(endpoint=endpoint, endpoint_name=endpoint_name) == (
            expected_path,
            expected_headers,
        )

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
        "env,endpoint,endpoint_name,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/move-task-orders",
                "",
                "https://primelocal:9443/support/v1/move-task-orders",
                {"headers": get_json_headers(), **deepcopy(LOCAL_TLS_CERT_KWARGS)},
            ),
            (
                MilMoveEnv.LOCAL,
                "/payment-requests/13/status",
                "/payment-requests/{paymentRequestID}/status",
                "https://primelocal:9443/support/v1/payment-requests/13/status",
                {
                    "name": "/support/v1/payment-requests/{paymentRequestID}/status",
                    "headers": get_json_headers(),
                    **deepcopy(LOCAL_TLS_CERT_KWARGS),
                },
            ),
            (
                MilMoveEnv.DP3,
                "/move-task-orders",
                "",
                "https://api.loadtest.dp3.us/support/v1/move-task-orders",
                {"headers": get_json_headers(), "cert": DP3_CERT_KEY_PEM},
            ),
            (
                MilMoveEnv.DP3,
                "/payment-requests/13/status",
                "/payment-requests/{paymentRequestID}/status",
                "https://api.loadtest.dp3.us/support/v1/payment-requests/13/status",
                {
                    "name": "/support/v1/payment-requests/{paymentRequestID}/status",
                    "headers": get_json_headers(),
                    "cert": DP3_CERT_KEY_PEM,
                },
            ),
        ),
    )
    def test_returns_values_needed_for_making_a_support_request(
        self,
        env: MilMoveEnv,
        endpoint: str,
        endpoint_name: str,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_support_request(endpoint=endpoint, endpoint_name=endpoint_name) == (
            expected_path,
            expected_headers,
        )


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
        # All task sets need to be initialized with a parent (user or another task set).
        mock_user = MagicMock()
        mock_user.host = user_host

        class SampleTaskSet(MilMoveRequestMixin, TaskSet):
            """
            User to use for unit tests
            """

            user = mock_user

        assert not hasattr(SampleTaskSet, "env")

        task_set = SampleTaskSet(parent=mock_user)

        assert hasattr(task_set, "env")

        assert task_set.env == env

    @pytest.mark.parametrize(
        "user_host,env",
        (
            ("local", MilMoveEnv.LOCAL),
            ("dp3", MilMoveEnv.DP3),
        ),
    )
    def test_sets_up_request_preparer_on_init(self, user_host: str, env: MilMoveEnv) -> None:
        # All task sets need to be initialized with a parent (user or another task set).
        mock_user = MagicMock()
        mock_user.host = user_host

        class SampleTaskSet(MilMoveRequestMixin, TaskSet):
            """
            User to use for unit tests
            """

            user = mock_user

        assert not hasattr(SampleTaskSet, "request_preparer")

        user = SampleTaskSet(parent=mock_user)

        assert hasattr(user, "request_preparer")

        assert user.request_preparer == MilMoveRequestPreparer(env=env)
