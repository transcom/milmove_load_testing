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
from internal_client.model.omittable_ppm_document_status import OmittablePPMDocumentStatus
from internal_client.model.weight_ticket_empty_document import WeightTicketEmptyDocument
from internal_client.model.weight_ticket_full_document import WeightTicketFullDocument
from internal_client.model.weight_ticket_proof_of_trailer_ownership_document import WeightTicketProofOfTrailerOwnershipDocument
globals()['OmittablePPMDocumentStatus'] = OmittablePPMDocumentStatus
globals()['WeightTicketEmptyDocument'] = WeightTicketEmptyDocument
globals()['WeightTicketFullDocument'] = WeightTicketFullDocument
globals()['WeightTicketProofOfTrailerOwnershipDocument'] = WeightTicketProofOfTrailerOwnershipDocument
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
