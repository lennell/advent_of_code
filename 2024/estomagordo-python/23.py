from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp, union_find
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def parse(lines):
    return [list(line.rstrip().split('-')) for line in lines]
    

def solve_a(lines):
    edges = parse(lines)
    graph = defaultdict(set)
    three_tees = set()

    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    for a, b in combinations(graph.keys(), 2):
        if b not in graph[a]:
            continue

        for c in graph[a] & graph[b]:
            if a[0] == 't' or b[0] == 't' or c[0] == 't':
                three_tees.add(tuple(sorted([a, b, c])))

    return len(three_tees)


def solve_b(lines):
    edges = parse(lines)
    graph = defaultdict(set)
    
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    largest = []

    for a in graph.keys():
        for b in graph[a]:
            for c in graph[a]:
                if c not in graph[b]:
                    continue

                clique = {a, b, c}

                for dcand in graph[c]:
                    if all(dcand in graph[node] for node in clique):
                        clique.add(dcand)

                if len(clique) > len(largest):
                    largest = sorted(clique)

    return ','.join(largest)


def main():
    lines = []

    with open('23.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
    