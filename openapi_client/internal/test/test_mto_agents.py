"""
    my.move.mil

    The internal/website API for my.move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.mto_agent import MTOAgent
globals()['MTOAgent'] = MTOAgent
from internal_client.model.mto_agents import MTOAgents


class TestMTOAgents(unittest.TestCase):
    """MTOAgents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOAgents(self):
        """Test MTOAgents"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOAgents()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
