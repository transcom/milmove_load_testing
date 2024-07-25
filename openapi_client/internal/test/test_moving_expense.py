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
from internal_client.model.moving_expense_document import MovingExpenseDocument
from internal_client.model.omittable_moving_expense_type import OmittableMovingExpenseType
from internal_client.model.omittable_ppm_document_status import OmittablePPMDocumentStatus
from internal_client.model.submitted_moving_expense_type import SubmittedMovingExpenseType
globals()['MovingExpenseDocument'] = MovingExpenseDocument
globals()['OmittableMovingExpenseType'] = OmittableMovingExpenseType
globals()['OmittablePPMDocumentStatus'] = OmittablePPMDocumentStatus
globals()['SubmittedMovingExpenseType'] = SubmittedMovingExpenseType
from internal_client.model.moving_expense import MovingExpense


class TestMovingExpense(unittest.TestCase):
    """MovingExpense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMovingExpense(self):
        """Test MovingExpense"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MovingExpense()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
