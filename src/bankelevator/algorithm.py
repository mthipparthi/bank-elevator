import logging


_logger = logging.getLogger(__name__)


class ElevatorInsideController:
    def __init__(self, elevator):
        self._elevator = elevator

    def set_current_floor(self, current_floor):
        self._elevator.current_floor = current_floor

    def _validate_inputs(self, input_floors, up=True):

        if (
            self._elevator.ground_floor > self._elevator.current_floor
            or self._elevator.current_floor > self._elevator.top_floor
        ):
            raise ValueError("Current floor should be between  ground and top floor")

        if up:
            if min(input_floors) < self._elevator.current_floor:
                raise ValueError("UP Floor can't be less than current floor")
        else:
            if max(input_floors) > self._elevator.current_floor:
                raise ValueError("Down Floor can't be greater than current floor")

    def _get_moves(self, current_floor, up_floors, down_floors):
        """Calculate all moves needed for algo.

        As part of this, firstly, we calculate all the up moves needed
        from current floor and then the destination floor of all moves
        are calaulated(MAX of up_floors) and that is the basis to calulate
        all down floors moves.

        For eg : if set of users all at floor 4 and decided go UP[9, 8, 5, 6],
        DOWN[3, 2, 0].This algo calcuklate all up moves first and final
        destination is 9 and from that point it calculates all down moves.

        Args:
            current_floor (int): Current Floor to be used for calculation
            up_floors ([int]): All users choices(an array) who want to go up
            down_floors ([int]): All users choices(an array) who want to go down

        Returns:
            ([int][int]): An array of array enlisting all moves for each user
        """
        self._elevator.current_floor = current_floor

        self._validate_inputs(up_floors, up=True)

        up_moves = []
        for i in up_floors:
            up_moves += [self._elevator.up_down_moves(steps=i, up=True)]

        self._elevator.current_floor = max(up_floors)

        self._validate_inputs(down_floors, up=False)

        down_moves = []
        for i in down_floors:
            down_moves += [self._elevator.up_down_moves(steps=i, up=False)]

        return up_moves, down_moves

    def __call__(self, current_floor, up_floors, down_floors):
        """Calculate all instructions.

        This functions takes all consolidated up/down floors users entered from
        starting floor. First it calculates all up moves from "Starting floor"
        and then calculates down moves from there(top floor).
        And then calculate instructions for up/down moves.

        Args:
            current_floor (int): This algo works with any floor, starting floor
            up_floors ([int]): Consoloidated up floors users enter from
            starting floor
            down_floors ([int]): Consoloidated down floors users enter from
            starting floor

        Returns:
            ([str]): Instruction set for elevator
        """
        up_moves, down_moves = self._get_moves(current_floor, up_floors, down_floors)

        up_instructions = self._inside_without_move(up_moves, up=True)

        down_instructions = self._inside_without_move(down_moves, up=False)

        return up_instructions + down_instructions

    def _inside_without_move(self, users_moves, up=True):
        """Core algo that is basis for both inside and outside.

        For eg :
        a = [1, 2, 3, 4, 5] - for User a destination is 5
        b = [1, 2, 3, 4, 5, 8]- for User b destination is 8
        c = [1, 2, 3, 4, 5, 6, 7, 8, 9] - for User c destination is 9
        d = [1, 2, 3, 4, 5, 6, 7] - for User d destination is 7
        users_moves = [a,b,c,d]

        Step1 : Sort all the user in the ascending(UP)/descending(DOWN)
        order of destination

        Step2 : And keep track of all visited floors and if already visited
        do not add to instructions else add to instruction.

        step3 : if one user moves are exhausted then add OPEN/CLOSE to
        instruction set.

        Args:
            user_inputs ([[int]...]): List of all possible user moves from
            current floor to destination
            up (bool, optional): To indicate UP moves or Down moves.
            Defaults to True.

        Returns:
            [str]: List of all instruction set
        """
        users_moves = [i for i in users_moves if len(i) > 0]
        sorted_input = sorted(users_moves, key=lambda x: x[-1], reverse=not up)
        visited = set()
        instructions_set = []
        # Leaving this here for easy visulization
        start_stop_array = []
        for i in sorted_input:
            for j in i:
                if j not in visited:
                    start_stop_array.append(j)
                    instruction = "UP_1" if up else "DOWN_1"
                    instructions_set.append(instruction)
                visited.add(j)

            if instructions_set[-1] != "CLOSE_DOOR":
                instructions_set.append("OPEN_DOOR")
                instructions_set.append("CLOSE_DOOR")
                start_stop_array.append("-")

        _logger.info(f"Instruction set for up={up} - {start_stop_array}")

        return instructions_set


class ElevatorOutsideController:
    def __init__(self, elevator):

        self._elevator = elevator

    def __call__(self, current_floor, user_inputs):
        """Outside algo.

        Outside algo can be reduced to of inside algo + segregation of user inputs.
        if we segregate user inputs(his current location, his target location)
        by substracting targetlocation and currentlocation,
        then we can arrive at upfloors and down floors.

        For eg :
        if User1 who is at floor 3 wants go to Floor 9 - (3,9) - 9 > 3 it is up move
        if User2 who is at floor 7 wants go to Floor 2 - (7,2) - 2 < 7 it is down move

        Args:
            current_floor (int): Current floor elevator stationed at
            user_inputs ([(int, int)]): list of User location and his target floor

        Returns:
            [str]: List of instruction
        """
        up_floors = [i[1] for i in user_inputs if i[1] >= i[0]]
        down_floors = [i[1] for i in user_inputs if i[1] < i[0]]
        ec = ElevatorInsideController(self._elevator)

        return ec(current_floor, up_floors, down_floors)
