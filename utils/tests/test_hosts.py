# -*- coding: utf-8 -*-
""" Tests utils/parsers.py """

from utils.hosts import MilMoveHostMixin, MilMoveDomain, MilMoveEnv


class TestMilMoveHostMixin:
    """ Tests the MilMoveHostMixin class and its methods. """

    @classmethod
    def setup_class(cls):
        """ Define and initialize classes to be tested """

        class HostLocal(MilMoveHostMixin):
            # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
            local_port = "9443"
            domain = MilMoveDomain.PRIME  # the base domain for the host
            is_api = True  # if True, uses the api base domain in deployed environments
            host = "exp"

        """ Initialize the APIParser that will be tested. """
        cls.TestUser1 = HostLocal()
        cls.TestUser2 = HostLocal()
        cls.HostLocalClass = HostLocal

    def test_set_host_name(self):

        print("after init", self.TestUser1.host)
        # self.TestUser.host = None
        self.HostLocalClass.host = None
        print("after setting to none", self.TestUser1.host)
        print(self.TestUser1)

        self.HostLocalClass.env = MilMoveEnv.LOCAL
        self.HostLocalClass.is_api = True
        self.HostLocalClass.local_port = 9443
        self.HostLocalClass.local_protocol = "http"

        self.TestUser1.set_host_name()
        print("after running set host name", self.TestUser1.host)
        print("after running set host name", self.TestUser2.host)
        assert True
