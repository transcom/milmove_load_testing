"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.move_status import MoveStatus
from internal_client.model.mto_shipments import MTOShipments
from internal_client.model.transportation_office import TransportationOffice
globals()['MTOShipments'] = MTOShipments
globals()['MoveStatus'] = MoveStatus
globals()['TransportationOffice'] = TransportationOffice
from internal_client.model.move_payload import MovePayload


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
