"""
    Milmove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `primelocal/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.payment_request_status import PaymentRequestStatus
from prime_client.model.payment_service_items import PaymentServiceItems
from prime_client.model.proof_of_service_docs import ProofOfServiceDocs
globals()['PaymentRequestStatus'] = PaymentRequestStatus
globals()['PaymentServiceItems'] = PaymentServiceItems
globals()['ProofOfServiceDocs'] = ProofOfServiceDocs
from prime_client.model.payment_request import PaymentRequest


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