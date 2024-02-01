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
from ghc_client.model.address import Address
from ghc_client.model.shipment_address_update_status import ShipmentAddressUpdateStatus
globals()['Address'] = Address
globals()['ShipmentAddressUpdateStatus'] = ShipmentAddressUpdateStatus
from ghc_client.model.shipment_address_update import ShipmentAddressUpdate


class TestShipmentAddressUpdate(unittest.TestCase):
    """ShipmentAddressUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testShipmentAddressUpdate(self):
        """Test ShipmentAddressUpdate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ShipmentAddressUpdate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()