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
from ghc_client.model.customer import Customer
from ghc_client.model.dept_indicator import DeptIndicator
from ghc_client.model.duty_location import DutyLocation
from ghc_client.model.gbloc import GBLOC
from ghc_client.model.move_status import MoveStatus
globals()['Customer'] = Customer
globals()['DeptIndicator'] = DeptIndicator
globals()['DutyLocation'] = DutyLocation
globals()['GBLOC'] = GBLOC
globals()['MoveStatus'] = MoveStatus
from ghc_client.model.queue_move import QueueMove


class TestQueueMove(unittest.TestCase):
    """QueueMove unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueueMove(self):
        """Test QueueMove"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueueMove()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()