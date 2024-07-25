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
from ghc_client.model.document import Document
from ghc_client.model.move_status import MoveStatus
from ghc_client.model.mto_shipments import MTOShipments
from ghc_client.model.transportation_office import TransportationOffice
globals()['Document'] = Document
globals()['MTOShipments'] = MTOShipments
globals()['MoveStatus'] = MoveStatus
globals()['TransportationOffice'] = TransportationOffice
from ghc_client.model.move_payload import MovePayload


class TestMovePayload(unittest.TestCase):
    """MovePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMovePayload(self):
        """Test MovePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MovePayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()