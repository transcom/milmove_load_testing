# -*- coding: utf-8 -*-
""" Tests utils/hosts.py """
import re
import pytest
import os
from unittest import mock
import logging

from locust.env import Environment

from utils.hosts import MilMoveHostMixin, MilMoveDomain, MilMoveEnv, clean_milmove_host_users
from utils.base import ImplementationError


class TestMilMoveDomain:
    """Tests the MilMoveDomain class and its methods."""

    def test_host_name(self):
        assert (
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name("local", True, 1111, "http") == "http://primelocal:1111"
        )
        assert MilMoveDomain.match(MilMoveDomain.PRIME).host_name("exp") == "https://prime.exp.move.mil"

        with pytest.raises(ImplementationError):
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name("local", True, 11111)

        with pytest.raises(ImplementationError):
            MilMoveDomain.match(MilMoveDomain.PRIME).host_name("test")


class TestMilMoveHostMixin:
    """Tests the MilMoveHostMixin class and its methods."""

    @classmethod
    def setup_class(cls):
        """Define and initialize classes to be tested"""

        class HostUser(MilMoveHostMixin):
            # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
            local_port = "9443"
            domain = MilMoveDomain.PRIME  # the base domain for the host
            is_api = True  # if True, uses the api base domain in deployed environments
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
        self.TestUser1.set_milmove_env("exp")

        assert self.HostUserClass.env == MilMoveEnv.EXP
        assert self.TestUser1.env == MilMoveEnv.EXP
        assert self.TestUser2.env == MilMoveEnv.EXP

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
        self.HostUserClass.env = MilMoveEnv.EXP

        # host is None due to setting the class host to None above
        assert self.TestUser1.host is None
        assert self.TestUser2.host is None

        self.TestUser1.set_host_name()
        assert self.TestUser1.host == "https://api.exp.move.mil"
        assert self.TestUser2.host == "https://api.exp.move.mil"

    @mock.patch.dict(os.environ, {"MOVE_MIL_EXP_TLS_CERT": "test_cert", "MOVE_MIL_EXP_TLS_KEY": "test_key"})
    def test_set_cert_kwargs(self):
        # Test if the environment is experimental
        self.HostUserClass.cert_kwargs = None
        self.TestUser1.set_cert_kwargs()

        assert re.search("tls/exp_tls_cert_key.pem", self.TestUser1.cert_kwargs["cert"])
        assert re.search("tls/dod-ca-60-61-bundle.pem", self.TestUser1.cert_kwargs["verify"])
        assert re.search("tls/exp_tls_cert_key.pem", self.TestUser2.cert_kwargs["cert"])
        assert re.search("tls/dod-ca-60-61-bundle.pem", self.TestUser2.cert_kwargs["verify"])

        # Test if the environment is local
        self.HostUserClass.cert_kwargs = None
        self.HostUserClass.env = MilMoveEnv.LOCAL
        self.TestUser1.set_cert_kwargs()

        assert re.search("tls/devlocal-mtls.cer", self.TestUser1.cert_kwargs["cert"][0])
        assert re.search("tls/devlocal-mtls.key", self.TestUser1.cert_kwargs["cert"][1])
        assert re.search("tls/devlocal-mtls.cer", self.TestUser2.cert_kwargs["cert"][0])
        assert re.search("tls/devlocal-mtls.key", self.TestUser2.cert_kwargs["cert"][1])

    @mock.patch.dict(os.environ, {"MOVE_MIL_EXP_TLS_CERT": "test_cert", "MOVE_MIL_EXP_TLS_KEY": "test_key"})
    def test_create_deployed_cert_file(self):
        self.HostUserClass.env = MilMoveEnv.EXP
        cert_file_path = self.TestUser1.create_deployed_cert_file()
        test_file_contents = "test_cert\ntest_key"

        assert re.search("tls/exp_tls_cert_key.pem", cert_file_path)
        with open(cert_file_path, "r") as f:
            assert f.read() == test_file_contents

    @mock.patch.dict(os.environ, {"MOVE_MIL_EXP_TLS_CERT": "", "MOVE_MIL_EXP_TLS_KEY": ""})
    def test_no_env_variables_create_deployed_cert_file(self):
        self.HostUserClass.env = MilMoveEnv.EXP
        with pytest.raises(ImplementationError):
            self.TestUser1.create_deployed_cert_file()

    @mock.patch.dict(os.environ, {"MOVE_MIL_EXP_TLS_CERT": "test_cert", "MOVE_MIL_EXP_TLS_KEY": "test_key"})
    def test_remove_deployed_cert_file(self):
        # Setup kwargs
        self.HostUserClass.env = MilMoveEnv.EXP
        self.HostUserClass.cert_kwargs = None
        self.TestUser1.set_cert_kwargs()
        cert_kwargs_before = self.TestUser1.cert_kwargs["cert"]

        self.TestUser1.remove_deployed_cert_file()
        assert os.path.exists(cert_kwargs_before) is False
        assert self.TestUser1.cert_kwargs == {}
        assert self.TestUser2.cert_kwargs == {}

        # Call function again to make sure it doesn't error
        self.TestUser1.remove_deployed_cert_file()


@mock.patch.dict(os.environ, {"MOVE_MIL_EXP_TLS_CERT": "test_cert", "MOVE_MIL_EXP_TLS_KEY": "test_key"})
def test_clean_milmove_host_users(mocker):
    # tasks.base logger for mocking
    logger = logging.getLogger("utils.hosts")

    class MockUser(MilMoveHostMixin):
        local_port = "9443"
        domain = MilMoveDomain.PRIME
        is_api = True
        host = "exp"
        tasks = {}

    env = Environment(user_classes=[MockUser])
    TestUser = MockUser()
    TestUser.create_deployed_cert_file()

    mocker.patch.object(logger, "info")
    clean_milmove_host_users(locust_env=env)
    assert TestUser.cert_kwargs == {}
    logger.info.assert_called_once_with("Cleaned up User SSL/TLS certificates.")
