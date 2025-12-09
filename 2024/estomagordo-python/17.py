from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm, log

from algo import a_star, custsort, merge_ranges, sssp
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def parse(lines):
    registers, program = grouped_lines(lines)
    a = ints(registers[0])[0]
    b = ints(registers[1])[0]
    c = ints(registers[2])[0]
    code = ints(program[0])

    return a, b, c, code
    

def solve_a(lines):
    a, b, c, code = parse(lines)
    n = len(code)
    out = []
    pointer = 0

    def combo(val):
        match val:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                return val
        
    while 0 <= pointer < n:
        opcode = code[pointer]
        operand = code[pointer+1]
        move_pointer = True

        match opcode:
            case 0:
                a //= 2**combo(operand)
            case 1:
                b ^= operand
            case 2:
                b = combo(operand)%8
            case 3:
                if a != 0:
                    pointer = operand
                    move_pointer = False
            case 4:
                b ^= c
            case 5:
                out.append(combo(operand)%8)
            case 6:
                b = a // 2**combo(operand)
            case 7:
                c = a // 2**combo(operand)

        if move_pointer:
            pointer += 2
            
    return ','.join(str(val) for val in out)


def solve_b(lines):
    _, _, _, code = parse(lines)
    n = len(code)
            
    def run(a):
        b = 0
        c = 0

        def combo(val):
            match val:
                case 4:
                    return a
                case 5:
                    return b
                case 6:
                    return c
                case _:
                    return val

        for i in range(0, len(code)-2, 2):
            opcode = code[i]
            operand = code[i+1]

            match opcode:
                case 0:
                    a //= 2**combo(operand)
                case 1:
                    b ^= operand
                case 2:
                    b = combo(operand)%8
                case 4:
                    b ^= c
                case 5:
                    return combo(operand)%8
                case 6:
                    b = a // 2**combo(operand)
                case 7:
                    c = a // 2**combo(operand)

    bmappings = defaultdict(list)
    
    for a in range(2**6):
        result = run(a)
        bmappings[result].append(a)

    frontier = [(1, a) for a in bmappings[code[0]]]
    highest = -1

    for pos, a in frontier:
        if pos == len(code):
            return a
        
        target = code[pos]

        for possa in bmappings[target]:
            mid_three = a//2**(3*pos)
            if possa%8 == mid_three:
                highest = max(highest, pos)
                top_three = possa//8
                term = top_three << (pos-1)*3+6
                frontier.append((pos+1, a+term))
            

    return len(frontier)

def main():
    lines = []

    with open('17.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())

# 4,4,2,6,5,4,3,1,7 awrong
# 2121125247610067 too high
# 2121125247610067