import pytest

# from bankelevator  import


def test_elevator_created(elevator):
    assert elevator.top_floor == 10
    assert elevator.ground_floor == 0
    assert elevator.current_floor == 0


@pytest.mark.parametrize(
    "current_floor,target_floor, result",
    [
        (3, 8, [4, 5, 6, 7, 8]),
        (0, 5, [1, 2, 3, 4, 5]),
        (9, 5, [10]),
        (0, 5, [1, 2, 3, 4, 5]),
    ],
)
def test_up_moves(elevator, current_floor, target_floor, result):
    elevator.current_floor = current_floor
    assert elevator.up_moves(target_floor) == result


@pytest.mark.parametrize(
    "current_floor,target_floor, result",
    [(9, 5, [8, 7, 6, 5]), (7, 2, [6, 5, 4, 3, 2]), (4, -2, [3, 2, 1, 0])],
)
def test_down_moves(elevator, current_floor, target_floor, result):
    elevator.current_floor = current_floor
    assert elevator.down_moves(target_floor) == result
