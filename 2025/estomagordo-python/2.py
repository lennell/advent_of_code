from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def really_invalid(n):
    s = str(n)
    l = len(s)

    for x in range(1, l):
        if l % x == 0 and len(set(chunks(s, x))) == 1:
            return True
        
    return False


def invalid(n):
    s = str(n)
    l = len(s)

    return l % 2 == 0 and s[:l//2] == s[l//2:]

def parse(lines):
    ranges = []

    for pairs in lines[0].split(','):
        a, b = map(int, pairs.split('-'))
        ranges.append((a,b))

    return ranges
    

def solve_a(lines):
    ranges = parse(lines)
    total = 0

    for a, b in ranges:
        for n in range(a, b+1):
            if invalid(n):
                total += n

    return total


def solve_b(lines):
    ranges = parse(lines)
    total = 0

    for a, b in ranges:
        for n in range(a, b+1):
            if really_invalid(n):
                total += n

    return total


def main():
    lines = []

    with open('2.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())

# b 45275536578 too low