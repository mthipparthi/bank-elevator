class Elevator:
    def __init__(self, floors):
        self._floors = list(range(0, floors))
        self.ground_floor = self._floors[0]
        self.top_floor = self._floors[-1]
        self._current_floor = self.ground_floor

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, position):
        self._current_floor = position

    def up_moves(self, target_floor):
        """
        Give the floors(UP) from Current floor to Target floor.

        >>> e=Elevator(10)
        >>> e.current_floor = 3
        >>> e.up_moves(8)
        [4, 5, 6, 7, 8]

        """
        rv = []
        floor_itr = self._current_floor
        while self.ground_floor <= floor_itr < self.top_floor:
            if floor_itr == target_floor:
                break
            floor_itr += 1
            rv.append(floor_itr)
        return rv

    def down_moves(self, target_floor):
        """
        Give the floors(DOWN) from Current floor to Target floor.

        >>> e=Elevator(10)
        >>> e.current_floor = 9
        >>> e.down_moves(3)
        [8, 7, 6, 5, 4, 3]
        """
        rv = []
        floor_itr = self._current_floor
        while self.ground_floor <= floor_itr <= self.top_floor:
            if floor_itr == target_floor:
                break
            floor_itr -= 1
            if floor_itr >= 0:
                rv.append(floor_itr)
        return rv

    def up_down_moves(self, steps=1, up=True):
        return self.up_moves(steps) if up else self.down_moves(steps)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
