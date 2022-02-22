"""
    Milmove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `primelocal/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.address import Address
from prime_client.model.destination_type import DestinationType
from prime_client.model.mto_agents import MTOAgents
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.mto_shipment_type import MTOShipmentType
from prime_client.model.reweigh import Reweigh
from prime_client.model.sit_extensions import SITExtensions
from prime_client.model.storage_facility import StorageFacility
globals()['Address'] = Address
globals()['DestinationType'] = DestinationType
globals()['MTOAgents'] = MTOAgents
globals()['MTOServiceItem'] = MTOServiceItem
globals()['MTOShipmentType'] = MTOShipmentType
globals()['Reweigh'] = Reweigh
globals()['SITExtensions'] = SITExtensions
globals()['StorageFacility'] = StorageFacility
from prime_client.model.mto_shipment import MTOShipment


class TestMTOShipment(unittest.TestCase):
    """MTOShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOShipment(self):
        """Test MTOShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()