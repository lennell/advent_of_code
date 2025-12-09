from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, words


def parse(lines):
    return ints(lines[0])
    

def solve_a(lines):
    times = 25
    nums = parse(lines)

    @cache
    def stones(remaining, value):
        if remaining == 0:
            return 1
        
        if value == 0:
            return stones(remaining-1, 1)
        
        s = str(value)
        n = len(s)
        
        if n % 2 == 0:
            a = s[:n//2]
            b = s[n//2:]

            return stones(remaining-1, int(a)) + stones(remaining-1, int(b))
        
        return stones(remaining-1, value*2024)
    
    return sum(stones(times, value) for value in nums)


def solve_b(lines):
    times = 75
    nums = parse(lines)

    @cache
    def stones(remaining, value):
        if remaining == 0:
            return 1
        
        if value == 0:
            return stones(remaining-1, 1)
        
        s = str(value)
        n = len(s)
        
        if n % 2 == 0:
            a = s[:n//2]
            b = s[n//2:]

            return stones(remaining-1, int(a)) + stones(remaining-1, int(b))
        
        return stones(remaining-1, value*2024)
    
    return sum(stones(times, value) for value in nums)


def main():
    lines = []

    with open('11.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
