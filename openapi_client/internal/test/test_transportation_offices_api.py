"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.transportation_offices_api import TransportationOfficesApi  # noqa: E501


class TestTransportationOfficesApi(unittest.TestCase):
    """TransportationOfficesApi unit test stubs"""

    def setUp(self):
        self.api = TransportationOfficesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transportation_offices(self):
        """Test case for get_transportation_offices

        Returns the transportation offices matching the search query  # noqa: E501
        """
        pass

    def test_show_duty_location_transportation_office(self):
        """Test case for show_duty_location_transportation_office

        Returns the transportation office for a given duty location  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
