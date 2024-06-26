"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.ppm_api import PpmApi  # noqa: E501


class TestPpmApi(unittest.TestCase):
    """PpmApi unit test stubs"""

    def setUp(self):
        self.api = PpmApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_moving_expense(self):
        """Test case for create_moving_expense

        Creates moving expense document  # noqa: E501
        """
        pass

    def test_create_ppm_upload(self):
        """Test case for create_ppm_upload

        Create a new upload for a PPM weight ticket, pro-gear, or moving expense document  # noqa: E501
        """
        pass

    def test_create_pro_gear_weight_ticket(self):
        """Test case for create_pro_gear_weight_ticket

        Creates a pro-gear weight ticket  # noqa: E501
        """
        pass

    def test_create_weight_ticket(self):
        """Test case for create_weight_ticket

        Creates a weight ticket document  # noqa: E501
        """
        pass

    def test_delete_moving_expense(self):
        """Test case for delete_moving_expense

        Soft deletes a moving expense by ID  # noqa: E501
        """
        pass

    def test_delete_pro_gear_weight_ticket(self):
        """Test case for delete_pro_gear_weight_ticket

        Soft deletes a pro-gear weight line item by ID  # noqa: E501
        """
        pass

    def test_delete_weight_ticket(self):
        """Test case for delete_weight_ticket

        Soft deletes a weight ticket by ID  # noqa: E501
        """
        pass

    def test_resubmit_ppm_shipment_documentation(self):
        """Test case for resubmit_ppm_shipment_documentation

        Updates signature and routes PPM shipment to service counselor  # noqa: E501
        """
        pass

    def test_show_aoa_packet(self):
        """Test case for show_aoa_packet

        Downloads AOA Packet form PPMShipment as a PDF  # noqa: E501
        """
        pass

    def test_show_payment_packet(self):
        """Test case for show_payment_packet

        Returns PPM payment packet  # noqa: E501
        """
        pass

    def test_submit_ppm_shipment_documentation(self):
        """Test case for submit_ppm_shipment_documentation

        Saves signature and routes PPM shipment to service counselor  # noqa: E501
        """
        pass

    def test_update_moving_expense(self):
        """Test case for update_moving_expense

        Updates the moving expense  # noqa: E501
        """
        pass

    def test_update_pro_gear_weight_ticket(self):
        """Test case for update_pro_gear_weight_ticket

        Updates a pro-gear weight ticket  # noqa: E501
        """
        pass

    def test_update_weight_ticket(self):
        """Test case for update_weight_ticket

        Updates a weight ticket document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
