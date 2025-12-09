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
    return [list(line.rstrip()) for line in lines]


def solve_a(lines):
    grid = parse(lines)

    h = len(grid)
    w = len(grid[0])
    count = 0

    for y, x in product(range(h), range(w)):
        if grid[y][x] == '@' and sum(grid[i][j] == '@' for i,j in eight_neighs_bounded(y, x, 0, h-1, 0, w-1)) < 4:
            count += 1

    return count


def solve_b(lines):
    grid = parse(lines)

    h = len(grid)
    w = len(grid[0])
    count = 0

    removing = True
    while removing:
        removing = False
        to_remove = []

        for y, x in product(range(h), range(w)):
            if grid[y][x] == '@' and sum(grid[i][j] == '@' for i,j in eight_neighs_bounded(y, x, 0, h-1, 0, w-1)) < 4:
                to_remove.append((y, x))
                count += 1

        for y, x in to_remove:
            removing = True
            grid[y][x] = '.'

    return count


def main():
    lines = []

    with open('4.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
