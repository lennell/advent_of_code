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
    return [int(line) for line in lines]
    

def solve_a(lines):
    numbers = parse(lines)

    def simulate(number, times=2000):
        for _ in range(times):
            number ^= (number * 64)
            number %= 16777216
            number ^= (number // 32)
            number %= 16777216
            number ^= (number * 2048)
            number %= 16777216

        return number

    return sum(simulate(number) for number in numbers)


def solve_b(lines):
    numbers = parse(lines)
    global_fours = defaultdict(int)

    def simulate(number, times=2000):
        local_fours = {}
        last = -1
        diffs = []

        for _ in range(times):
            number ^= (number * 64)
            number %= 16777216
            number ^= (number // 32)
            number %= 16777216
            number ^= (number * 2048)
            number %= 16777216
            lastdig = number%10

            if last > -1:
                diffs.append(lastdig-last)

            if len(diffs) > 3:
                key = tuple(diffs[-4:])
                if key not in local_fours:
                    local_fours[key] = lastdig

            last = lastdig

        for k, v in local_fours.items():
            global_fours[k] += v

    for number in numbers:
        simulate(number)

    return max(v for v in global_fours.values())


def main():
    lines = []

    with open('22.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
