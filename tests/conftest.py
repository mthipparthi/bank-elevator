import bankelevator

import pytest


@pytest.fixture()
def elevator():
    elevator = bankelevator.Elevator(floors=11)
    yield elevator


@pytest.fixture()
def elevator_inside_controller(elevator):
    yield bankelevator.ElevatorInsideController(elevator)


@pytest.fixture()
def elevator_outside_controller(elevator):
    yield bankelevator.ElevatorOutsideController(elevator)
