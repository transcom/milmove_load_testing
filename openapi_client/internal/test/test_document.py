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
from internal_client.model.upload import Upload
globals()['Upload'] = Upload
from internal_client.model.document import Document


class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDocument(self):
        """Test Document"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Document()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
