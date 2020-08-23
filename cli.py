import logging

import click

from bankelevator import Elevator, ElevatorInsideController, ElevatorOutsideController

logger = logging.getLogger(__name__)


@click.command()
@click.option("--floors", type=int, required=True)
@click.option("--current_floor", type=int, required=True)
def main(floors, current_floor):

    elevator = Elevator(floors)
    elevator.current_floor = current_floor

    eic = ElevatorInsideController(elevator)
    result1 = eic(current_floor, [9, 8, 5, 6], [3, 2, 0])

    eoc = ElevatorOutsideController(elevator)
    result2 = eoc(
        current_floor, [(1, 9), (2, 8), (5, 5), (4, 6), (9, 3), (9, 2), (9, 0)]
    )

    logger.info(f"Inside Algo Output: {result1}")
    logger.info(f"Outside Algo Output: {result2}")

    assert result1 == result2


if __name__ == "__main__":
    main()
