from aoc_prepare import PrepareAoc
from utils.grid import Grid2D

test_inp_1 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
test_inp_2 = test_inp_1


def parse_input(inp):
    return (Grid2D(inp, relevant=lambda c: c in (".", "@"), def_outside="."),
            Grid2D(inp, relevant=lambda c: c in (".", "@"), def_outside=0))


def calc_neighbors(grid, neighbors):
    for pos, ch in grid.items():
        count = 0
        for delta in Grid2D.eight_directions():
            neighbor = pos + delta
            if grid.get(neighbor) == "@":
                count += 1
        neighbors[pos] = count


def part1(inp):
    result = 0
    grid, neighbors = parse_input(inp)
    calc_neighbors(grid, neighbors)
    for pos, ch in grid.items():
        if ch != "@":
            continue
        if neighbors[pos] < 4:
            result += 1
    return result


def part2(inp):
    result = 0
    grid, neighbors = parse_input(inp)
    calc_neighbors(grid, neighbors)
    changed = True
    while changed:
        changed = False
        for pos, ch in grid.items():
            if ch != "@":
                continue
            if neighbors[pos] < 4:
                grid[pos] = "."
                result += 1
                for delta in Grid2D.eight_directions():
                    neighbor = pos + delta
                    if neighbor in grid:
                        neighbors[neighbor] -= 1
                changed = True
    return result


def test_1_1():
    assert part1(test_inp_1) == 13


def test_1_2():
    assert part2(test_inp_2) == 43


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 4)
    main(prep.get_content())