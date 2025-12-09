from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def parse(lines):
    grid = []

    for line in lines:
        if line.strip()[0].isdigit():
            grid.append(list(map(int, line.split())))
        else:
             grid.append(line.split())

    return grid


def parse_b(lines):
    starts = [x for x in range(len(lines[-1])) if lines[-1][x] != ' ']
    widest = max(len(line) for line in lines)
    cols = []

    for colindex in range(len(starts)):
        stopx = starts[colindex+1] if colindex < len(starts) - 1 else widest
        startx = starts[colindex]
        operator = lines[-1][startx]
        col = []

        for x in range(stopx-1, startx-1, -1):
            num = ''

            for line in lines:
                if x < len(line) and line[x].isdigit():
                    num += line[x]

            if num:
                col.append(int(num))

        col.append(operator)
        cols.append(col)

    return cols
    

def solve_a(lines):
    grid = parse(lines)
    h,w = dimensions(grid)

    total = 0

    for col in range(w):
        if grid[-1][col] == '*':
            val = 1
            for y in range(h-1):
                val *= grid[y][col]
            total += val
        else:
            val = 0
            for y in range(h-1):
                val += grid[y][col]
            total += val

    return total


def solve_b(lines):
    cols = parse_b(lines)

    total = 0

    for col in cols:
        if col[-1] == '*':
            val = 1
            for num in col[:-1]:
                val *= num
            total += val
        else:
            val = 0
            for num in col[:-1]:
                val += num
            total += val

    return total


def main():
    lines = []

    with open('6.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())

# 10266453446867 too high