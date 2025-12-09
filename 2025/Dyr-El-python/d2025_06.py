from functools import reduce
from aoc_prepare import PrepareAoc
from utils.parse import parse_lines


test_inp_1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
test_inp_2 = test_inp_1


def parse_input(inp):
    return [[int(x) if x.strip().isdigit() else x for x in line.split()] for line in inp.splitlines()]


def parse_input2(inp):
    lines = inp.splitlines()
    numbers = []
    for column in range(len(lines[0]) -1, -1, -1):
        number = 0
        for row in range(len(lines)):
            if lines[row][column].isdigit():
                number = number * 10 + int(lines[row][column])
            elif lines[row][column] in ("*", "+"):
                numbers.append(number)
                yield numbers, lines[row][column]
                number = 0
                numbers = []
        if number != 0:
            numbers.append(number)

def part1(inp):
    data = parse_input(inp)
    total = 0
    for x in range(len(data[0])):
        if data[-1][x] == "*":
            total += reduce(lambda a, b: a * b, [data[y][x] for y in range(len(data)-1)], 1)
        elif data[-1][x] == "+":
            total += sum([data[y][x] for y in range(len(data)-1)])
    return total


def part2(inp):
    total = 0
    for numbers, operation in parse_input2(inp):
        if operation == "*":
            total += reduce(lambda a, b: a * b, numbers, 1)
        elif operation == "+":
            total += sum(numbers)
    return total


def test_1_1():
    assert part1(test_inp_1) == 4277556


def test_1_2():
    assert part2(test_inp_2) == 3263827


def main(inp):
    print("Part1:", part1(inp))
    print("Part2:", part2(inp))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 6)
    main(prep.get_content())
