#!/usr/bin/env python3

import helpfunctions as hf
import sys, pytest
import numpy as np
from pprint import pprint

@hf.timing
def part1(data):
    matrix = []
    operations = []
    for line in data:
        try:
            matrix.append([int(v) for v in line.split()])
        except ValueError:
            operations = line.split()
    matrix_np = np.array(matrix)
    num_rows = matrix_np.shape[0]
    operations_np = np.array(operations)
    additions = np.repeat(np.expand_dims(operations_np == "+", 0), num_rows, 0)
    products = np.repeat(np.expand_dims(operations_np == "*", 0), num_rows, 0)

    total_sum = np.sum(np.where(additions, matrix_np, 0), axis=0)
    total_product = np.prod(np.where(products, matrix_np, 0), axis=0)

    return np.sum(total_sum) + np.sum(total_product)

@hf.timing
def part2(data):
    operations = data[-1].split()
    operations_np = np.array(operations)
    
    n_rows = len(data)
    n_cols = len(data[0])

    nt_rows = n_cols
    nt_cols = n_rows-1
    transposed_data = [['' for i in range(nt_cols)] for j in range(nt_rows)]
    for ln, line in enumerate(data[:-1]):
        for cn, char in enumerate(line):
            transposed_data[cn][ln] = char
            
    numbers = [[]]
    for l in transposed_data:
        line = "".join(l).strip()
        if line != "":
            numbers[-1].append(int(line))
        else:
            numbers.append([])

    max_list_len = max((len(row) for row in transposed_data))
    for row in numbers:
        numbers_to_extend = max_list_len - len(row)
        row = row.extend([np.nan] * numbers_to_extend)
    numbers_np = np.array(numbers)

    operations_np = np.array(operations)
    additions = np.repeat(np.expand_dims(operations_np == "+", 1), numbers_np.shape[1], 1)
    products = np.repeat(np.expand_dims(operations_np == "*", 1), numbers_np.shape[1], 1)
    
    total_sum = np.nansum(np.where(additions, numbers_np, 0), axis=1)
    total_product = np.nanprod(np.where(products, numbers_np, 0), axis=1)

    return int(np.sum(total_sum) + np.sum(total_product))

## Unit tests ########################################################

@pytest.fixture
def input():
    return ["123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  "]

def test_part1(input):
    assert part1(input) == 4277556

def test_part2(input):
    assert part2(input) == 3263827

## Main ########################################################

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        input = [line.rstrip('\n') for line in f.readlines()]

    print("Advent of code day X")
    print(f"Part1 result: {part1(input.copy())}")
    print(f"Part2 result: {part2(input.copy())}")
