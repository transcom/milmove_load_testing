"""
    my.move.mil

    The internal/website API for my.move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import internal_client
from internal_client.model.selected_move_type import SelectedMoveType
globals()['SelectedMoveType'] = SelectedMoveType
from internal_client.model.patch_move_payload import PatchMovePayload


class TestPatchMovePayload(unittest.TestCase):
    """PatchMovePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchMovePayload(self):
        """Test PatchMovePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchMovePayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
