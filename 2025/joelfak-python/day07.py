#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
import numpy as np
from pprint import pprint

@hf.timing
def part1(data):
    beams = np.array(list(data[0])) == "S"
    splitters = np.array([list(row) for row in data]) == "^"

    split_count = 0
    print()
    for row_splitters in splitters:
        splitters_hit = np.logical_and(beams, row_splitters)
        split_count += np.sum(splitters_hit)
        split_beams_left = np.concatenate((splitters_hit[1:], [False]))
        split_beams_right = np.concatenate(([False], splitters_hit[:-1]))
        # print("beams\t\t\t", [int(v) for v in beams])
        # print("splitters\t\t", [int(v) for v in row_splitters])
        # print("split_beams_left\t", [int(v) for v in split_beams_left])
        # print("split_beams_right\t", [int(v) for v in split_beams_right])

        beams = np.logical_or(beams, split_beams_left)
        beams = np.logical_or(beams, split_beams_right)
        beams = np.logical_or(beams, split_beams_right)
        beams = np.logical_and(beams, np.logical_not(splitters_hit))

    return split_count

@hf.timing
def part2(data):
    beams = np.array(list(data[0])) == "S"
    splitters = np.array([list(row) for row in data]) == "^"

    split_count = 0
    print()
    for row_splitters in splitters:
        splitters_hit = beams * row_splitters
        beams_not_split = beams * np.logical_not(row_splitters)
        split_beams_left = np.concatenate((splitters_hit[1:], [0]))
        split_beams_right = np.concatenate(([0], splitters_hit[:-1]))
        # print("beams\t\t\t", [int(v) for v in beams])
        # print("splitters\t\t", [int(v) for v in row_splitters])
        # print("beams_not_split\t\t", [int(v) for v in beams_not_split])
        # print("split_beams_left\t", [int(v) for v in split_beams_left])
        # print("split_beams_right\t", [int(v) for v in split_beams_right])

        beams = beams_not_split + split_beams_left + split_beams_right
        # print("beams\t\t\t", [int(v) for v in beams])

    return np.sum(beams)

## Unit tests ########################################################

@pytest.fixture
def input():
    return [".......S.......",
            "...............",
            ".......^.......",
            "...............",
            "......^.^......",
            "...............",
            ".....^.^.^.....",
            "...............",
            "....^.^...^....",
            "...............",
            "...^.^...^.^...",
            "...............",
            "..^...^.....^..",
            "...............",
            ".^.^.^.^.^...^.",
            "..............."]

@pytest.mark.parametrize("test_input,expected", [(35, 35),
                                                 (26, 26)])
def test_help_function(test_input, expected):
    # assert test_input == expected
    pass

# def test_part1(input):
#     assert part1(input) == 21

def test_part2(input):
    assert part2(input) == 40

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
