#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

@hf.timing
def part1(data):
    dial = 50
    dirs = {"L":-1, "R":1}
    zero_counter = 0
    for turn in data:
        direction = turn[0]
        steps = int(turn[1:])
        dial += dirs[direction] * steps
        dial = dial % 100
        if dial == 0:
            zero_counter += 1
    return zero_counter

@hf.timing
def part2(data):
    dial = 50
    dirs = {"L":-1, "R":1}
    zero_counter = 0
    print()
    for turn in data:
        print(f"dial: {dial}, turn: {turn}", end=" ")
        direction = turn[0]
        steps = int(turn[1:])
        if dial == 0:
            starts_at_zero=True
        else:
            starts_at_zero=False

        dial += dirs[direction] * steps
        if dirs[direction] == 1:
            zero_counter += dial // 100
        else:
            zero_counter += abs((dial-1) // 100)
            if starts_at_zero:
                zero_counter -= 1

        print(f"new dial: {dial}, zero_counter: {zero_counter}", end=" ")
        dial = dial % 100
        print(f" dial: {dial}")
    return zero_counter

## Unit tests ########################################################

@pytest.fixture
def input():
    return ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

# @pytest.mark.parametrize("test_input,expected", [["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"],
#                                                  ()])
# def test_help_function(test_input, expected):
#     assert test_input == expected

def test_part1(input):
    assert part1(input) == 3

def test_part2(input):
    assert part2(input) == 6

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
