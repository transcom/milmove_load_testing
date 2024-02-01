"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.document import Document
from ghc_client.model.upload import Upload
globals()['Document'] = Document
globals()['Upload'] = Upload
from ghc_client.model.weight_ticket_empty_document import WeightTicketEmptyDocument


class TestWeightTicketEmptyDocument(unittest.TestCase):
    """WeightTicketEmptyDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWeightTicketEmptyDocument(self):
        """Test WeightTicketEmptyDocument"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WeightTicketEmptyDocument()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
