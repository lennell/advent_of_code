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
    rawranges, ingredients = grouped_lines(lines)
    ranges = []
    
    for r in rawranges:
        ranges.append(list(map(int, r.split('-'))))

    return ranges, list(map(int, ingredients))
    

def solve_a(lines):
    ranges, ingredients = parse(lines)

    count = 0

    for ingredient in ingredients:
        for a, b in ranges:
            if a <= ingredient <= b:
                count += 1
                break

    return count


def solve_b(lines):
    ranges, _ = parse(lines)

    count = 0
    events = []

    for a, b in ranges:
        heappush(events, (a, True))
        heappush(events, (b, False))

    prev = 0
    open = 0

    while events:
        id, opening = heappop(events)

        if opening:
            if not open:
                prev = id
            open += 1
        else:
            open -= 1
            if not open:
                count += id - prev + 1
            
    return count


def main():
    lines = []

    with open('5.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
