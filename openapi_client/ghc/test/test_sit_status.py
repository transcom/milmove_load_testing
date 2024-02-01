"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.mto_service_items import MTOServiceItems
from ghc_client.model.sit_status_current_sit import SITStatusCurrentSIT
globals()['MTOServiceItems'] = MTOServiceItems
globals()['SITStatusCurrentSIT'] = SITStatusCurrentSIT
from ghc_client.model.sit_status import SITStatus


class TestSITStatus(unittest.TestCase):
    """SITStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSITStatus(self):
        """Test SITStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SITStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
