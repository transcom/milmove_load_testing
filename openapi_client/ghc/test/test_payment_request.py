"""
    move.mil API

    The API for move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.move import Move
from ghc_client.model.payment_request_status import PaymentRequestStatus
from ghc_client.model.payment_service_items import PaymentServiceItems
from ghc_client.model.proof_of_service_docs import ProofOfServiceDocs
globals()['Move'] = Move
globals()['PaymentRequestStatus'] = PaymentRequestStatus
globals()['PaymentServiceItems'] = PaymentServiceItems
globals()['ProofOfServiceDocs'] = ProofOfServiceDocs
from ghc_client.model.payment_request import PaymentRequest


class TestPaymentRequest(unittest.TestCase):
    """PaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentRequest(self):
        """Test PaymentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()