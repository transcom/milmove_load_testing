"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.shipment_api import ShipmentApi  # noqa: E501


class TestShipmentApi(unittest.TestCase):
    """ShipmentApi unit test stubs"""

    def setUp(self):
        self.api = ShipmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_approve_shipment(self):
        """Test case for approve_shipment

        Approves a shipment  # noqa: E501
        """
        pass

    def test_approve_shipment_diversion(self):
        """Test case for approve_shipment_diversion

        Approves a shipment diversion  # noqa: E501
        """
        pass

    def test_approve_sit_extension(self):
        """Test case for approve_sit_extension

        Approves a SIT extension  # noqa: E501
        """
        pass

    def test_create_approved_sit_duration_update(self):
        """Test case for create_approved_sit_duration_update

        Create an approved SIT Duration Update  # noqa: E501
        """
        pass

    def test_delete_shipment(self):
        """Test case for delete_shipment

        Soft deletes a shipment by ID  # noqa: E501
        """
        pass

    def test_deny_sit_extension(self):
        """Test case for deny_sit_extension

        Denies a SIT extension  # noqa: E501
        """
        pass

    def test_reject_shipment(self):
        """Test case for reject_shipment

        rejects a shipment  # noqa: E501
        """
        pass

    def test_request_shipment_cancellation(self):
        """Test case for request_shipment_cancellation

        Requests a shipment cancellation  # noqa: E501
        """
        pass

    def test_request_shipment_diversion(self):
        """Test case for request_shipment_diversion

        Requests a shipment diversion  # noqa: E501
        """
        pass

    def test_request_shipment_reweigh(self):
        """Test case for request_shipment_reweigh

        Requests a shipment reweigh  # noqa: E501
        """
        pass

    def test_review_shipment_address_update(self):
        """Test case for review_shipment_address_update

        Allows TOO to review a shipment address update  # noqa: E501
        """
        pass

    def test_update_sit_service_item_customer_expense(self):
        """Test case for update_sit_service_item_customer_expense

        Converts a SIT to customer expense  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
