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
    groups = grouped_lines(lines)
    machines = []

    for group in groups:
        a = ints(group[0])
        b = ints(group[1])
        prize = ints(group[2])
        machines.append((a, b, tuple(prize)))

    return machines
    

def solve_a(lines):
    acost = 3
    bcost = 1
    machines = parse(lines)

    def solve(machine):
        a, b, prize = machine
        limit = 100
        costseen = {(0, 0): 0}
        aseen = {(0, 0): 0}
        bseen = {(0, 0): 0}
        frontier = [(0, 0, 0, 0, 0)]

        while frontier:
            cost, amoves, bmoves, y, x = heappop(frontier)

            if (y, x) == prize:
                return cost
            
            if amoves == limit:
                continue

            if bmoves == limit:
                continue

            if y > prize[0] or x > prize[1]:
                continue
            
            actions = [(cost+acost, amoves+1, bmoves, y+a[0], x+a[1]), (cost+bcost, amoves, bmoves+1, y+b[0], x+b[1])]

            for mcost, mamoves, mbmoves, my, mx in actions:
                if (my, mx) in aseen and aseen[(my, mx)] <= mamoves and (my, mx) in bseen and bseen[(my, mx)] <= mbmoves and (my, mx) in costseen and costseen[(my, mx)] <= mcost:
                    continue

                if (my, mx) not in aseen or aseen[(my, mx)] > mamoves:
                    aseen[(my, mx)] = mamoves

                if (my, mx) not in bseen or bseen[(my, mx)] > mbmoves:
                    bseen[(my, mx)] = mbmoves

                if (my, mx) not in costseen or costseen[(my, mx)] > mcost:
                    costseen[(my, mx)] = mcost

                heappush(frontier, (mcost, mamoves, mbmoves, my, mx))
            
        return 0
    
    return sum(solve(machine) for machine in machines)


def solve_b(lines):
    acost = 3
    bcost = 1
    added = 10000000000000
    machines = parse(lines)

    def solve(machine):
        a, b, prize = machine
        ay, ax = a
        by, bx = b
        y, x = prize
        y += added
        x += added

        solution = solve_system([[ay, by, y], [ax, bx, x]])

        if not solution[0] or solution[1][0].denominator > 1 or solution[1][1].denominator > 1:
            return 0
        
        return solution[1][0].numerator * acost + solution[1][1].numerator * bcost

    return sum(solve(machine) for machine in machines)


def main():
    lines = []

    with open('13.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())