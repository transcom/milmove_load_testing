"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.mto_service_item_model_type import MTOServiceItemModelType
from prime_client.model.mto_service_item_shuttle_all_of import MTOServiceItemShuttleAllOf
from prime_client.model.mto_service_item_status import MTOServiceItemStatus
from prime_client.model.service_request_documents import ServiceRequestDocuments
globals()['MTOServiceItem'] = MTOServiceItem
globals()['MTOServiceItemModelType'] = MTOServiceItemModelType
globals()['MTOServiceItemShuttleAllOf'] = MTOServiceItemShuttleAllOf
globals()['MTOServiceItemStatus'] = MTOServiceItemStatus
globals()['ServiceRequestDocuments'] = ServiceRequestDocuments
from prime_client.model.mto_service_item_shuttle import MTOServiceItemShuttle


class TestMTOServiceItemShuttle(unittest.TestCase):
    """MTOServiceItemShuttle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOServiceItemShuttle(self):
        """Test MTOServiceItemShuttle"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOServiceItemShuttle()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
