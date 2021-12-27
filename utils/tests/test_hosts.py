# -*- coding: utf-8 -*-
""" Tests utils/hosts.py """
import os
import re
from pathlib import Path
from unittest import mock

import pytest
from _pytest.monkeypatch import MonkeyPatch

from utils.base import ImplementationError
from utils.constants import DP3_CERT_KEY_PEM_FILENAME
from utils.hosts import MilMoveDomain, MilMoveEnv, MilMoveHostMixin, remove_certs, set_up_certs


class TestMilMoveDomain:
    """Tests the MilMoveDomain class and its methods."""

    def test_host_name(self):
        assert (
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name(env="local", port=1111, protocol="http")
            == "http://primelocal:1111"
        )

        assert MilMoveDomain.match(MilMoveDomain.PRIME).host_name(env="dp3") == "https://api.loadtest.dp3.us"

        with pytest.raises(ImplementationError):
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name(env="local", port=11111)

        with pytest.raises(ImplementationError):
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name(env="test")


class TestMilMoveHostMixin:
    """Tests the MilMoveHostMixin class and its methods."""

    @classmethod
    def setup_class(cls):
        """Define and initialize classes to be tested"""

        class HostUser(MilMoveHostMixin):
            # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
            local_port = "9443"
            domain = MilMoveDomain.PRIME  # the base domain for the host
            host = "local"

        cls.TestUser1 = HostUser()
        cls.TestUser2 = HostUser()
        cls.HostUserClass = HostUser

    def test__init__(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert self.TestUser1.env == MilMoveEnv.LOCAL
        assert self.TestUser1.host == "https://primelocal:9443"
        assert re.search("static/tls/devlocal-mtls.cer", self.TestUser1.cert_kwargs["cert"][0])
        assert re.search("static/tls/devlocal-mtls.key", self.TestUser1.cert_kwargs["cert"][1])

    def test_set_milmove_env(self):
        self.HostUserClass.env = None
        self.TestUser1.set_milmove_env("dp3")

        assert self.HostUserClass.env == MilMoveEnv.DP3
        assert self.TestUser1.env == MilMoveEnv.DP3
        assert self.TestUser2.env == MilMoveEnv.DP3

    def test_invalid_set_milmove_env(self):
        self.HostUserClass.env = None

        with pytest.raises(ImplementationError):
            self.TestUser1.set_milmove_env("test")

    def test_set_host_name(self):
        """
        Tests the host name for the class can be set using the class env
        and be called from a class instance
        """
        # reset all initally set values in class
        self.HostUserClass.host = None
        self.HostUserClass.env = MilMoveEnv.DP3

        # host is None due to setting the class host to None above
        assert self.TestUser1.host is None
        assert self.TestUser2.host is None

        self.TestUser1.set_host_name()
        assert self.TestUser1.host == "https://api.loadtest.dp3.us"
        assert self.TestUser2.host == "https://api.loadtest.dp3.us"

    @mock.patch.dict(os.environ, {"MOVE_MIL_DP3_TLS_CERT": "test_cert", "MOVE_MIL_DP3_TLS_KEY": "test_key"})
    def test_set_cert_kwargs(self):
        # Test if the environment is dp3
        self.HostUserClass.cert_kwargs = None
        self.TestUser1.set_cert_kwargs()

        assert re.search("tls/dp3_tls_cert_key.pem", self.TestUser1.cert_kwargs["cert"])
        assert re.search("tls/dp3_tls_cert_key.pem", self.TestUser2.cert_kwargs["cert"])

        # Test if the environment is local
        self.HostUserClass.cert_kwargs = None
        self.HostUserClass.env = MilMoveEnv.LOCAL
        self.TestUser1.set_cert_kwargs()

        assert re.search("tls/devlocal-mtls.cer", self.TestUser1.cert_kwargs["cert"][0])
        assert re.search("tls/devlocal-mtls.key", self.TestUser1.cert_kwargs["cert"][1])
        assert re.search("tls/devlocal-mtls.cer", self.TestUser2.cert_kwargs["cert"][0])
        assert re.search("tls/devlocal-mtls.key", self.TestUser2.cert_kwargs["cert"][1])


class TestSetUpCerts:
    """
    Tests for set_up_certs
    """

    def test_no_file_is_created_if_running_locally(self, tmp_path: Path) -> None:
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            set_up_certs(host=MilMoveEnv.LOCAL.value)

            assert len(list(tmp_path.iterdir())) == 0

    @pytest.mark.parametrize("tls_env_var", ["MOVE_MIL_DP3_TLS_CERT", "MOVE_MIL_DP3_TLS_KEY"])
    def test_missing_env_tls_var_raises_exception_for_deployed_host(
        self, tls_env_var: str, tmp_path: Path, monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.delenv(tls_env_var, raising=False)

        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            with pytest.raises(
                ImplementationError,
                match="Cannot run load testing in a deployed environment without the matching certificate and key.",
            ):

                set_up_certs(host=MilMoveEnv.DP3.value)

            assert len(list(tmp_path.iterdir())) == 0

    def test_cert_created_for_deployed_host_with_env_vars(self, tmp_path: Path, monkeypatch: MonkeyPatch):
        fake_cert = "fake cert"
        fake_key = "fake key"
        monkeypatch.setenv("MOVE_MIL_DP3_TLS_CERT", fake_cert)
        monkeypatch.setenv("MOVE_MIL_DP3_TLS_KEY", fake_key)

        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            set_up_certs(host=MilMoveEnv.DP3.value)

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

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(host=MilMoveEnv.LOCAL.value)

            assert len(list(tmp_path.iterdir())) == 1
            assert cert_key_pem.exists()

    def test_cert_removed_for_deployed_envs(self, tmp_path: Path):
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        cert_key_pem.touch()

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(host=MilMoveEnv.DP3.value)

            assert len(list(tmp_path.iterdir())) == 0

            assert not cert_key_pem.exists()

    def test_no_error_if_cert_already_gone(self, tmp_path: Path):
        cert_key_pem = tmp_path / DP3_CERT_KEY_PEM_FILENAME

        assert len(list(tmp_path.iterdir())) == 0

        with mock.patch("utils.hosts.DP3_CERT_KEY_PEM", cert_key_pem):
            remove_certs(host=MilMoveEnv.DP3.value)

            assert len(list(tmp_path.iterdir())) == 0

            assert not cert_key_pem.exists()
