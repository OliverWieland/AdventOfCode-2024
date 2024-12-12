from pathlib import Path

Equation = tuple[int, list[int]]


def get_equations(lines: list[str]) -> list[Equation]:
    equations = []
    for line in lines:
        parts = line.split(" ")
        sum = int(parts.pop(0)[:-1])
        coefficients = list(map(int, parts))
        equations.append((sum, coefficients))

    return equations


def calc(expected: int, a: int, coefficients: list[int], concat_op: bool) -> bool:
    if len(coefficients) == 0:
        return a == expected

    b = coefficients[0]
    result = a * b

    if result <= expected:
        coeff_copy = coefficients.copy()
        coeff_copy.pop(0)
        valid = calc(expected, result, coeff_copy, concat_op)

        if valid:
            return True

    result = a + b
    if result <= expected:
        coeff_copy = coefficients.copy()
        coeff_copy.pop(0)
        valid = calc(expected, result, coeff_copy, concat_op)

        if valid:
            return True

    if not concat_op:
        return False

    result = int(f"{a}{b}")
    if result <= expected:
        coeff_copy = coefficients.copy()
        coeff_copy.pop(0)
        valid = calc(expected, result, coeff_copy, concat_op)

        if valid:
            return True

    return False


def part_1(data: list[str]) -> int:
    equations = get_equations(data)
    result = 0
    for equation in equations:
        coefficients = equation[1]

        if calc(equation[0], 0, coefficients, False):
            result += equation[0]
    return result


def part_2(data: list[str]) -> int:
    equations = get_equations(data)
    result = 0
    for equation in equations:
        coefficients = equation[1]

        if calc(equation[0], 0, coefficients, True):
            result += equation[0]
    return result


def day_7():
    data = read_input()
    print(f"Part1: {part_1(data)}")
    data = read_input()
    print(f"Part2: {part_2(data)}")


def read_input() -> list[str]:
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    return lines
