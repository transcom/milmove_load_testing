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
from internal_client.model.dept_indicator import DeptIndicator
from internal_client.model.orders_type import OrdersType
from internal_client.model.orders_type_detail import OrdersTypeDetail
globals()['DeptIndicator'] = DeptIndicator
globals()['OrdersType'] = OrdersType
globals()['OrdersTypeDetail'] = OrdersTypeDetail
from internal_client.model.create_update_orders import CreateUpdateOrders


class TestCreateUpdateOrders(unittest.TestCase):
    """CreateUpdateOrders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateUpdateOrders(self):
        """Test CreateUpdateOrders"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateUpdateOrders()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
