#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

def get_range(min_max_tuple):
    return range(min_max_tuple[0], min_max_tuple[1]+1)

def is_fresh(fresh_ranges, id):
    return any((id in get_range(r) for r in fresh_ranges))

def parse_input(data):
    fresh_ranges = []
    ids = []

    read_ranges = True
    for line in data:
        if line == "":
            read_ranges = False
            continue
        if read_ranges:
            fresh_ranges.append(tuple((int(n) for n in line.split("-"))))
        else:
            ids.append(int(line))
    return fresh_ranges, ids

@hf.timing
def part1(data):
    fresh_ranges, ids = parse_input(data)
    return sum((is_fresh(fresh_ranges, id) for id in ids))

def combine_ranges(input_ranges):
    input_ranges = sorted(input_ranges, key=lambda r: r[0])
    combined_ranges = []
    # print()
    current_min, current_max = input_ranges[0]
    for r_min, r_max in input_ranges[1:]:
        if r_min <= current_max:
            current_max = max(current_max, r_max)
        else:
            combined_ranges.append((current_min, current_max))
            current_min = r_min
            current_max = r_max
        # print(min_v, max_v)

    combined_ranges.append((current_min, current_max))
    return combined_ranges

@hf.timing
def part2(data):
    fresh_ranges, _ = parse_input(data)
    combined_ranges = combine_ranges(fresh_ranges)
    return sum(r[1]-r[0]+1 for r in combined_ranges)

## Unit tests ########################################################

@pytest.fixture
def input():
    return ["3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32"]

fresh_ranges = [(3,5),
                (10,14),
                (16,20),
                (12,18)]
@pytest.mark.parametrize("test_input,expected", [((fresh_ranges, 1), False),
                                                 ((fresh_ranges, 5), True),
                                                 ((fresh_ranges, 8), False),
                                                 ((fresh_ranges, 11), True),
                                                 ((fresh_ranges, 17), True),
                                                 ((fresh_ranges, 32), False)])
def test_is_fresh(test_input, expected):
    assert is_fresh(*test_input) == expected

@pytest.mark.parametrize("test_input,expected",
                         [([(3,5),(10,14),(16,20),(12,18)],
                           [(3,5),(10,20)]),
                          ([(2,5),(8,10)],
                           [(2,5),(8,10)]),
                          ([(2,5),(8,10),(4,8)],
                           [(2,10)]),
                          ([(2,8),(3,5)],
                           [(2,8)]),
                          ([(8,10),(4,8),(2,5)],
                           [(2,10)])])
def test_combine_ranges(test_input, expected):
    assert combine_ranges(test_input) == expected

def test_part1(input):
    assert part1(input) == 3

def test_part2(input):
    assert part2(input) == 14

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
