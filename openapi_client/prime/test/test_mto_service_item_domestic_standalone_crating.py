"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.mto_service_item_domestic_standalone_crating_all_of import MTOServiceItemDomesticStandaloneCratingAllOf
from prime_client.model.mto_service_item_model_type import MTOServiceItemModelType
from prime_client.model.mto_service_item_status import MTOServiceItemStatus
from prime_client.model.service_request_documents import ServiceRequestDocuments
globals()['MTOServiceItem'] = MTOServiceItem
globals()['MTOServiceItemDomesticStandaloneCratingAllOf'] = MTOServiceItemDomesticStandaloneCratingAllOf
globals()['MTOServiceItemModelType'] = MTOServiceItemModelType
globals()['MTOServiceItemStatus'] = MTOServiceItemStatus
globals()['ServiceRequestDocuments'] = ServiceRequestDocuments
from prime_client.model.mto_service_item_domestic_standalone_crating import MTOServiceItemDomesticStandaloneCrating


class TestMTOServiceItemDomesticStandaloneCrating(unittest.TestCase):
    """MTOServiceItemDomesticStandaloneCrating unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOServiceItemDomesticStandaloneCrating(self):
        """Test MTOServiceItemDomesticStandaloneCrating"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOServiceItemDomesticStandaloneCrating()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
