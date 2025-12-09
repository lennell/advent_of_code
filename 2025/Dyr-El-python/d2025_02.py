from aoc_prepare import PrepareAoc


test_inp_1 = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
test_inp_2 = test_inp_1

def parse_input(inp):
    for r in inp.split(","):
        yield range(int(r.split("-")[0]),int(r.split("-")[1])+1)
    

def part1(inp):
    total = 0
    for r in parse_input(inp):
        for i in r:
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                total += i
    return total

def part2(inp):
    total = 0
    for r in parse_input(inp):
        for i in r:
            s = str(i)
            isinvalid = False
            for j in range(1, len(s)):
                if len(s) % j == 0 and s[:j] * (len(s) // j) == s:
                    isinvalid = True
            if isinvalid:
                total += i
    return total


def test_1_1():
    assert part1(test_inp_1) == 1227775554


def test_1_2():
    assert part2(test_inp_2) == 4174379265


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 2)
    main(prep.get_content())