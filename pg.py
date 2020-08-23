def up_moves(self, steps):
    rv = []
    target_floor = self._current_floor + steps
    floor_itr = self._current_floor
    while self._ground <= floor_itr <= self._top:
        if floor_itr == target_floor:
            break
        floor_itr += 1
        rv.append(floor_itr)
    return rv


def down_moves(self, steps):
    rv = []
    floor_itr = self._current_floor
    target_floor = self._current_floor - steps
    while self._ground <= floor_itr <= self._top:
        if floor_itr == target_floor:
            break
        if floor_itr > 0:
            rv.append(floor_itr)
        floor_itr -= 1
    return rv


def elevator_algo_up():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = [1, 2, 3, 4, 5, 6, 7]
    e = [a, d, b, c]
    print(e)
    e = sorted(e, key=lambda x: x[-1])
    print(e)
    visited = set()
    start_stop_array = []
    for i in e:
        for j in i:
            if j not in visited:
                start_stop_array.append(j)
            visited.add(j)
        if start_stop_array[-1] != "-":
            start_stop_array.append("-")

    print(visited)
    print(start_stop_array)

    instruction_set = []

    for i in start_stop_array:
        if i == "-":
            instruction_set.append("OPEN_DOOR")
            instruction_set.append("CLOSE_DOOR")
        else:
            instruction_set.append("UP_1")

    print(instruction_set)


def elevator_algo_down():
    a = [9, 8, 7, 6, 5]
    b = [9, 8, 7, 6, 5, 4]
    c = [9, 8, 7, 6, 5, 4, 3]
    c1 = [9, 8, 7, 6, 5, 4, 3]
    d = [9, 8, 7, 6, 5, 4, 3, 2]
    e = [a, d, b, c, c1]
    print(e)
    e = sorted(e, key=lambda x: x[-1], reverse=True)
    print(e)
    visited = set()
    start_stop_array = []
    for i in e:
        for j in i:
            if j not in visited:
                start_stop_array.append(j)
            visited.add(j)

        if start_stop_array[-1] != "-":
            start_stop_array.append("-")

    print(visited)
    print(start_stop_array)

    instruction_set = []

    for i in start_stop_array:
        if i == "-":
            instruction_set.append("OPEN_DOOR")
            instruction_set.append("CLOSE_DOOR")
        else:
            instruction_set.append("DOWN_1")

    print(instruction_set)


# elevator_algo_down()
# elevator_algo_up()


def elevator_algo():
    up_inputs = []
    down_inputs = []

    if len(up_inputs) >= len(down_inputs):
        current_floor, instructions = elevator_algo_inside(up_inputs)
        current_floor, instructions = elevator_algo_inside(up_inputs)


def elevator_algo_inside(user_inputs, up=True):
    """[summary]

    Args:
        user_inputs ([type]): [description]
        up (bool, optional): [description]. Defaults to True.

    Returns:
        [string]: [ instruction set]
    """

    # For UP , it should be in ascending order(floor) as it is going up
    # For Down , It should be in desciding order(floor) as it is coming Down.

    sorted_input = sorted(user_inputs, key=lambda x: x[-1], reverse=not up)

    visited = set()
    instructions_set = []
    # Leaving this here for easy visulization
    start_stop_array = []
    current_floor = 0
    for i in sorted_input:
        for j in i:
            if j not in visited:
                start_stop_array.append(j)
                instruction = "UP_1" if up else "DOWN_1"
                instructions_set.append(instruction)
            visited.add(j)
            current_floor = j

        if instructions_set[-1] != "CLOSE_DOOR":
            instructions_set.append("OPEN_DOOR")
            instructions_set.append("CLOSE_DOOR")
            start_stop_array.append("-")

    print(start_stop_array)
    return current_floor, instructions_set


def main():

    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = [1, 2, 3, 4, 5, 6, 7]
    e = [a, d, b, c]

    print(elevator_algo_inside(e, up=True))

    a = [9, 8, 7, 6, 5]
    b = [9, 8, 7, 6, 5, 4]
    c = [9, 8, 7, 6, 5, 4, 3]
    c1 = [9, 8, 7, 6, 5, 4, 3]
    d = [9, 8, 7, 6, 5, 4, 3, 2]
    e = [a, d, b, c, c1]

    print(elevator_algo_inside(e, up=False))


def elevator_algo_outside():
    a = (1, 2)
    b = (2, 5)
    c = (3, 9)
    d = (4, 2)
    e = [a, b, c, d]

    up_floors = [i[1] for i in e if i[1] - i[0] > 0]
    down_floors = [i[1] for i in e if i[1] - i[0] < 0]

    breakpoint()


if __name__ == "__main__":
    elevator_algo_outside()
