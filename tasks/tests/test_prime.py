# -*- coding: utf-8 -*-
""" Tests tasks/prime.py """
import pytest

import responses
from requests import Session

from tasks.prime import PrimeDataStorageMixin, support_path
from utils.constants import MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST, ZERO_UUID


class TestPrimeDataStorageMixin:
    """
    Tests the PrimeDataStorageMixin class and its methods. This class is intended to be subclasses and work on ALL
    instances of inheriting classes.
    """

    @classmethod
    def setup_class(cls):
        """ Define and initialize the classes that will be tested. """
        # environment = Environment(events=Events(), catch_exceptions=False)

        class PrimeStorage1(PrimeDataStorageMixin):
            DATA_LIST_MAX = 3

        class PrimeStorage2(PrimeDataStorageMixin):
            DATA_LIST_MAX = 3

        cls.storage1 = PrimeStorage1()
        cls.storage2 = PrimeStorage2()

    @pytest.mark.parametrize(
        "object_key,test_store",
        [
            (MOVE_TASK_ORDER, ["MTO 1"]),
            (MTO_SERVICE_ITEM, ["item 1", "item 2", "item 3"]),
        ],
    )
    def test_get_stored(self, object_key, test_store):
        """ Test retrieving a random object from the local_store dictionary lists. """
        self.storage1.local_store[object_key] = test_store

        assert self.storage1.get_stored(object_key) in test_store
        assert self.storage2.get_stored(object_key) in test_store
        assert len(self.storage1.local_store[object_key]) == len(self.storage2.local_store[object_key])

    def test_get_stored__empty(self):
        """ Test the get_stored() method with an empty list of data. """
        empty_list = "empty"
        self.storage1.local_store[empty_list] = []

        assert self.storage1.get_stored(empty_list) is None
        assert self.storage2.get_stored(empty_list) is None

    @pytest.mark.parametrize(
        "shipment_test_store",
        [
            ([{"pickupAddress": {"no": "id"}, "destinationAddress": {"id": "01010"}}]),
            ([{"destinationAddress": {"id": "1234"}}, {"pickupAddress": {"id": "5555555"}}]),
        ],
    )
    def test_get_stored_shipment_address(self, shipment_test_store):
        """ Test the process of getting a random address from the MTO_SHIPMENT local store. """
        self.storage1.local_store[MTO_SHIPMENT] = shipment_test_store
        field, address = self.storage1.get_stored_shipment_address()

        assert any([shipment.get(field) == address for shipment in self.storage1.local_store[MTO_SHIPMENT]])
        assert any([shipment.get(field) == address for shipment in self.storage2.local_store[MTO_SHIPMENT]])
        assert address["id"] != ZERO_UUID

    @pytest.mark.parametrize(
        "test_shipment",
        [
            ({"pickupAddress": {"id": "1234"}, "destinationAddress": {"id": "5768"}}),
            ({"pickupAddress": {"id": "11111"}, "destinationAddress": {"id": ZERO_UUID}}),
            ({"destinationAddress": {"id": "1357"}}),
        ],
    )
    def test_get_stored_shipment_address__given_shipment(self, test_shipment):
        """ Test the process of getting a random address from an MTO_SHIPMENT object passed in as an argument. """
        test_shipment = {"pickupAddress": {"id": "1234"}, "destinationAddress": {"id": "5768"}}
        field, address = self.storage1.get_stored_shipment_address(test_shipment)

        assert test_shipment[field] == address
        assert address["id"] != ZERO_UUID

    @pytest.mark.parametrize(
        "test_store",
        [
            ([]),
            ([{"no": "address"}]),
            ([{"pickupAddress": {"no": "id"}}]),
            ([{"destinationAddress": {"id": ZERO_UUID}}]),
        ],
    )
    def test_get_stored_shipment_address__none_found(self, test_store):
        """ Test get_stored_shipment_address when there are no valid addresses. """
        self.storage1.local_store[MTO_SHIPMENT] = test_store
        with pytest.raises(TypeError):
            _field, _address = self.storage1.get_stored_shipment_address()

        assert self.storage1.get_stored_shipment_address() is None
        assert self.storage2.get_stored_shipment_address() is None

    @pytest.mark.parametrize(
        "object_key,new_object,test_store",
        [
            (MOVE_TASK_ORDER, "new MTO", []),
            (PAYMENT_REQUEST, "new payment", ["old payment"]),
            (MTO_SERVICE_ITEM, "over data list max", ["item 1", "item 2", "item 3"]),
        ],
    )
    def test_add_stored(self, object_key, new_object, test_store):
        """ Test adding an object to local storage. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.add_stored(object_key, new_object)

        assert new_object in self.storage1.local_store[object_key]
        assert new_object in self.storage2.local_store[object_key]
        assert len(self.storage1.local_store[object_key]) == len(self.storage2.local_store[object_key])

    def test_add_stored__list(self):
        """ Test adding a list of objects to local storage. """
        new_data = ["multiple", "new", "objects"]
        self.storage1.local_store[PAYMENT_REQUEST] = ["payment"]
        self.storage1.add_stored(PAYMENT_REQUEST, new_data)

        assert all([data in self.storage1.local_store[PAYMENT_REQUEST] for data in new_data])
        assert all([data in self.storage2.local_store[PAYMENT_REQUEST] for data in new_data])
        assert len(self.storage1.local_store[PAYMENT_REQUEST]) == 4
        assert len(self.storage2.local_store[PAYMENT_REQUEST]) == 4

    @pytest.mark.parametrize(
        "object_key,old_object,new_object,test_store",
        [
            (MOVE_TASK_ORDER, "old MTO", "new MTO", ["old MTO"]),
            (PAYMENT_REQUEST, "old payment", "new payment", []),  # "new payment" should be added w/o error
            (MTO_SERVICE_ITEM, "item 3", "the third item", ["item 1", "item 2", "item 3"]),
            # both "item 3"s should be removed:
            (MTO_SERVICE_ITEM, "item 3", "the third item", ["item 1", "item 2", "item 3", "item 3"]),
        ],
    )
    def test_update_stored(self, object_key, old_object, new_object, test_store):
        """ Test updating an object that is already in the local storage. """
        self.storage1.local_store[object_key] = test_store
        self.storage1.update_stored(object_key, old_object, new_object)

        assert new_object in self.storage1.local_store[object_key]
        assert new_object in self.storage2.local_store[object_key]
        assert old_object not in self.storage1.local_store[object_key]
        assert old_object not in self.storage2.local_store[object_key]
        assert len(self.storage1.local_store[object_key]) == len(self.storage2.local_store[object_key])

    @responses.activate
    def test_set_default_mto_ids(self):
        """ TODO """

        def mocked_url(url):
            return f"http:/{url}"

        test_moves = [
            {
                "id": "0",  # the fake move ID
                "status": 200,
                "json": {"contractorID": "contractor0"},
            },
            {
                "id": "X",
                "status": 404,  # should just be skipped, won't interrupt processing
                "json": {"error": "not found"},  # format doesn't matter, this is a completely fake/mocked response
            },
            {
                "id": "1",
                "status": 200,
                "json": {
                    "moveOrder": {
                        "uploadedOrdersID": "upload1",
                        "destinationDutyStationID": "",  # purposefully blank, will not count for end of loop
                        "originDutyStationID": "origin1",
                    },
                },
            },
            {
                "id": "2",
                "status": 200,
                "json": {
                    "moveOrder": {
                        "destinationDutyStationID": "destination2",
                        "originDutyStationID": "origin2",
                    }
                },
            },
            {
                "id": "3",
                "status": 200,
                "json": {
                    # these values should not be used because they all should have been set previously
                    "contractorID": "contractor3",
                    "moveOrder": {
                        "uploadedOrdersID": "upload3",
                    },
                },
            },
        ]
        # Mock the API calls for each of these moves:
        for test_move in test_moves:
            responses.add(
                responses.GET,
                mocked_url(support_path(f"/move-task-orders/{test_move['id']}")),
                json=test_move["json"],
                status=test_move["status"],
            )

        expected_ids = {
            "contractorID": "contractor0",
            "destinationDutyStationID": "destination2",
            "originDutyStationID": "origin2",
            "uploadedOrdersID": "upload1",
        }

        # Random list to use after first run, none of these values will be used after the default IDs are initially set:
        test_moves_after = [
            {
                "contractorID": "contractor4",
                "moveOrder": {
                    "uploadedOrdersID": "upload4",
                    "destinationDutyStationID": "destination4",
                    "originDutyStationID": "origin4",
                },
            }
        ]

        class MockLocustSession(Session):
            def get(self, path, **kwargs):
                return super().get(mocked_url(path))

        class PrimeSessionStorage1(PrimeDataStorageMixin):
            client = MockLocustSession()
            cert_kwargs = {}

        class PrimeSessionStorage2(PrimeDataStorageMixin):
            client = MockLocustSession()
            cert_kwargs = {}

        session_storage1 = PrimeSessionStorage1()
        session_storage2 = PrimeSessionStorage2()

        session_storage1.set_default_mto_ids(test_moves)

        assert session_storage1.default_mto_ids == expected_ids
        assert session_storage1.default_mto_ids == session_storage2.default_mto_ids
        assert len(responses.calls) == 4

        # Call func again with new list, but all values should stay the same as before:
        session_storage2.set_default_mto_ids(test_moves_after)

        assert session_storage1.default_mto_ids == expected_ids
        assert session_storage1.default_mto_ids == session_storage2.default_mto_ids
        assert len(responses.calls) == 4  # no additional calls
