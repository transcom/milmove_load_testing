"""
    Milmove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `primelocal/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import prime_client
from prime_client.api.mto_shipment_api import MtoShipmentApi  # noqa: E501


class TestMtoShipmentApi(unittest.TestCase):
    """MtoShipmentApi unit test stubs"""

    def setUp(self):
        self.api = MtoShipmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mto_agent(self):
        """Test case for create_mto_agent

        createMTOAgent  # noqa: E501
        """
        pass

    def test_create_mto_shipment(self):
        """Test case for create_mto_shipment

        createMTOShipment  # noqa: E501
        """
        pass

    def test_create_sit_extension(self):
        """Test case for create_sit_extension

        createSITExtension  # noqa: E501
        """
        pass

    def test_update_mto_agent(self):
        """Test case for update_mto_agent

        updateMTOAgent  # noqa: E501
        """
        pass

    def test_update_mto_shipment(self):
        """Test case for update_mto_shipment

        updateMTOShipment  # noqa: E501
        """
        pass

    def test_update_mto_shipment_address(self):
        """Test case for update_mto_shipment_address

        updateMTOShipmentAddress  # noqa: E501
        """
        pass

    def test_update_mto_shipment_status(self):
        """Test case for update_mto_shipment_status

        updateMTOShipmentStatus  # noqa: E501
        """
        pass

    def test_update_reweigh(self):
        """Test case for update_reweigh

        updateReweigh  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()