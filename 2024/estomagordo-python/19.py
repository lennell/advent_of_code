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
    a, b = grouped_lines(lines)
    towels = a[0].rstrip().split(', ')
    patterns = [line.strip() for line in b]

    return towels, patterns
    

def solve_a(lines):
    towels, patterns = parse(lines)

    def can_build(pattern):
        seen = set()
        frontier = ['']

        for s in frontier:
            if s == pattern:
                return True
            
            for towel in towels:
                t = s+towel

                if t in seen:
                    continue

                if len(t) <= len(pattern) and pattern[:len(t)] == t:
                    seen.add(t)
                    frontier.append(t)

        return False
    
    return sum(can_build(pattern) for pattern in patterns)


def solve_b(lines):
    towels, patterns = parse(lines)

    @cache
    def combos(pattern):
        if not pattern:
            return 1
        
        ways = 0
        
        for towel in towels:
            if len(towel) > len(pattern):
                continue

            if towel == pattern[:len(towel)]:
                ways += combos(pattern[len(towel):])

        return ways
    
    return sum(combos(pattern) for pattern in patterns)


def main():
    lines = []

    with open('19.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
