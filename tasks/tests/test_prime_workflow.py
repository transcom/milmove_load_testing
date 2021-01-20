# -*- coding: utf-8 -*-
from locust.test.testcases import LocustTestCase

from tasks import PrimeWorkflowTasks
from locustfiles.prime_workflow import PrimeWorkflowUser
from utils.constants import (
    MOVE_TASK_ORDER,
    MTO_SHIPMENT,
    MTO_SERVICE_ITEM,
    PAYMENT_REQUEST,
)
from utils.base import ImplementationError


class TestPrimeWorkflowTasks(LocustTestCase):
    def setUp(self):
        super().setUp()

        class TestWorkflowUser(PrimeWorkflowUser):
            host = "127.0.0.1"

        self.locust = TestWorkflowUser(self.environment)
        self.taskset = PrimeWorkflowTasks(self.locust)

    def test_add_stored_mto(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move, and then another move
        # Expectation: It should store the move into current move and then replace it, since we only keep one move.

        move = {"id": "12345"}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)
        assert self.taskset.current_move["id"] == move["id"]

        new_move = {"id": "45678"}
        self.taskset.add_stored(MOVE_TASK_ORDER, new_move)
        assert self.taskset.current_move["id"] == new_move["id"]

    def test_add_stored_shipment(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and a shipment
        # Expectation: It should store the shipment into the move

        # Add a move
        move = {"id": "12345", "mtoShipments": None}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Add a first shipment
        shipment = {"id": "45678", "moveTaskOrderID": "12345"}
        self.taskset.add_stored(MTO_SHIPMENT, shipment)

        # Check that move stayed the same
        stored_move = self.taskset.current_move
        assert stored_move["id"] == move["id"]

        # Check that shipment was added
        assert stored_move["mtoShipments"]
        stored_shipment = stored_move["mtoShipments"][0]
        assert stored_shipment["id"] == shipment["id"]

        # Scenario: We add a second shipment
        # Expectation: It should store the second shipment into the move

        # Add a second shipment
        shipment = {"id": "56789", "moveTaskOrderID": "12345"}
        self.taskset.add_stored(MTO_SHIPMENT, shipment)

        # Check that second shipment was stored
        assert len(stored_move["mtoShipments"]) == 2
        stored_shipment = stored_move["mtoShipments"][1]
        assert stored_shipment["id"] == shipment["id"]

    def test_add_stored_shipment_errors(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and a shipment, and then try to add a shipment with the same
        # moveTaskOrderID
        # Expectation: It should raise an exception and not be stored

        # Add a move with a shipment
        move = {"id": "12345", "mtoShipments": [{"id": "56789", "moveTaskOrderID": "12345"}]}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Add a second shipment with the same shipment id, should assert error
        shipment = {"id": "56789", "moveTaskOrderID": "12345"}
        self.assertRaises(ImplementationError, self.taskset.add_stored, MTO_SHIPMENT, shipment)

        # Check that this shipment was not added, same number of shipments as before
        stored_move = self.taskset.current_move
        assert len(stored_move["mtoShipments"]) == 1

        # Scenario: We now try to add a shipment with the wrong parent moveTaskOrderID
        # Expectation: It should raise an exception and not be stored

        # Add a second shipment with the wrong moveTaskOrderID
        shipment = {"id": "76543", "moveTaskOrderID": "66666"}
        self.assertRaises(ImplementationError, self.taskset.add_stored, MTO_SHIPMENT, shipment)

        # Check that this shipment was not added, same number of shipments as before
        stored_move = self.taskset.current_move
        assert len(stored_move["mtoShipments"]) == 1

    def test_add_stored_service_item(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and a service item
        # Expectation: It should store the service item into the move

        # Add a move
        move = {"id": "12345", "mtoShipments": None, "mtoServiceItems": None}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Add a first serviceItem
        service_item = {"id": "45678", "moveTaskOrderID": "12345"}
        self.taskset.add_stored(MTO_SERVICE_ITEM, service_item)

        # Check that the serviceItem was added to the right part of the move
        stored_move = self.taskset.current_move
        assert stored_move["mtoServiceItems"]
        stored_service_item = stored_move["mtoServiceItems"][0]
        assert stored_service_item["id"] == service_item["id"]

    def test_add_stored_payment_request(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and a payment_request
        # Expectation: It should store the payment_request into the move

        # Add a move
        move = {"id": "12345", "mtoShipments": None, "mtoServiceItems": None}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Add a first shipment
        payment_request = {"id": "45678", "moveTaskOrderID": "12345"}
        self.taskset.add_stored(PAYMENT_REQUEST, payment_request)

        # Check that the serviceItem was added
        stored_move = self.taskset.current_move
        assert stored_move["paymentRequests"]
        stored_payment_request = stored_move["paymentRequests"][0]
        assert stored_payment_request["id"] == payment_request["id"]

    def test_replace_stored_shipment(self):
        """
        Under test: add_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and a shipment
        # Expectation: It should store the shipment into the move

        # Add a move
        move = {"id": "12345", "mtoShipments": None}
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Add a first shipment
        shipment = {"id": "45678", "moveTaskOrderID": "12345", "weight": "100"}
        self.taskset.add_stored(MTO_SHIPMENT, shipment)

        # Check that move stayed the same
        stored_move = self.taskset.current_move
        stored_shipment = stored_move["mtoShipments"][0]
        assert stored_shipment["id"] == shipment["id"]

        # Scenario: We update the first shipment
        # Expectation: It should replace the first shipment

        # Update the shipment
        new_shipment = {"id": "45678", "moveTaskOrderID": "12345", "weight": "47"}
        self.taskset.update_stored(MTO_SHIPMENT, shipment, new_shipment)

        # Check that shipment was updated
        assert len(stored_move["mtoShipments"]) == 1
        stored_shipment = stored_move["mtoShipments"][0]
        assert stored_shipment["weight"] == new_shipment["weight"]

    def test_get_stored_shipment(self):
        """
        Under test: get_stored function
        Mocked: Data objects are simplified versions
        """

        # Scenario: We add a move and 2 shipments
        # Expectation: We should be able to retrieve a random and a specific shipment

        # Add a move with shipments
        move = {
            "id": "12345",
            "mtoShipments": [{"id": "56789", "moveTaskOrderID": "12345"}, {"id": "34567", "moveTaskOrderID": "12345"}],
        }
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        # Get a random shipment
        shipment = self.taskset.get_stored(MTO_SHIPMENT)
        assert shipment["id"] == "56789" or shipment["id"] == "34567"

        # Get a specific shipment
        shipment = self.taskset.get_stored(MTO_SHIPMENT, id="34567")
        assert shipment["id"] == "34567"

        # Scenario: We add a move and no shipments
        # Expectation: We should get None when we request shipments

        # Add a move with no shipments
        move = {
            "id": "12345",
            "mtoShipments": [],
        }
        self.taskset.add_stored(MOVE_TASK_ORDER, move)

        shipment = self.taskset.get_stored(MTO_SHIPMENT)
        assert shipment is None

        shipment = self.taskset.get_stored(MTO_SHIPMENT, id="34567")
        assert shipment is None
