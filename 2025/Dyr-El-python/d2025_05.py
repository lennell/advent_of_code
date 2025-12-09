from aoc_prepare import PrepareAoc
from utils.parse import parse_lines


test_inp_1 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
test_inp_2 = test_inp_1


def parse_input(inp):
    return parse_lines(inp, [lambda x: list(map(int, x.split("-"))), int], split_groups="\n\n")


def part1(inp):
    rs, items = parse_input(inp)
    rs = [range(r[0], r[1] + 1) for r in rs]
    return sum(1 for item in items if any(item in r for r in rs))


def part2(inp):
    ranges, _ = parse_input(inp)
    data = []
    while ranges:
        rng = ranges.pop(0)
        no_overlap = True
        for idx, r in enumerate(data):
            if not (rng[1] < r[0] or rng[0] > r[1]):
                ranges.append((min(r[0], rng[0]), max(r[1], rng[1])))
                del data[idx]
                no_overlap = False
                break
        if no_overlap:
            data.append(rng)
    return sum((r[1] - r[0] + 1) for r in data)


def test_1_1():
    assert part1(test_inp_1) == 3


def test_1_2():
    assert part2(test_inp_2) == 14


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 5)
    main(prep.get_content())