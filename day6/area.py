from enum import Flag, auto


class LoopException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class ObstacleException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class Direction(Flag):
    NONE = 0
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Element:
    def __init__(self) -> None:
        self._obstacle = False
        self._used_direction = Direction.NONE

    def add_direction(self, direction: Direction) -> None:
        if direction in self._used_direction:
            raise LoopException("Direction already used")
        self._used_direction |= direction

    @property
    def obstacle(self) -> bool:
        return self._obstacle

    @obstacle.setter
    def obstacle(self, value: bool) -> None:
        if value and self._obstacle:
            raise ObstacleException("Element is already an Obstacle")
        self._obstacle = value

    @property
    def is_used(self) -> bool:
        return self._used_direction != Direction.NONE

    @property
    def up(self) -> bool:
        return Direction.UP in self._used_direction

    @up.setter
    def up(self, value: bool) -> None:
        if value:
            self._used_direction |= Direction(Direction.UP)
        else:
            self._used_direction &= ~Direction(Direction.UP)

    @property
    def down(self) -> bool:
        return Direction.DOWN in self._used_direction

    @down.setter
    def down(self, value: bool) -> None:
        if value:
            self._used_direction |= Direction(Direction.DOWN)
        else:
            self._used_direction &= ~Direction(Direction.DOWN)

    @property
    def left(self) -> bool:
        return Direction.LEFT in self._used_direction

    @left.setter
    def left(self, value: bool) -> None:
        if value:
            self._used_direction |= Direction(Direction.LEFT)
        else:
            self._used_direction &= ~Direction(Direction.LEFT)

    @property
    def right(self) -> bool:
        return Direction.RIGHT in self._used_direction

    @right.setter
    def right(self, value: bool) -> None:
        if value:
            self._used_direction |= Direction(Direction.RIGHT)
        else:
            self._used_direction &= ~Direction(Direction.RIGHT)


Row = list[Element]


class Area:
    def __init__(self, area: list[str]) -> None:
        self._area = area
        self.width = len(area[0])
        self.height = len(area)
        self.x: int = 0
        self.y: int = 0

        self.reset()
        # self._init_map(area)
        # self._init_position(area)

    def reset(self) -> None:
        self._init_map()
        self._init_position()

    def _init_map(self) -> None:
        self.map: list[Row] = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Element())
                if self._area[y][x] == "#":
                    row[-1].obstacle = True
            self.map.append(row)

    def _init_position(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self._area[y][x] not in ("^", "v", "<", ">"):
                    continue

                if self._area[y][x] == "^":
                    self.direction = Direction.UP
                elif self._area[y][x] == "v":
                    self.direction = Direction.DOWN
                elif self._area[y][x] == "<":
                    self.direction = Direction.LEFT
                elif self._area[y][x] == ">":
                    self.direction = Direction.RIGHT

                self.x = x
                self.y = y
                self.current_element = self.map[y][x]
                return
        raise ValueError("Start position not found")

    @property
    def all_positions(self) -> list[tuple[int, int]]:
        positions = []
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x].is_used:
                    positions.append((x,y))
        return positions

    def append_obstacle(self, x: int, y: int) -> None:
        self.map[y][x].obstacle = True

    def remove_obstacle(self, x: int, y: int) -> None:
        self.map[y][x].obstacle = False

    def get_next_element(self) -> Element:
        if self.direction == Direction.UP:
            if self.y == 0:
                raise IndexError("Out of bounds")

            return self.map[self.y - 1][self.x]
        elif self.direction == Direction.DOWN:
            if self.y == self.height - 1:
                raise IndexError("Out of bounds")

            return self.map[self.y + 1][self.x]
        elif self.direction == Direction.LEFT:
            if self.x == 0:
                raise IndexError("Out of bounds")

            return self.map[self.y][self.x - 1]
        elif self.direction == Direction.RIGHT:
            if self.x == self.width - 1:
                raise IndexError("Out of bounds")

            return self.map[self.y][self.x + 1]

        raise ValueError("Invalid direction")

    def turn_right(self) -> None:
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP
        else:
            raise ValueError("Invalid direction")

    def update_position(self) -> None:
        if self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        else:
            raise ValueError("Invalid direction")

    def walk(self) -> None:
        next_element = self.get_next_element()
        if next_element.obstacle:
            self.turn_right()
            self.current_element.add_direction(self.direction)
            return

        self.current_element = next_element
        self.update_position()
        self.current_element.add_direction(self.direction)
