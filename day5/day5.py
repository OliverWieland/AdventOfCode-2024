from pathlib import Path

Rule = tuple[int, int]
Update = list[int]


def is_valid(update: Update, ruleset: list[Rule]) -> bool:
    for rule in ruleset:
        try:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
        except ValueError:
            continue
    return True


def findMiddle(update: Update) -> int:
    middle = float(len(update)) / 2
    if middle % 2 != 0:
        return update[int(middle - 0.5)]
    else:
        return 0


def repair(update: Update, ruleset: list[Rule]) -> Update:
    repaired = update.copy()
    rule_idx = 0
    while rule_idx < len(ruleset):
        rule = ruleset[rule_idx]
        try:
            index1 = repaired.index(rule[0])
            index2 = repaired.index(rule[1])
            if index1 > index2:
                repaired[index1], repaired[index2] = repaired[index2], repaired[index1]
                rule_idx = 0
                continue
        except ValueError:
            rule_idx += 1
            continue

        rule_idx += 1

    return repaired


def part_1(ruleset: list[Rule], updates: list[Update]) -> int:
    valid_updates: list[Update] = []
    for update in updates:
        if is_valid(update, ruleset):
            valid_updates.append(update)

    middle_pagenumber = 0
    for update in valid_updates:
        middle_pagenumber += findMiddle(update)

    return middle_pagenumber


def part_2(ruleset: list[Rule], updates: list[Update]) -> int:
    valid_updates: list[Update] = []
    for update in updates:
        if not is_valid(update, ruleset):
            valid_updates.append(repair(update, ruleset))

    middle_pagenumber = 0
    for update in valid_updates:
        middle_pagenumber += findMiddle(update)

    return middle_pagenumber


def split_lines(lines: list[str]) -> tuple[list[Rule], list[Update]]:
    ruleset: list[Rule] = []
    updates: list[Update] = []

    for line in lines:
        if not len(line):
            continue
        if "|" in line:
            rule: Rule = tuple(int(val) for val in line.split("|"))
            ruleset.append(rule)
            continue
        update = [int(val) for val in line.split(",")]
        updates.append(update)
    return ruleset, updates


def day_5():
    ruleset, updates = read_input()
    print(f"Part1: {part_1(ruleset, updates)}")
    print(f"Part2: {part_2(ruleset, updates)}")


def read_input():
    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]  # Remove trailing newline characters

    ruleset, updates = split_lines(lines)
    return ruleset, updates
