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

    @pytest.mark.parametrize(
        "object_key, object_data, test_store",
        [
            (MOVE_TASK_ORDER, {"id": "2"}, {"1": {"id": "1"}}),
        ],
    )
    def test_add_stored__new_item(self, object_key, object_data, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.add_stored(object_key, object_data)

        assert self.storage1.get_stored(object_key, object_data["id"]) == object_data

    @pytest.mark.parametrize(
        "object_key, object_data, test_store",
        [
            (MOVE_TASK_ORDER, [{"id": "2"}, {"id": "3"}], {"1": {"id": "1"}}),
        ],
    )
    def test_add_stored__items_list(self, object_key, object_data, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.add_stored(object_key, object_data)

        for item in object_data:
            assert self.storage1.get_stored(object_key, item["id"]) == item

    @pytest.mark.parametrize(
        "object_key, object_data, test_store",
        [
            (MOVE_TASK_ORDER, {"id": "1", "orderId": "2"}, {"1": {"id": "1"}}),
        ],
    )
    def test_add_stored__updates_existing(self, object_key, object_data, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.add_stored(object_key, object_data)

        assert self.storage1.get_stored(object_key, object_data["id"]) == object_data

    @pytest.mark.parametrize(
        "object_key, object_data, test_store",
        [
            (MOVE_TASK_ORDER, [{"id": "1", "ordersId": "2"}, {"id": "2"}], {"1": {"id": "1"}}),
        ],
    )
    def test_add_stored__list_does_not_overwrite(self, object_key, object_data, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.add_stored(object_key, object_data)

        assert self.storage1.get_stored(object_key, "1") == {"id": "1"}
        assert self.storage1.get_stored(object_key, "2") == {"id": "2"}

    @pytest.mark.parametrize(
        "object_key, object_data, test_store",
        [
            (MOVE_TASK_ORDER, {"id": "4"}, {"1": {"id": "1"}, "2": {"id": "2"}, "3": {"id": "3"}}),
        ],
    )
    def test_add_stored__max_capacity(self, object_key, object_data, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store
        assert len(self.storage1.local_store[object_key]) == self.storage1.DATA_LIST_MAX

        self.storage1.add_stored(object_key, object_data)

        assert len(self.storage1.local_store[object_key]) <= self.storage1.DATA_LIST_MAX
        assert self.storage1.get_stored(object_key, object_data["id"]) == object_data
