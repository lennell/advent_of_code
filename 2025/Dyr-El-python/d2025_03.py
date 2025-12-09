from aoc_prepare import PrepareAoc

test_inp_1 = """987654321111111
811111111111119
234234234234278
818181911112111"""
test_inp_2 = test_inp_1


def parse_input(inp):
    return inp.splitlines()


def part1(inp):
    data = parse_input(inp)
    total = 0
    for row in data:
        mx = max(int(c) for c in row[:-1])
        total += mx * 10 + max(int(c) for c in row[row.index(str(mx)) + 1:])
    return total
        

def part2(inp):
    data = parse_input(inp)
    total = 0
    for row in data:
        row_total = 0
        start_idx = 0
        for i in range(12):
            mx = max(int(c) for c in row[start_idx:len(row) - 11 + i])
            row_total = row_total * 10 + mx
            start_idx = row.index(str(mx), start_idx, len(row) - 11 + i) + 1
        total += row_total
    return total
    


def test_1_1():
    assert part1(test_inp_1) == 357


def test_1_2():
    assert part2(test_inp_2) == 3121910778619


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 3)
    main(prep.get_content())