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
from internal_client.model.transportation_office import TransportationOffice
globals()['TransportationOffice'] = TransportationOffice
from internal_client.model.transportation_offices import TransportationOffices


class TestTransportationOffices(unittest.TestCase):
    """TransportationOffices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransportationOffices(self):
        """Test TransportationOffices"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransportationOffices()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()