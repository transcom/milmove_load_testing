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
from ghc_client.model.evaluation_report import EvaluationReport
globals()['EvaluationReport'] = EvaluationReport
from ghc_client.model.evaluation_report_list import EvaluationReportList


class TestEvaluationReportList(unittest.TestCase):
    """EvaluationReportList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvaluationReportList(self):
        """Test EvaluationReportList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EvaluationReportList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
