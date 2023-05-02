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
from internal_client.model.document import Document
from internal_client.model.omittable_ppm_document_status import OmittablePPMDocumentStatus
globals()['Document'] = Document
globals()['OmittablePPMDocumentStatus'] = OmittablePPMDocumentStatus
from internal_client.model.weight_ticket import WeightTicket


class TestWeightTicket(unittest.TestCase):
    """WeightTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWeightTicket(self):
        """Test WeightTicket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WeightTicket()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()