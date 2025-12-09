#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

def get_highest_number(number_string):
    first_digit = max(number_string[:-1])
    first_digit_index = number_string.index(first_digit)
    last_digit = max(number_string[first_digit_index+1:])
    return int(first_digit+last_digit)

def get_highest_number2(number_string, num_digits):
    digits = []
    last_index = -1
    # print(f"\n\nnumber string: {number_string}, num digits: {num_digits}")
    for n in range(num_digits):
        num_digits_left = num_digits - n - 1
        if num_digits_left == 0:
            sub_str = number_string[last_index+1:]
        else:
            sub_str = number_string[last_index+1:-num_digits_left]
        # print(f"digits left: {num_digits_left}, string: {sub_str}, ", end="")
        selected_digit = max(sub_str)
        last_index = last_index + sub_str.index(selected_digit) + 1
        # print(f"iteration: {n}, index: {last_index}, digit: {selected_digit}")
        digits.append(selected_digit)

    return int("".join(digits))

@hf.timing
def part1(data):
    return sum((get_highest_number(line) for line in data))

@hf.timing
def part2(data):
    return sum((get_highest_number2(line, 12) for line in data))

## Unit tests ########################################################

@pytest.fixture
def input():
    return ["987654321111111","811111111111119","234234234234278","818181911112111"]

@pytest.mark.parametrize("test_input,expected", [
    ("987654321111111", 98),
    ("811111111111119", 89),
    ("234234234234278", 78),
    ("818181911112111", 92),])
def test_get_highest_number(test_input, expected):
    assert get_highest_number(test_input) == expected

def test_part1(input):
    assert part1(input) == 357


@pytest.mark.parametrize("test_input,expected", [
    (("987654321111111", 2), 98),
    (("811111111111119", 2), 89),
    (("234234234234278", 2), 78),
    (("818181911112111", 2), 92),
    (("987654321111111", 12), 987654321111),
    (("811111111111119", 12), 811111111119),
    (("234234234234278", 12), 434234234278),
    (("818181911112111", 12), 888911112111),
    ])
def test_get_highest_number(test_input, expected):
    assert get_highest_number2(test_input[0], test_input[1]) == expected

def test_part2(input):
    assert part2(input) == 3121910778619

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
