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
from ghc_client.model.mto_service_item_customer_contacts import MTOServiceItemCustomerContacts
from ghc_client.model.mto_service_item_dimensions import MTOServiceItemDimensions
from ghc_client.model.mto_service_item_status import MTOServiceItemStatus
from ghc_client.model.service_request_documents import ServiceRequestDocuments
from ghc_client.model.sit_address_updates import SITAddressUpdates
globals()['Address'] = Address
globals()['MTOServiceItemCustomerContacts'] = MTOServiceItemCustomerContacts
globals()['MTOServiceItemDimensions'] = MTOServiceItemDimensions
globals()['MTOServiceItemStatus'] = MTOServiceItemStatus
globals()['SITAddressUpdates'] = SITAddressUpdates
globals()['ServiceRequestDocuments'] = ServiceRequestDocuments
from ghc_client.model.mto_service_item import MTOServiceItem


class TestMTOServiceItem(unittest.TestCase):
    """MTOServiceItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOServiceItem(self):
        """Test MTOServiceItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOServiceItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
