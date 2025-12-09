from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import combinations

from helpers import overlap


@dataclass
class SearchResult:
    success: bool
    path: list[object]
    cost: int
    end_state: object
    path_length: int


def unroll(node, previous):
    path = []

    while node in previous:
        path.append(node)
        node = previous[node]

    return path[::-1]


def sssp(start, goal_function, step_finder):
    previous = {}
    frontier = [(0, start, None)]

    while frontier:
        steps, position, prev = heappop(frontier)

        if position in previous:
            continue

        previous[position] = prev

        if goal_function(position):
            path = unroll(position, previous)
            return SearchResult(True, path, steps, position, len(path))

        for cost, next_step in step_finder(position):
            if next_step in previous:
                continue

            heappush(frontier, (steps+cost, next_step, position))

    return SearchResult(False, [], -1, None, -1)


def custsort(l, comparator):
    n = len(l)

    if n < 2:
        return l

    a = l[:n//2]
    b = l[n//2:]

    ll = []

    la = len(a)
    lb = len(b)
    pa = 0
    pb = 0
    sa = custsort(a, comparator)
    sb = custsort(b, comparator)

    while pa < la and pb < lb:
        comp = comparator(sa[pa], sb[pb])

        if comp > 0:
            ll.append(sb[pb])
            pb += 1
        else:
            ll.append(sa[pa])
            pa += 1

    while pa < la:
        ll.append(sa[pa])
        pa += 1
    while pb < lb:
        ll.append(sb[pb])
        pb += 1

    return ll


def a_star(start, step_finder, heuristic):
    answers = []
    frontier = [(heuristic(start), 0, start, None, {})]

    while frontier:
        best_possible, steps, state, prev, previous = heappop(frontier)

        if answers and answers[0].path_length < steps:
            break

        # if state in previous:
        #     continue

        previous[state] = prev

        if best_possible == steps:
            path = unroll(state, previous)
            answers.append(SearchResult(True, path, steps, state, len(path)))
            continue
        
        for next_state, cost in step_finder(state):
            if next_state in previous:
                continue

            h = heuristic(next_state)

            heappush(frontier, (h + steps + cost, steps + cost, next_state, state, dict(previous)))

    return answers


def merge_ranges(ranges):
    while True:
        found = False

        for i, j in combinations(range(len(ranges)), 2):
            a, b = ranges[i], ranges[j]

            if overlap(a, b):
                merged = [min(a[0], b[0]), max(a[1], b[1])]
                ranges = ranges[:i] + [merged] + ranges[i+1:j] + ranges[j+1:]
                found = True
                break

        if not found:
            return ranges
        

def union_find(edges):
    @dataclass
    class UnionFindNode:
        leader: str
        size: int

    nodes = {}

    def find(key):
        compression = []

        while nodes[key].leader != key:
            compression.append(key)
            key = nodes[key].leader

        for compressee in compression:
            nodes[compressee].leader = key

        return key
    
    def union(a, b):
        alead = find(a)
        blead = find(b)

        if alead == blead:
            return
        
        asize = nodes[alead].size
        bsize = nodes[blead].size

        newlead, newfollow = alead, blead

        if bsize > asize:
            newlead, newfollow = newfollow, newlead

        nodes[newfollow].leader = newlead
        nodes[newlead].size = asize+bsize

    for a, b in edges:
        if a not in nodes:
            nodes[a] = UnionFindNode(a, 1)
        if b not in nodes:
            nodes[b] = UnionFindNode(b, 1)

        union(a, b)
        
    return nodes