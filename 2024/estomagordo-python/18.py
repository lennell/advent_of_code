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
    return [tuple(ints(line)) for line in lines]
    

def solve_a(lines):
    miny = 0
    maxy = 70
    minx = 0
    maxx = 70

    corrupted = parse(lines)
    fallen = set(pair for pair in corrupted[:1024])

    def step_finder(position):
        y, x = position

        for ny, nx in neighs_bounded(y, x, miny, maxy, minx, maxx):
            if (ny, nx) not in fallen:
                yield (1, (ny, nx))

    def goal_function(position):
        return position == (maxy, maxx)
    
    result = sssp((miny, minx), goal_function, step_finder)

    return result.cost


def solve_b(lines):
    miny = 0
    maxy = 70
    minx = 0
    maxx = 70

    corrupted = parse(lines)

    def tryworks(ci):
        fallen = set(tuple(pair) for pair in corrupted[:ci])

        def step_finder(position):
            y, x = position

            for ny, nx in neighs_bounded(y, x, miny, maxy, minx, maxx):
                if (ny, nx) not in fallen:
                    yield (1, (ny, nx))

        def goal_function(position):
            return position == (maxy, maxx)
        
        result = sssp((miny, minx), goal_function, step_finder)

        return result.success
    
    minci = 1025
    maxci = len(corrupted)
    
    while minci<maxci:
        ci = (minci+maxci)//2

        success = tryworks(ci)

        if success:
            minci = ci+1
        else:
            maxci = ci-1

    return ','.join(str(val) for val in corrupted[minci])


def main():
    lines = []

    with open('18.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
