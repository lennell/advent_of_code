#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
import numpy as np
from typing import List
from pprint import pprint

def pad(input: np.array, value: int) -> np.array:
    return np.pad(input, pad_width=1, mode="constant", constant_values=value)

def convolute2d(input: np.array, kernel: np.array) -> np.array:
    input_height, input_width = input.shape
    kernel_height, kernel_width = kernel.shape

    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1

    output = np.zeros((output_height, output_width))
    
    # print(f"\n\nkernel:\n{kernel}\n")
    
    for r in range(output_height):
        for c in range(output_width):
            region = input[r:r+kernel_height, c:c+kernel_width]
            # print(f"r: {r}, c: {c}\n{region}\n")
            output[r,c] = np.sum(region * kernel)
    
    return output

def convolute_with_padding(input: np.array, kernel: np.array, padding: int) -> np.array:
    input = pad(input, padding)
    return convolute2d(input, kernel)

def convert_array(input: List[str]) -> np.array:
    rows = []
    for row in input:
         int_row = row.replace("@", "1").replace(".", "0")
         rows.append([int(c) for c in list(int_row)])
    return np.array(rows)

def find_accessible_rolls(input: np.array) -> np.array:
    kernel = np.array([[-1,-1,-1],
                       [-1, 5,-1],
                       [-1,-1,-1]])
    convoluted_array = convolute_with_padding(input, kernel, 0)
    accessible_rolls = convoluted_array > 1
    # print(f"input:\n{input}\n")
    # print(f"convoluted_array:\n{convoluted_array}\n")
    # print(f"accessible_rolls:\n{accessible_rolls*1}\n")
    return accessible_rolls

@hf.timing
def part1(data):
    # print("\n\data:\n")
    # pprint(data)
    input = convert_array(data)
    accessible_rolls = find_accessible_rolls(input)
    return np.sum(accessible_rolls)

@hf.timing
def part2(data):
    map = convert_array(data)
    num_removed_rolls = 0
    while True:
        # print(map)
        accessible_rolls = find_accessible_rolls(map)
        num_accessible_rolls = np.sum(accessible_rolls)
        # print(f"num_accessible_rolls: {num_accessible_rolls}")
        if num_accessible_rolls == 0:
            break
        num_removed_rolls += num_accessible_rolls
        map[accessible_rolls] = 0

    return num_removed_rolls

## Unit tests ########################################################

def test():
    test_input = np.array( [[1,2],
                            [3,4]] )
    expected = np.array( [[1,1,1,1],
                          [1,1,2,1],
                          [1,3,4,1],
                          [1,1,1,1]] )
    assert (pad(test_input, 1) == expected).all()
    
def test_convolute_with_padding():
    test_input = np.array( [[1,0,2],
                            [1,0,2],
                            [1,0,2]] )
    kernel = np.array( [[0,1,0],
                        [1,0,1],
                        [0,1,0]] )
    expected = np.array( [[1,3,2],
                          [2,3,4],
                          [1,3,2]] )
    assert (convolute_with_padding(test_input, kernel, 0) == expected).all()

def test_convert_array():
    input = ["..@.",
             ".@.@"]
    expected = np.array([[0,0,1,0],
                         [0,1,0,1]])
    assert (convert_array(input) == expected).all()

@pytest.fixture
def input():
    return ["..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@."]

def test_part1(input):
    assert part1(input) == 13

def test_part2(input):
    assert part2(input) == 43

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
