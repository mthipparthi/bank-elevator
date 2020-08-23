import pytest


@pytest.mark.parametrize(
    "up, users_moves, result",
    [
        (
            True,
            [[3, 4, 5], [3, 4, 5, 6], [3, 4, 5, 6, 7]],
            [
                "UP_1",
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
            ],
        ),
        (
            True,
            [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 5, 6, 7, 8]],
            [
                "UP_1",
                "UP_1",
                "UP_1",
                "UP_1",
                "UP_1",
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
            ],
        ),
    ],
)
def test_elevator_inside_without_move_up(
    elevator_inside_controller, users_moves, up, result
):
    assert elevator_inside_controller._inside_without_move(users_moves, up) == result


@pytest.mark.parametrize(
    "current_floor, invalid_inputs, up",
    [(4, [1, 2, 3], True), (5, [7, 8, 9], False), (15, [7, 8, 9], True)],
)
def test_elevator_inside_validate(
    elevator_inside_controller, current_floor, invalid_inputs, up
):
    with pytest.raises(ValueError):
        elevator_inside_controller.set_current_floor(current_floor)
        elevator_inside_controller._validate_inputs(invalid_inputs, up)


@pytest.mark.parametrize(
    "current_floor, up_floors, down_floors, result ",
    [
        (
            4,
            [9, 8, 5, 6],
            [3, 2, 0],
            (
                [[5, 6, 7, 8, 9], [5, 6, 7, 8], [5], [5, 6]],
                [
                    [8, 7, 6, 5, 4, 3],
                    [8, 7, 6, 5, 4, 3, 2],
                    [8, 7, 6, 5, 4, 3, 2, 1, 0],
                ],
            ),
        )
    ],
)
def test_elevator_inside_without_get_moves(
    elevator_inside_controller, current_floor, up_floors, down_floors, result
):
    assert (
        elevator_inside_controller._get_moves(current_floor, up_floors, down_floors)
        == result
    )


@pytest.mark.parametrize(
    "current_floor, up_floors, down_floors, result ",
    [
        (
            3,
            [9, 8, 5, 6],
            [3, 2, 0],
            [
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
            ],
        ),
        (
            8,
            [9, 10],
            [0],
            [
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
            ],
        ),
    ],
)
def test_elevator_inside_algo(
    elevator_inside_controller, current_floor, up_floors, down_floors, result
):

    assert elevator_inside_controller(current_floor, up_floors, down_floors) == result


@pytest.mark.parametrize(
    "current_floor, users_input, result",
    [
        (
            3,
            [(1, 9), (2, 8), (5, 5), (4, 6), (9, 3), (9, 2), (9, 0)],
            [
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "UP_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
                "DOWN_1",
                "DOWN_1",
                "OPEN_DOOR",
                "CLOSE_DOOR",
            ],
        )
    ],
)
def test_elevator_outside_algo(
    elevator_outside_controller, current_floor, users_input, result
):

    assert elevator_outside_controller(current_floor, users_input) == result
