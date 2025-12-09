from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def parse(lines):
    return [ints(line) for line in lines]
    

def solve_a(lines):
    width = 101
    height = 103
    midx = width//2
    midy = height//2
    time = 100
    robots = parse(lines)

    for _ in range(time):
        for i, robot in enumerate(robots):
            x, y, dx, dy = robot
            nx = (x+dx)%width
            ny = (y+dy)%height

            robots[i][0] = nx
            robots[i][1] = ny

    quadrants = [0, 0, 0, 0]

    for x, y, _, _ in robots:
        if x == midx or y == midy:
            continue

        quadrant = 2 * (x > midx) + (y > midy)
        quadrants[quadrant] += 1

    return multall(quadrants)


def solve_b(lines):
    width = 101
    height = 103
    robots = parse(lines)
    t = 0

    while True:
        seen = set()
        collided = False

        for i, robot in enumerate(robots):
            x, y, dx, dy = robot
            nx = (x+dx)%width
            ny = (y+dy)%height

            robots[i][0] = nx
            robots[i][1] = ny

            if (nx, ny) in seen:
                collided = True

            seen.add((nx, ny))

        t += 1

        if not collided:
            return t

def main():
    lines = []

    with open('14.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
