from pathlib import Path

from day6.area import Area, LoopException, ObstacleException


def part_1(data: list[str]) -> list:
    area = Area(data)

    try:
        while True:
            area.walk()
    except IndexError:
        pass

    return area.all_positions


def part_2(data: list[str]) -> int:
    possible_positions = part_1(data)
    count_positions = 0
    area = Area(data)
    obstruction_positions = set()

    for position in possible_positions:
        area.reset()
        try:
            area.append_obstacle(*position)
        except ObstacleException:
            continue

        try:
            while True:
                area.walk()
        except IndexError:
            pass
        except LoopException:
            obstruction_positions.add(position)
            count_positions += 1
            print(f"Possible obstruction #{count_positions} at ({position[1]}, {position[0]})")

    return len(obstruction_positions)


def day_6():
    data = read_input()
    print(f"Part1: {len(part_1(data))}")
    # data = read_input()
    # print(f"Part2: {part_2(data)}")


def read_input() -> list[str]:
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = f.readlines()
        area = [line.strip() for line in lines]  # Remove trailing newline characters

    return area
