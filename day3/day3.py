import re
from pathlib import Path


def part_1(memory):
    result = 0
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    match = pattern.findall(memory)

    if match:
        for group in match:
            result += int(group[0]) * int(group[1])

    return result


def part_2(memory):
    enabled = True
    result = 0
    pattern = re.compile(r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    match = pattern.findall(memory)

    if match:
        for group in match:
            if "don't()" in group:
                enabled = False
                continue
            if "do()" in group:
                enabled = True
                continue

            if not enabled:
                continue
            result += int(group[0]) * int(group[1])

    return result


def day_3():
    memory = read_input()
    print(f"Part1: {part_1(memory)}")
    print(f"Part2: {part_2(memory)}")


def read_input():
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        memory = f.read()

    return memory
