#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest

def validate_number(number_string):
    if len(number_string) % 2 == 1:
        return True

    half_length = len(number_string) // 2
    if number_string[:half_length] == number_string[half_length:]:
        return False

    return True

def get_invalid_ids(range_string):
    range_list = range_string.split("-")
    start = int(range_list[0])
    end = int(range_list[1])
    invalid_ids = []
    for n in range(start, end+1):
        if not validate_number(str(n)):
            invalid_ids.append(n)
    return invalid_ids


def validate_number2(number_string):
    half_length = len(number_string) // 2
    for len_substr in range(1, half_length+1):
        if (len(number_string) % len_substr) == 0:
            num_substrings = len(number_string) // len_substr
            strings = [number_string[i*len_substr : i*len_substr+len_substr] for i in range(num_substrings)]
            if len(set(strings)) <= 1:
                return False
    return True

def get_invalid_ids2(range_string):
    range_list = range_string.split("-")
    start = int(range_list[0])
    end = int(range_list[1])
    invalid_ids = []
    for n in range(start, end+1):
        if not validate_number2(str(n)):
            invalid_ids.append(n)
    return invalid_ids

@hf.timing
def part1(data):
    ranges = data[0].split(",")
    invalid_ids = []
    for r in ranges:
        invalid_ids.extend(get_invalid_ids(r))
    return sum(invalid_ids)

@hf.timing
def part2(data):
    ranges = data[0].split(",")
    invalid_ids = []
    for r in ranges:
        invalid_ids.extend(get_invalid_ids2(r))
    return sum(invalid_ids)

## Unit tests ########################################################

@pytest.mark.parametrize("test_input,expected", [("11", False),
                                                 ("22", False),
                                                 ("99", False),
                                                 ("1010", False),
                                                 ("1188511885", False),
                                                 ("222222", False),
                                                 ("446446", False),
                                                 ("38593859", False),
                                                 ("2345", True),
                                                 ("531", True),
                                                 ("5115", True)])
def test_validate_number(test_input, expected):
    assert validate_number(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("11-22", [11,22]),
    ("95-115", [99]),
    ("998-1012", [1010]),
    ("1188511880-1188511890", [1188511885]),
    ("222220-222224", [222222]),
    ("1698522-1698528", []),
    ("446443-446449", [446446]),
    ("38593856-38593862", [38593859])
])
def test_get_invalid_ids(test_input, expected):
    assert get_invalid_ids(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("11", False),
                                                 ("22", False),
                                                 ("99", False),
                                                 ("111", False),
                                                 ("999", False),
                                                 ("1010", False),
                                                 ("1188511885", False),
                                                 ("222222", False),
                                                 ("446446", False),
                                                 ("38593859", False),
                                                 ("565656", False),
                                                 ("824824824", False),
                                                 ("2121212121", False),
                                                 ("2345", True),
                                                 ("531", True),
                                                 ("5115", True),
                                                 ])
def test_validate_number2(test_input, expected):
    assert validate_number2(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("11-22", [11,22]),
    ("95-115", [99,111]),
    ("998-1012", [999,1010]),
    ("1188511880-1188511890", [1188511885]),
    ("222220-222224", [222222]),
    ("1698522-1698528", []),
    ("446443-446449", [446446]),
    ("38593856-38593862", [38593859]),
    ("565653-565659", [565656]),
    ("824824821-824824827", [824824824]),
    ("2121212118-2121212124", [2121212121]),
])
def test_get_invalid_ids2(test_input, expected):
    assert get_invalid_ids2(test_input) == expected

@pytest.fixture
def input():
    return ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]

def test_part1(input):
    assert part1(input) == 1227775554

def test_part2(input):
    assert part2(input) == 4174379265

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
