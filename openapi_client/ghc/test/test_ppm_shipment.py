"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.ppm_shipment_status import PPMShipmentStatus
globals()['PPMShipmentStatus'] = PPMShipmentStatus
from ghc_client.model.ppm_shipment import PPMShipment


class TestPPMShipment(unittest.TestCase):
    """PPMShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPPMShipment(self):
        """Test PPMShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PPMShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
