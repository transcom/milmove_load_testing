"""
    my.move.mil

    The internal/website API for my.move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.uploads_api import UploadsApi  # noqa: E501


class TestUploadsApi(unittest.TestCase):
    """UploadsApi unit test stubs"""

    def setUp(self):
        self.api = UploadsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_upload(self):
        """Test case for create_upload

        Create a new upload  # noqa: E501
        """
        pass

    def test_delete_upload(self):
        """Test case for delete_upload

        Deletes an upload  # noqa: E501
        """
        pass

    def test_delete_uploads(self):
        """Test case for delete_uploads

        Deletes a collection of uploads  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
