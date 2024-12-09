from pathlib import Path


def is_safe(report: list[int]) -> bool:
    report2 = sorted(report)
    if report2 != report:
        report2 = sorted(report, reverse=True)
        if report2 != report:
            return False

    s = set(report)
    if len(s) < len(report):
        return False

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3:
            return False

    return True


def part_1(reports) -> int:
    save_reports = 0

    for report in reports:
        if is_safe(report):
            save_reports += 1

    return save_reports


def part_2(reports) -> int:
    save_reports = 0

    for report in reports:
        if is_safe(report):
            save_reports += 1
            continue

        for i in range(len(report)):
            dampered = report.copy()
            dampered.pop(i)
            if is_safe(dampered):
                save_reports += 1
                break

    return save_reports


def day_2():
    reports = read_input()
    print(f"Part1: {part_1(reports)}")
    print(f"Part2: {part_2(reports)}")


def read_input():
    path = Path(__file__).parent.joinpath("input.txt")
    reports = []
    with open(path, "r") as f:
        for line in f:
            report = line.strip().split(" ")
            report = list(map(int, report))
            reports.append(report)

    return reports
