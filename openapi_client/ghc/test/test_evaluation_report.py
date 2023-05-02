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
from ghc_client.model.evaluation_report_inspection_type import EvaluationReportInspectionType
from ghc_client.model.evaluation_report_location import EvaluationReportLocation
from ghc_client.model.evaluation_report_office_user import EvaluationReportOfficeUser
from ghc_client.model.evaluation_report_type import EvaluationReportType
from ghc_client.model.report_violations import ReportViolations
globals()['EvaluationReportInspectionType'] = EvaluationReportInspectionType
globals()['EvaluationReportLocation'] = EvaluationReportLocation
globals()['EvaluationReportOfficeUser'] = EvaluationReportOfficeUser
globals()['EvaluationReportType'] = EvaluationReportType
globals()['ReportViolations'] = ReportViolations
from ghc_client.model.evaluation_report import EvaluationReport


class TestEvaluationReport(unittest.TestCase):
    """EvaluationReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvaluationReport(self):
        """Test EvaluationReport"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EvaluationReport()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()