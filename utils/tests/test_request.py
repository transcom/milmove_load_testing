# -*- coding: utf-8 -*-
"""
Tests for utils/request.py
"""
import os
from copy import deepcopy
from unittest.mock import MagicMock, create_autospec, patch

import pytest
from locust import TaskSet
from requests import PreparedRequest, Response

from utils.base import ImplementationError, MilMoveEnv
from utils.constants import DP3_CERT_KEY_PEM, LOCAL_TLS_CERT_KWARGS
from utils.request import (
    MilMoveRequestMixin,
    MilMoveRequestPreparer,
    format_request_display_message,
    format_response_display_message,
    log_response_failure,
    log_response_info,
)
from utils.rest import RestResponseContextManager, get_json_headers
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
        "env,endpoint,include_prefix,expected_path",
        (
            (MilMoveEnv.LOCAL, "/moves", True, "http://officelocal:8080/ghc/v1/moves"),
            (MilMoveEnv.LOCAL, "/internal/users/logged_in", False, "http://officelocal:8080/internal/users/logged_in"),
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
        env: MilMoveEnv,
        endpoint: str,
        include_prefix: bool,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_ghc_path(endpoint=endpoint, include_prefix=include_prefix) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,endpoint_name,include_prefix,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/queues/moves",
                "",
                True,
                "http://officelocal:8080/ghc/v1/queues/moves",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/internal/users/logged_in",
                "",
                False,
                "http://officelocal:8080/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/queues/counseling",
                "",
                True,
                "http://officelocal:8080/ghc/v1/queues/counseling",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/move/1",
                "/move/{locator}",
                True,
                "http://officelocal:8080/ghc/v1/move/1",
                {"name": "/ghc/v1/move/{locator}", "headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/queues/moves",
                "",
                True,
                "https://office.loadtest.dp3.us/ghc/v1/queues/moves",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/internal/users/logged_in",
                "",
                False,
                "https://office.loadtest.dp3.us/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/move/1",
                "/move/{locator}",
                True,
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
        include_prefix: bool,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_ghc_request(
            endpoint=endpoint, endpoint_name=endpoint_name, include_prefix=include_prefix
        ) == (
            expected_path,
            expected_headers,
        )

    @pytest.mark.parametrize(
        "env,endpoint,include_prefix,expected_path",
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
        env: MilMoveEnv,
        endpoint: str,
        include_prefix: bool,
        expected_path: str,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.form_internal_path(endpoint=endpoint, include_prefix=include_prefix) == expected_path

    @pytest.mark.parametrize(
        "env,endpoint,endpoint_name,include_prefix,expected_path,expected_headers",
        (
            (
                MilMoveEnv.LOCAL,
                "/users/logged_in",
                "",
                True,
                "http://milmovelocal:8080/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/devlocal-auth/login",
                "",
                False,
                "http://milmovelocal:8080/devlocal-auth/login",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/mto_shipments",
                "",
                True,
                "http://milmovelocal:8080/internal/mto_shipments",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.LOCAL,
                "/service_members/4",
                "/service_members/{serviceMemberId}",
                True,
                "http://milmovelocal:8080/internal/service_members/4",
                {"name": "/internal/service_members/{serviceMemberId}", "headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/users/logged_in",
                "",
                True,
                "https://my.loadtest.dp3.us/internal/users/logged_in",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/devlocal-auth/login",
                "",
                False,
                "https://my.loadtest.dp3.us/devlocal-auth/login",
                {"headers": get_json_headers()},
            ),
            (
                MilMoveEnv.DP3,
                "/service_members/4",
                "/service_members/{serviceMemberId}",
                True,
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
        include_prefix: bool,
        expected_path: str,
        expected_headers: RequestKwargsType,
    ) -> None:
        request_preparer = MilMoveRequestPreparer(env=env)

        assert request_preparer.prep_internal_request(
            endpoint=endpoint, endpoint_name=endpoint_name, include_prefix=include_prefix
        ) == (
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


@patch("utils.request.logger", autospec=True)
class TestLogResponseInfo:
    """
    Tests for log_response_info
    """

    def test_defaults_to_include_calling_function_name_in_log(self, mock_logger: MagicMock) -> None:
        mock_response = create_autospec(Response)
        mock_response.status_code = 200
        mock_response.reason = ""

        log_response_info(response=mock_response)

        mock_logger.info.assert_called_once()

        assert "test_defaults_to_include_calling_function_name_in_log" in mock_logger.info.call_args[0][0]

    def test_can_override_task_name_in_log(self, mock_logger: MagicMock) -> None:
        mock_response = create_autospec(Response)
        mock_response.status_code = 200
        mock_response.reason = ""

        task_name = "my_task"
        log_response_info(response=mock_response, task_name=task_name)

        mock_logger.info.assert_called_once()

        assert task_name in mock_logger.info.call_args[0][0]
        assert "test_can_override_task_name_in_log" not in mock_logger.info.call_args[0][0]

    def test_includes_status_code_in_log(self, mock_logger: MagicMock) -> None:
        mock_response = create_autospec(Response)
        mock_response.status_code = 200
        mock_response.reason = ""

        log_response_info(response=mock_response)

        mock_logger.info.assert_called_once()

        assert str(mock_response.status_code) in mock_logger.info.call_args[0][0]

    def test_includes_reason_in_log(self, mock_logger: MagicMock) -> None:
        mock_response = create_autospec(Response)
        mock_response.status_code = 500
        mock_response.reason = "Server Error"

        log_response_info(response=mock_response)

        mock_logger.info.assert_called_once()

        assert mock_response.reason in mock_logger.info.call_args[0][0]


class TestFormatResponseDisplayMessage:
    """
    Tests for format_response_display_message
    """

    def test_indicates_if_no_content_found(self) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.js = ""

        msg = format_response_display_message(response=mock_response)

        assert "No content found." in msg

    def test_includes_js_content(self) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.js = {"moveID": "123"}

        msg = format_response_display_message(response=mock_response)

        assert '"moveID": "123"' in msg

    @patch("utils.request.parse_response_json")
    def test_parses_response_content_to_json_if_not_already_parsed(self, mock_parse_response_json: MagicMock) -> None:
        mock_parse_response_json.return_value = ({"moveID": "123"}, "")

        mock_response = create_autospec(Response)

        msg = format_response_display_message(response=mock_response)

        mock_parse_response_json.assert_called_once_with(response=mock_response)

        assert '"moveID": "123"' in msg

    @patch("utils.request.parse_response_json")
    def test_if_parses_response_content_to_json_fails_then_msg_includes_failure(
        self, mock_parse_response_json: MagicMock
    ) -> None:
        fail_msg = "Response content not parsable to JSON."
        mock_parse_response_json.return_value = ({}, fail_msg)

        mock_response = create_autospec(Response)

        msg = format_response_display_message(response=mock_response)

        mock_parse_response_json.assert_called_once_with(response=mock_response)

        assert fail_msg in msg


class TestFormatRequestDisplayMessage:
    """
    Tests for format_request_display_message
    """

    def test_indicates_if_no_content_found(self) -> None:
        mock_request = create_autospec(PreparedRequest)
        mock_request.method = "GET"
        mock_request.url = "http://milmovelocal:8080/internal/users/logged_in"
        mock_request.body = ""

        msg = format_request_display_message(request=mock_request)

        assert mock_request.method in msg
        assert mock_request.url in msg
        assert "No content found." in msg

    @patch("utils.request.json", autospec=True)
    def test_request_body_is_parsed_using_json(self, mock_json: MagicMock) -> None:
        mock_request = create_autospec(PreparedRequest)
        mock_request.method = "GET"
        mock_request.url = "http://milmovelocal:8080/internal/users/logged_in"
        mock_request.body = '{"moveID": "123"}'

        msg = format_request_display_message(request=mock_request)

        assert mock_request.method in msg
        assert mock_request.url in msg

        mock_json.loads.assert_called_once_with(mock_request.body)
        mock_json.dumps.assert_called_once_with(mock_json.loads.return_value, indent=4)

    def test_if_invalid_request_body_includes_msg_indicating_that_and_raw_body(self) -> None:
        mock_request = create_autospec(PreparedRequest)
        mock_request.method = "GET"
        mock_request.url = "http://milmovelocal:8080/internal/users/logged_in"
        mock_request.body = '{"moveID": "123"'  # missing closing curly bracket on purpose

        msg = format_request_display_message(request=mock_request)

        assert mock_request.method in msg
        assert mock_request.url in msg
        assert "Error parsing body" in msg
        assert mock_request.body in msg

    @patch("utils.request.json", autospec=True)
    def test_if_json_cant_be_dumped_then_includes_msg_with_raw_body(self, mock_json: MagicMock) -> None:
        mock_request = create_autospec(PreparedRequest)
        mock_request.method = "GET"
        mock_request.url = "http://milmovelocal:8080/internal/users/logged_in"
        mock_request.body = '{"moveID": "123"}'

        mock_json.dumps.side_effect = TypeError("Bad json!")  # faking out the error

        msg = format_request_display_message(request=mock_request)

        assert mock_request.method in msg
        assert mock_request.url in msg
        assert "Error parsing body" in msg
        assert mock_request.body in msg

    @patch("utils.request.json", autospec=True)
    def test_includes_parsed_response_body_in_msg(self, mock_json: MagicMock) -> None:
        mock_request = create_autospec(PreparedRequest)
        mock_request.method = "GET"
        mock_request.url = "http://milmovelocal:8080/internal/users/logged_in"
        mock_request.body = '{"moveID": "123"}'

        msg = format_request_display_message(request=mock_request)

        assert mock_request.method in msg
        assert mock_request.url in msg

        assert str(mock_json.dumps.return_value) in msg


@patch("utils.request.format_response_display_message", autospec=True)
@patch("utils.request.format_request_display_message", autospec=True)
@patch("utils.request.logger", autospec=True)
class TestLogResponseFailure:
    """
    Tests for log_response_failure
    """

    def test_defaults_to_include_calling_function_name_in_log(
        self, mock_logger: MagicMock, _mock_request_formatter: MagicMock, _mock_response_formatter: MagicMock
    ) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.request = create_autospec(PreparedRequest)

        log_response_failure(response=mock_response)

        mock_logger.error.assert_called_once()

        assert "test_defaults_to_include_calling_function_name_in_log failed" in mock_logger.error.call_args[0][0]

    def test_can_override_task_name_in_log(
        self, mock_logger: MagicMock, _mock_request_formatter: MagicMock, _mock_response_formatter: MagicMock
    ) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.request = create_autospec(PreparedRequest)

        task_name = "my_task"
        log_response_failure(response=mock_response, task_name=task_name)

        mock_logger.error.assert_called_once()

        assert f"{task_name} failed" in mock_logger.error.call_args[0][0]
        assert "test_can_override_task_name_in_log" not in mock_logger.error.call_args[0][0]

    def test_includes_formatted_response_in_log(
        self, mock_logger: MagicMock, _mock_request_formatter: MagicMock, mock_response_formatter: MagicMock
    ) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.request = create_autospec(PreparedRequest)

        log_response_failure(response=mock_response)

        mock_logger.error.assert_called_once()

        assert str(mock_response_formatter.return_value) in mock_logger.error.call_args[0][0]

    def test_includes_formatted_request_in_log(
        self, mock_logger: MagicMock, mock_request_formatter: MagicMock, _mock_response_formatter: MagicMock
    ) -> None:
        mock_response = create_autospec(RestResponseContextManager)
        mock_response.request = create_autospec(PreparedRequest)

        log_response_failure(response=mock_response)

        mock_logger.error.assert_called_once()

        assert str(mock_request_formatter.return_value) in mock_logger.error.call_args[0][0]
