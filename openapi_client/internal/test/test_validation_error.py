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
from internal_client.model.client_error import ClientError
globals()['ClientError'] = ClientError
from internal_client.model.validation_error import ValidationError


class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidationError(self):
        """Test ValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ValidationError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
