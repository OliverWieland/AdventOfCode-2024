import itertools
import operator
from pathlib import Path
from string import ascii_letters, digits

Area = list[str]
Position = tuple[int, int]


def get_antennas(area: Area, frequency: str) -> list[Position]:
    antennas: list[Position] = []
    for y, row in enumerate(area):
        cols = [i for i, letter in enumerate(row) if letter == frequency]

        for x in cols:
            antennas.append((x, y))
    return antennas


def get_antinodes(
    antenna1: Position, antenna2: Position, areasize: tuple[int, int]
) -> list[Position]:
    antinodes: list[Position] = []
    diff_antennas = tuple(map(operator.sub, antenna1, antenna2))
    antinode = tuple(map(operator.add, antenna1, diff_antennas))

    if 0 <= antinode[0] < areasize[0] and 0 <= antinode[1] < areasize[1]:
        antinodes.append(antinode)

    antinode = tuple(map(operator.sub, antenna2, diff_antennas))

    if 0 <= antinode[0] < areasize[0] and 0 <= antinode[1] < areasize[1]:
        antinodes.append(antinode)

    return antinodes


def get_antinodes2(
    antenna1: Position, antenna2: Position, areasize: tuple[int, int]
) -> list[Position]:
    antinodes: list[Position] = []
    diff_antennas = tuple(map(operator.sub, antenna1, antenna2))
    position = antenna1

    while True:
        antinode = tuple(map(operator.add, position, diff_antennas))

        if not (0 <= antinode[0] < areasize[0]):
            break
        if not (0 <= antinode[1] < areasize[1]):
            break

        antinodes.append(antinode)
        position = antinode

    position = antenna2

    while True:
        antinode = tuple(map(operator.sub, position, diff_antennas))

        if not (0 <= antinode[0] < areasize[0]):
            break
        if not (0 <= antinode[1] < areasize[1]):
            break

        antinodes.append(antinode)
        position = antinode

    return antinodes


def part_1(data: list[str]) -> int:
    antinodes: list[Position] = []
    valid_letters = ascii_letters + digits
    for letter in valid_letters:
        antennas = get_antennas(data, letter)
        if not antennas:
            continue

        pairs = list(itertools.combinations(antennas, 2))
        for pair in pairs:
            antinodes += get_antinodes(*pair, (len(data[0]), len(data)))
    return len(set(antinodes))


def part_2(data: list[str]) -> int:
    antinodes: list[Position] = []
    valid_letters = ascii_letters + digits
    for letter in valid_letters:
        antennas = get_antennas(data, letter)
        if not antennas:
            continue

        antinodes += antennas
        pairs = list(itertools.combinations(antennas, 2))
        for pair in pairs:
            antinodes += get_antinodes2(*pair, (len(data[0]), len(data)))
    return len(set(antinodes))


def day_8():
    data = read_input()
    print(f"Part1: {part_1(data)}")
    data = read_input()
    print(f"Part2: {part_2(data)}")


def read_input() -> list[str]:
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    return lines
