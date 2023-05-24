"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.document import Document
from ghc_client.model.upload import Upload
globals()['Document'] = Document
globals()['Upload'] = Upload
from ghc_client.model.weight_ticket_proof_of_trailer_ownership_document import WeightTicketProofOfTrailerOwnershipDocument


class TestWeightTicketProofOfTrailerOwnershipDocument(unittest.TestCase):
    """WeightTicketProofOfTrailerOwnershipDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWeightTicketProofOfTrailerOwnershipDocument(self):
        """Test WeightTicketProofOfTrailerOwnershipDocument"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WeightTicketProofOfTrailerOwnershipDocument()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()