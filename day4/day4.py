from pathlib import Path


def find_word(
    lines, x: int, y: int, direction: tuple[int, int], next_char: str
) -> bool:
    if x >= len(lines[0]):
        return False
    if x < 0:
        return False
    if y >= len(lines):
        return False
    if y < 0:
        return False

    char = lines[y][x]
    if char != next_char:
        return False
    x += direction[0]
    y += direction[1]

    try:
        next_char = "XMAS"["XMAS".index(next_char) + 1]
    except IndexError:
        return True

    return find_word(lines, x, y, direction, next_char)


def find_x_mas(lines, x: int, y: int) -> bool:
    if lines[y][x] != "A":
        return False
    if x >= len(lines[0]) - 1:
        return False
    if x < 1:
        return False
    if y >= len(lines) - 1:
        return False
    if y < 1:
        return False

    count = 0
    for dir_x in (-1, 1):
        for dir_y in (-1, 1):
            if lines[y + dir_y][x + dir_x] != "M":
                continue
            if lines[y - dir_y][x - dir_x] != "S":
                continue
            count += 1
            if count > 1:
                return True
    return False


def part_1(lines):
    words = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            char = lines[y][x]
            if char != "X":
                continue

            for dir_x in (-1, 0, 1):
                for dir_y in (-1, 0, 1):
                    if find_word(lines, x, y, (dir_x, dir_y), "X"):
                        words += 1
    return words


def part_2(lines):
    count = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if find_x_mas(lines, x, y):
                count += 1

    return count


def day_4():
    memory = read_input()
    print(f"Part1: {part_1(memory)}")
    print(f"Part2: {part_2(memory)}")


def read_input():
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]  # Remove trailing newline characters

    return lines
