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
    return [list(line) for line in lines]
    

def solve_a(lines):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    grid = parse(lines)
    sy, sx = find_in_grid(grid, 'S')
    ey, ex = find_in_grid(grid, 'E')
    sdir = 0

    def heuristic(state):
        return abs(state[0]-ey) + abs(state[1]-ex)
    
    def step_finder(state):
        yield ((state[0], state[1], (state[2]+1)%4), 1000)
        yield ((state[0], state[1], (state[2]-1)%4), 1000)

        dy, dx = directions[state[2]]

        if grid[state[0]+dy][state[1]+dx] != '#':
            yield ((state[0]+dy, state[1]+dx, state[2]), 1)

    return a_star((sy, sx, sdir), step_finder, heuristic)[0].cost


def solve_b(lines):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    grid = parse(lines)
    sy, sx = find_in_grid(grid, 'S')
    ey, ex = find_in_grid(grid, 'E')
    sdir = 0

    def heuristic(state):
        return abs(state[0]-ey) + abs(state[1]-ex)
    
    def step_finder(state):
        yield ((state[0], state[1], (state[2]+1)%4), 1000)
        yield ((state[0], state[1], (state[2]-1)%4), 1000)

        dy, dx = directions[state[2]]

        if grid[state[0]+dy][state[1]+dx] != '#':
            yield ((state[0]+dy, state[1]+dx, state[2]), 1)

    solutions = a_star((sy, sx, sdir), step_finder, heuristic)
    print(len(solutions))
    on_best_path = set()

    for solution in solutions:
        for step in solution.path:
            on_best_path.add((step[0], step[1]))

    return len(on_best_path)


def main():
    lines = []

    with open('16.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())

# 467 too high
# 393 too low