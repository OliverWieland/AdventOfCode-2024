import os
from pathlib import Path

Input_Data = tuple[list[int], list[int]]

def read_lists() -> Input_Data:
    """
    Read two lists from a file and sort them.
    """
    list1:list[int] = []
    list2:list[int] = []

    path = Path(__file__).parent.joinpath("input.txt")
    with open(path, "r") as f:
        for line in f:
            l = line.split("   ")
            list1.append(int(l[0]))
            list2.append(int(l[1]))

    list1.sort()
    list2.sort()

    return list1, list2

    
def part1(input_data: Input_Data):
    list1, list2 = input_data
    diff = 0

    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])

    return diff


def part2(input_data: Input_Data):
    list1, list2 = input_data

    similarity_score = 0
    for element in list1:
        similarity_score += element * list2.count(element)

    return similarity_score


def day_1():
    input_data = read_lists()
            
    print(f"Part1: {part1(input_data)}")
    print(f"Part2: {part2(input_data)}")
