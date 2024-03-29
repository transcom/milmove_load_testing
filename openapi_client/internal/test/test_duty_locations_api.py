"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.duty_locations_api import DutyLocationsApi  # noqa: E501


class TestDutyLocationsApi(unittest.TestCase):
    """DutyLocationsApi unit test stubs"""

    def setUp(self):
        self.api = DutyLocationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_duty_locations(self):
        """Test case for search_duty_locations

        Returns the duty locations matching the search query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
