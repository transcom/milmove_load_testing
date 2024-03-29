"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import prime_client
from prime_client.api.sit_address_update_api import SitAddressUpdateApi  # noqa: E501


class TestSitAddressUpdateApi(unittest.TestCase):
    """SitAddressUpdateApi unit test stubs"""

    def setUp(self):
        self.api = SitAddressUpdateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sit_address_update_request(self):
        """Test case for create_sit_address_update_request

        createSITAddressUpdateRequest  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
