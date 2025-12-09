from aoc_prepare import PrepareAoc
from utils.parse import parse_lines
from utils.grid import Grid2D
from utils.vec import Vec2D
from collections import deque
from functools import reduce

test_inp_1 = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
test_inp_2 = test_inp_1


def parse_input(inp):
    data = [tuple(map(int, line.split(","))) for line in inp.splitlines()]
    return data


def part1(inp, size=1000):
    data = parse_input(inp)
    connected = set()
    dists = []
    for box1 in data:
        for box2 in data:
            if box2 <= box1:
                continue
            if (box1, box2) in connected:
                continue
            dist = (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
            dists.append((dist, (box1, box2)))
    dists.sort()
    for connect in range(size):
        closest_dist, closest_pair = dists.pop(0)
        if closest_pair in connected:
            continue
        connected.add(closest_pair)
    groups = []
    while connected:
        box1, box2 = connected.pop()
        group1 = group2 = None
        for group in groups:
            if box1 in group:
                group1 = group
            if box2 in group:
                group2 = group
        if group1 and group2 and group1 != group2:
            group1.update(group2)
            groups.remove(group2)
        elif group1:
            group1.add(box2)
        elif group2:
            group2.add(box1)
        else:
            groups.append(set((box1, box2)))
    groups_sizes = [len(g) for g in groups]
    groups_sizes.sort(reverse=True)
    return reduce(lambda x, y: x * y, groups_sizes[:3])


def part2(inp):
    data = parse_input(inp)
    connected = set()
    dists = []
    for box1 in data:
        for box2 in data:
            if box2 <= box1:
                continue
            if (box1, box2) in connected:
                continue
            dist = (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
            dists.append((dist, (box1, box2)))
    dists.sort()
    connected_boxes = set()
    groups = []
    while True:
        _, closest_pair = dists.pop(0)
        if closest_pair in connected:
            continue
        connected.add(closest_pair)
        connected_boxes.update(closest_pair)
        box1, box2 = closest_pair
        group1 = group2 = None
        for group in groups:
            if box1 in group:
                group1 = group
            if box2 in group:
                group2 = group
        if group1 and group2 and group1 != group2:
            group1.update(group2)
            groups.remove(group2)
        elif group1:
            group1.add(box2)
        elif group2:
            group2.add(box1)
        else:
            groups.append(set((box1, box2)))
        if len(groups) == 1 and len(connected_boxes) == len(data):
            return closest_pair[0][0] * closest_pair[1][0]
    return 0


def test_1_1():
    assert part1(test_inp_1, 10) == 40


def test_1_2():
    assert part2(test_inp_2) == 25272


def main(inp):
    print("Part1:", part1(inp.strip()))
    print("Part2:", part2(inp.strip()))


if __name__ == "__main__":
    prep = PrepareAoc(2025, 8)
    main(prep.get_content())