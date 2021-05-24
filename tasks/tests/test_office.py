# -*- coding: utf-8 -*-
""" Tests tasks/prime.py """
import pytest

from tasks.office import OfficeDataStorageMixin
from utils.constants import MOVE_TASK_ORDER, ORDER


class TestOfficeDataStorageMixin:
    """
    Tests the OfficeDataStorageMixin class and its methods. This class is intended to be subclasses and work on ALL
    instances of inheriting classes.
    """

    @classmethod
    def setup_class(cls):
        """ Define and initialize the classes that will be tested. """

        class OfficeStorage1(OfficeDataStorageMixin):
            DATA_LIST_MAX = 3

        class OfficeStorage2(OfficeDataStorageMixin):
            DATA_LIST_MAX = 3

        cls.storage1 = OfficeStorage1()
        cls.storage2 = OfficeStorage2()

    @pytest.mark.parametrize(
        "object_key, object_id, test_store",
        [
            (MOVE_TASK_ORDER, None, {"1": {"id": "1"}}),
            (ORDER, None, {"1": {"id": "1"}, "2": {"id": "2"}, "3": {"id": "3"}}),
        ],
    )
    def test_get_stored__random(self, object_key, object_id, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store

        assert self.storage1.get_stored(object_key) in test_store.values()
        assert self.storage2.get_stored(object_key) in test_store.values()
        assert len(self.storage1.local_store[object_key]) == len(self.storage2.local_store[object_key])

    @pytest.mark.parametrize(
        "object_key, object_id, test_store",
        [
            (MOVE_TASK_ORDER, "1", {"1": {"id": "1"}}),
            (ORDER, "3", {"1": {"id": "1"}, "2": {"id": "2"}, "3": {"id": "3"}}),
        ],
    )
    def test_get_stored__by_id(self, object_key, object_id, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store

        assert self.storage1.get_stored(object_key, object_id) == test_store[object_id]
        assert self.storage2.get_stored(object_key, object_id) == test_store[object_id]

    def test_get_stored__empty(self):
        """ Test the get_stored() method with an empty list of data. """
        self.storage1.local_store["empty_list"] = {}

        assert self.storage1.get_stored("empty_list") is None
        assert self.storage2.get_stored("empty_list") is None
