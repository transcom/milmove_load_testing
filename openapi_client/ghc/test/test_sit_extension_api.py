"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.sit_extension_api import SitExtensionApi  # noqa: E501


class TestSitExtensionApi(unittest.TestCase):
    """SitExtensionApi unit test stubs"""

    def setUp(self):
        self.api = SitExtensionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_approve_sit_extension(self):
        """Test case for approve_sit_extension

        Approves a SIT extension  # noqa: E501
        """
        pass

    def test_create_approved_sit_duration_update(self):
        """Test case for create_approved_sit_duration_update

        Create an approved SIT Duration Update  # noqa: E501
        """
        pass

    def test_deny_sit_extension(self):
        """Test case for deny_sit_extension

        Denies a SIT extension  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
