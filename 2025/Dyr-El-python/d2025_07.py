from aoc_prepare import PrepareAoc
from utils.parse import parse_lines
from utils.grid import Grid2D
from utils.vec import Vec2D
from collections import deque


test_inp_1 = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
test_inp_2 = test_inp_1


def parse_input(inp):
    grid = Grid2D(inp, def_inside=".", def_outside=".")
    start = grid.find("S")[0]
    return grid, start


def part1(inp):
    grid, start = parse_input(inp)
    visited = {start}
    splits = 0
    down = Vec2D(0, 1)
    left, right = Vec2D(-1, 0), Vec2D(1, 0)
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        nxt = pos + down
        if nxt not in grid:
            continue
        if grid[nxt] == "^" and nxt not in visited:
            split = nxt + right, nxt + left
            splits += 1
            for s in split:
                if s not in visited:
                    visited.add(s)
                    queue.append(s)
        elif grid[nxt] == ".":
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return splits

def part2(inp):
    grid, start = parse_input(inp)
    visited = {start: 1}
    down = Vec2D(0, 1)
    left, right = Vec2D(-1, 0), Vec2D(1, 0)
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        nxt = pos + down
        if nxt not in grid:
            continue
        if grid[nxt] == "^" and nxt not in visited:
            split = nxt + right, nxt + left
            for s in split:
                if s not in visited:
                    visited [s] = visited[pos]
                    queue.append(s)
                else:
                    visited[s] += visited[pos]
        elif grid[nxt] == ".":
            if nxt not in visited:
                visited[nxt] = visited[pos]
                queue.append(nxt)
            else:
                visited[nxt] += visited[pos]
    return sum(v for p, v in visited.items() if p.y == grid.max_y)


def test_1_1():
    assert part1(test_inp_1) == 21


def test_1_2():
    assert part2(test_inp_2) == 40


def main(inp):
    print("Part1:", part1(inp))
    print("Part2:", part2(inp))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 7)
    main(prep.get_content())