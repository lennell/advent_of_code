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
    return [[int(val) for val in line.rstrip()] for line in lines]
    

def solve_a(lines):
    grid = parse(lines)
    height, width = dimensions(grid)

    def score(y, x):
        if grid[y][x] != 0:
            return 0
        
        seen = {(y, x)}
        heads = set()
        frontier = [(y, x)]

        for fy, fx in frontier:
            val = grid[fy][fx]

            if val == 9:
                heads.add((fy, fx))
                continue

            for ny, nx in neighs_bounded(fy, fx, 0, height-1, 0, width-1):
                if (ny, nx) in seen or grid[ny][nx] != val+1:
                    continue

                seen.add((ny, nx))
                frontier.append((ny, nx))

        return len(heads)
    
    return sum(score(y, x) for y, x in product(range(height), range(width)))


def solve_b(lines):
    grid = parse(lines)
    height, width = dimensions(grid)

    def score(y, x):
        if grid[y][x] != 0:
            return 0
        
        seen = {((y, x),)}
        trails = set()
        frontier = [((y, x),)]

        for trail in frontier:
            fy, fx = trail[-1]
            val = grid[fy][fx]

            if val == 9:
                trails.add(trail)
                continue

            for ny, nx in neighs_bounded(fy, fx, 0, height-1, 0, width-1):
                if grid[ny][nx] != val+1:
                    continue

                newtrail = tuple(list(trail) + [(ny, nx)])

                if newtrail in seen:
                    continue

                seen.add(newtrail)
                frontier.append(newtrail)

        return len(trails)
    
    return sum(score(y, x) for y, x in product(range(height), range(width)))


def main():
    lines = []

    with open('10.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
