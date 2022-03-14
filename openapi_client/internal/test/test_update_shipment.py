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
from internal_client.model.address import Address
from internal_client.model.mto_agents import MTOAgents
from internal_client.model.mto_shipment_status import MTOShipmentStatus
from internal_client.model.mto_shipment_type import MTOShipmentType
from internal_client.model.update_ppm_shipment import UpdatePPMShipment
globals()['Address'] = Address
globals()['MTOAgents'] = MTOAgents
globals()['MTOShipmentStatus'] = MTOShipmentStatus
globals()['MTOShipmentType'] = MTOShipmentType
globals()['UpdatePPMShipment'] = UpdatePPMShipment
from internal_client.model.update_shipment import UpdateShipment


class TestUpdateShipment(unittest.TestCase):
    """UpdateShipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateShipment(self):
        """Test UpdateShipment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateShipment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
