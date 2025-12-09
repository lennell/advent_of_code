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
    return [list(line.rstrip()) for line in lines]
    

def solve_a(lines):
    grid = parse(lines)
    height, width = dimensions(grid)

    score = 0
    seen = set()

    for y, x in product(range(height), range(width)):
        if (y, x) in seen:
            continue

        crop = grid[y][x]
        aseen = {(y, x)}
        frontier = [(y, x)]

        for cy, cx in frontier:
            for ny, nx in neighs_bounded(cy, cx, 0, height-1, 0, width-1):
                if (ny, nx) in seen or grid[ny][nx] != crop:
                    continue

                seen.add((ny, nx))
                aseen.add((ny, nx))
                frontier.append((ny, nx))

        area = len(aseen)
        perimeter = 0

        for cy, cx in aseen:
            for ny, nx in neighs(cy, cx):
                if (ny, nx) not in aseen:
                    perimeter += 1

        score += area*perimeter

    return score


def solve_b(lines):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    grid = parse(lines)
    height, width = dimensions(grid)

    score = 0
    seen = set()

    for y, x in product(range(height), range(width)):
        if (y, x) in seen:
            continue

        crop = grid[y][x]
        aseen = {(y, x)}
        frontier = [(y, x)]

        for cy, cx in frontier:
            for ny, nx in neighs_bounded(cy, cx, 0, height-1, 0, width-1):
                if (ny, nx) in seen or grid[ny][nx] != crop:
                    continue

                seen.add((ny, nx))
                aseen.add((ny, nx))
                frontier.append((ny, nx))

        area = len(aseen)
        sides = 0
        sy = y
        sx = x
        d = 0

        while True:
            dy, dx = directions[d]

            if (sy+dy, sx+dx) in aseen:
                sy += dy
                sx += dx
            else:
                d = (d+1) % 4
                sides += 1

            if sy == y and sx == x and d == 0:
                break
        print(crop, area, sides)
        score += area*sides

    return score


def main():
    lines = []

    with open('12.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
