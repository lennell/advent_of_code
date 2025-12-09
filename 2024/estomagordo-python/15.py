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
    grid = []
    instructions = ''.join(line.rstrip() for line in b)

    for line in a:
        grid.append(list(line.rstrip()))
    
    return grid, instructions
    

def solve_a(lines):
    grid, instructions = parse(lines)
    height, width = dimensions(grid)

    y, x = find_in_grid(grid, '@')
    grid[y][x] = '.'

    for instruction in instructions:
        dy, dx = DIRECTIONS[instruction]

        next_cell = grid[y+dy][x+dx]

        match next_cell:
            case '#':
                continue
            case '.':
                y += dy
                x += dx
            case 'O':
                step = 1

                while grid[y+dy*step][x+dx*step] == 'O':
                    step += 1

                if grid[y+dy*step][x+dx*step] == '#':
                    continue

                grid[y+dy*step][x+dx*step] = 'O'
                grid[y+dy][x+dx] = '.'
                y += dy
                x += dx

    return sum(100 * y + x for y, x in product(range(height), range(width)) if grid[y][x] == 'O')


def solve_b(lines):
    base_grid, instructions = parse(lines)

    grid = []

    for row in base_grid:
        rrow = []

        for c in row:
            rrow.append(c)
            rrow.append(c)

            if c == '@':
                rrow[-1] = '.'
            if c == 'O':
                rrow[-2] = '['
                rrow[-1] = ']'

        grid.append(rrow)

    height, width = dimensions(grid)

    y, x = find_in_grid(grid, '@')
    grid[y][x] = '.'

    for instruction in instructions:
        dy, dx = DIRECTIONS[instruction]

        next_cell = grid[y+dy][x+dx]

        match next_cell:
            case '#':
                continue
            case '.':
                y += dy
                x += dx
            case _:
                frontier = [(y+dy, x+dx)]
                
                if dy != 0:
                    if next_cell == '[':
                        frontier.append((y+dy, x+dx+1))
                    else:
                        frontier.append((y+dy, x+dx-1))
                
                blocked = False

                for fy, fx in frontier:
                    nexty = fy+dy
                    nextx = fx+dx

                    if grid[nexty][nextx] == '#':
                        blocked = True
                        break
                    elif grid[nexty][nextx] in '[]':
                        frontier.append((nexty, nextx))
                        if dx != 0:
                            if grid[nexty][nextx+dx] in '[]':
                                frontier.append((nexty, nextx+dx))
                        else:
                            if grid[nexty][nextx] == '[':
                                frontier.append((nexty, nextx+1))
                            else:
                                frontier.append((nexty, nextx-1))

                if blocked:
                    continue
                
                newgrid = [list(row) for row in grid]
                for fy, fx in frontier:
                    newgrid[fy+dy][fx+dx] = grid[fy][fx]
                    if (fy-dy, fx-dx) not in frontier:
                        newgrid[fy][fx] = '.'
                
                grid = newgrid

                y += dy
                x += dx

    for row in grid:
        print(''.join(row))
    return sum(100 * y + x for y, x in product(range(height), range(width)) if grid[y][x] == '[')


def main():
    lines = []

    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())