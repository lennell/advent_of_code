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
    out = []

    for line in lines:
        sign = 1 if line[0] == 'R' else -1
        val = int(line[1:])
        out.append(sign * val)

    return out
    

def solve_a(lines):
    moves = parse(lines)
    count = 0
    val = 50

    for move in moves:
        val = (val + move) % 100
        if val == 0:
            count += 1

    return count


def solve_b(lines):
    moves = parse(lines)
    count = 0
    val = 50

    for move in moves:
        sign = 1 if move > 0 else -1
        length = abs(move)

        for step in range(length):
            val = (val + sign) % 100
            if val == 0:
                count += 1

    return count


def main():
    lines = []

    with open('1.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
