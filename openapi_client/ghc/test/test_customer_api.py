"""
    move.mil API

    The API for move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.customer_api import CustomerApi  # noqa: E501


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_customer(self):
        """Test case for get_customer

        Returns a given customer  # noqa: E501
        """
        pass

    def test_update_customer(self):
        """Test case for update_customer

        Updates customer info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
