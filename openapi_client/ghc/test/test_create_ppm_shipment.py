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
from ghc_client.model.sit_location_type import SITLocationType
globals()['SITLocationType'] = SITLocationType
from ghc_client.model.create_ppm_shipment import CreatePPMShipment


class TestCreatePPMShipment(unittest.TestCase):
    """CreatePPMShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreatePPMShipment(self):
        """Test CreatePPMShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreatePPMShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()