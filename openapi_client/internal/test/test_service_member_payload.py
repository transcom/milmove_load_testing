"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.address import Address
from internal_client.model.affiliation import Affiliation
from internal_client.model.index_service_member_backup_contacts_payload import IndexServiceMemberBackupContactsPayload
from internal_client.model.order_pay_grade import OrderPayGrade
from internal_client.model.orders import Orders
from internal_client.model.weight_allotment import WeightAllotment
globals()['Address'] = Address
globals()['Affiliation'] = Affiliation
globals()['IndexServiceMemberBackupContactsPayload'] = IndexServiceMemberBackupContactsPayload
globals()['OrderPayGrade'] = OrderPayGrade
globals()['Orders'] = Orders
globals()['WeightAllotment'] = WeightAllotment
from internal_client.model.service_member_payload import ServiceMemberPayload


class TestServiceMemberPayload(unittest.TestCase):
    """ServiceMemberPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceMemberPayload(self):
        """Test ServiceMemberPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceMemberPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
