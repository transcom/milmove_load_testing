# -*- coding: utf-8 -*-
"""
Tests for utils/auth.py
"""
from pathlib import Path
from unittest import mock

import pytest
from _pytest.monkeypatch import MonkeyPatch

from utils.auth import remove_certs, set_up_certs
from utils.base import ImplementationError, MilMoveEnv
from utils.constants import DP3_CERT_KEY_PEM_FILENAME


class TestSetUpCerts:
    """
    Tests for set_up_certs
    """

    def test_no_file_is_created_if_running_locally(self, tmp_path: Path) -> None:
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", str(cert_key_pem)):
            set_up_certs(env=MilMoveEnv.LOCAL)

            assert len(list(tmp_path.iterdir())) == 0

    @pytest.mark.parametrize("tls_env_var", ["MOVE_MIL_DP3_TLS_CERT", "MOVE_MIL_DP3_TLS_KEY"])
    def test_missing_env_tls_var_raises_exception_for_deployed_host(
        self, tls_env_var: str, tmp_path: Path, monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.delenv(tls_env_var, raising=False)

        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", str(cert_key_pem)):
            with pytest.raises(
                ImplementationError,
                match="Cannot run load testing in a deployed environment without the matching certificate and key.",
            ):
                set_up_certs(env=MilMoveEnv.DP3)

            assert len(list(tmp_path.iterdir())) == 0

            assert not cert_key_pem.exists()

    def test_cert_created_for_deployed_host_with_env_vars(self, tmp_path: Path, monkeypatch: MonkeyPatch):
        fake_cert = "fake cert"
        fake_key = "fake key"
        monkeypatch.setenv("MOVE_MIL_DP3_TLS_CERT", fake_cert)
        monkeypatch.setenv("MOVE_MIL_DP3_TLS_KEY", fake_key)

        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", str(cert_key_pem)):
            set_up_certs(env=MilMoveEnv.DP3)

            assert len(list(tmp_path.iterdir())) == 1

            assert cert_key_pem.exists()

            assert f"{fake_cert}\n{fake_key}" == cert_key_pem.read_text()


class TestRemoveCerts:
    """
    Tests for remove_certs
    """

    def test_no_file_is_removed_if_running_locally(self, tmp_path: Path) -> None:
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        cert_key_pem.touch()  # creating it just so that we can test that it won't get removed

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(env=MilMoveEnv.LOCAL)

            assert len(list(tmp_path.iterdir())) == 1
            assert cert_key_pem.exists()

    def test_cert_removed_for_deployed_envs(self, tmp_path: Path):
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        cert_key_pem.touch()

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(env=MilMoveEnv.DP3)

            assert len(list(tmp_path.iterdir())) == 0

            assert not cert_key_pem.exists()

    def test_no_error_if_cert_already_gone(self, tmp_path: Path):
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        assert len(list(tmp_path.iterdir())) == 0

        with mock.patch("utils.auth.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(env=MilMoveEnv.DP3)

            assert len(list(tmp_path.iterdir())) == 0

            assert not cert_key_pem.exists()
