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
from internal_client.model.move_document_payload import MoveDocumentPayload
globals()['MoveDocumentPayload'] = MoveDocumentPayload
from internal_client.model.move_documents import MoveDocuments


class TestMoveDocuments(unittest.TestCase):
    """MoveDocuments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMoveDocuments(self):
        """Test MoveDocuments"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MoveDocuments()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
