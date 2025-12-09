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
    return [list(line.rstrip()) for line in lines]
    

def solve_a(lines):
    grid = parse(lines)
    height, width = dimensions(grid)
    sy, sx = find_in_grid(grid, 'S')
    ey, ex = find_in_grid(grid, 'E')

    def goal_function(position):
        return position == (ey, ex)
    
    def step_finder(position):
        return [(1, (y, x)) for y, x in neighs_bounded(position[0], position[1], 0, height-1, 0, width-1) if grid[y][x] != '#']
    
    base = sssp((sy, sx), goal_function, step_finder).cost
    count = 0

    for y, x in product(range(height), range(width)):
        if grid[y][x] != '#':
            continue

        grid[y][x] = '.'
        cost = sssp((sy, sx), goal_function, step_finder).cost

        if cost + 100 <= base:
            count += 1

        grid[y][x] = '#'

    return count


def solve_b(lines):
    grid = parse(lines)
    height, width = dimensions(grid)
    sy, sx = find_in_grid(grid, 'S')
    ey, ex = find_in_grid(grid, 'E')
    distances = {(ey, ex): 0}
    frontier = [(0, ey, ex)]

    for steps, y, x in frontier:
        for ny, nx in neighs_bounded(y, x, 0, height-1, 0, width-1):
            if grid[ny][nx] != '#' and (ny, nx) not in distances:
                distances[(ny, nx)] = steps+1
                frontier.append((steps+1, ny, nx))

    count = 0
    max_cheat = 20
    min_save = 100
    
    for y, x in product(range(height), range(width)):
        if grid[y][x] == '#':
            continue

        for dy in range(-max_cheat, max_cheat+1):
            remaining = max_cheat - abs(dy)
            for dx in range(-remaining, remaining+1):
                if y+dy < 0 or y+dy >= height or x+dx < 0 or x+dx >= width or grid[y+dy][x+dx] == '#':
                    continue

                steps = abs(dy) + abs(dx)
                diff = distances[(y, x)] - distances[(y+dy, x+dx)]

                if diff-steps >= min_save:
                    count += 1
        
    return count


def main():
    lines = []

    with open('20.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
