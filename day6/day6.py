from pathlib import Path


class Area:
    def __init__(self, area: list[str]) -> None:
        self._area = area
        self.width = len(area[0])
        self.height = len(area)
        self.position: list[int] = [0, 0]
        self.direction: str = ""

        self._init_position()

    @property
    def x(self) -> int:
        return self.position[0]

    @x.setter
    def x(self, value: int) -> None:
        self.position[0] = value if value in range(self.width) else -1
        if not self.in_area:
            raise IndexError

    @property
    def y(self) -> int:
        return self.position[1]

    @y.setter
    def y(self, value: int) -> None:
        self.position[1] = value if value in range(self.height) else -1
        if not self.in_area:
            raise IndexError

    @property
    def in_area(self) -> bool:
        return self.x != -1 and self.y != -1

    def _init_position(self):
        for x in range(len(self._area[0])):
            for y in range(len(self._area)):
                if self._area[y][x] in ("^", "v", "<", ">"):
                    self.position = [x, y]
                    self.direction = self._area[y][x]
                    return
        raise ValueError("Start position not found")

    @property
    def current_value(self) -> str:
        return self._area[self.y][self.x]

    @current_value.setter
    def current_value(self, value: str) -> None:
        row = self._area[self.y]
        self._area[self.y] = row[: self.x] + value + row[self.x + 1 :]

    @property
    def position_count(self) -> int:
        count = 0
        for y in range(self.height):
            count += self._area[y].count("X")

        return count

    def walk(self) -> None:
        self.current_value = "X"

        match self.direction:
            case "^":
                self.y -= 1
                if self.current_value == "#":
                    self.y += 1
                    self.direction = ">"
                    self.walk()
                    return
            case "v":
                self.y += 1
                if self.current_value == "#":
                    self.y -= 1
                    self.direction = "<"
                    self.walk()
                    return
            case "<":
                self.x -= 1
                if self.current_value == "#":
                    self.x += 1
                    self.direction = "^"
                    self.walk()
                    return
            case ">":
                self.x += 1
                if self.current_value == "#":
                    self.x -= 1
                    self.direction = "v"
                    self.walk()
                    return
            case _:
                raise ValueError
        self.current_value = "X"


def part_1(data: list[str]) -> int:
    area = Area(data)

    count_positions = 0
    try:
        while True:
            area.walk()
    except IndexError:
        pass

    return area.position_count

    # x, y = get_start_position(area)
    # while x in range(len(area[0])) and y in range(len(area)):
    #     direction = area[y][x]
    #     row = area[y]
    #     area[y] = row[:x] + "X" + row[x + 1 :]
    #     x, y = walk((x, y), area, direction)

    # for i in range(len(area)):
    #     count_positions += area[i].count("X")

    # return count_positions


def part_2(area: Area) -> int: ...


def day_6():
    area = read_input()
    print(f"Part1: {part_1(area)}")
    print(f"Part2: {part_2(area)}")


def read_input() -> list[str]:
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = f.readlines()
        area = [line.strip() for line in lines]  # Remove trailing newline characters

    return area
