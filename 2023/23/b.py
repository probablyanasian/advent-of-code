import itertools
from collections import deque
import sys
sys.setrecursionlimit(9999999)

forest_map = []
with open("input", "r") as inf:
    for line in inf:
        forest_map.append(list(line.rstrip()))

bound_x = lambda x: 0 if x < 0 else len(forest_map[0])-1 if x > len(forest_map[0])-1 else x 
bound_y = lambda y: 0 if y < 0 else len(forest_map)-1 if y > len(forest_map)-1 else y
in_bound_x = lambda x: x == bound_x(x)
in_bound_y = lambda y: y == bound_y(y)

movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Node():
    def __init__(self, loc):
        self.loc = loc
        self.edges = []

    def __repr__(self) -> str:
        return f"{self.loc}" # f"{len(self.edges)}" #

class Edge():
    def __init__(self, start, end, dist):
        self.start = start
        self.end = end
        self.other = {start: end, end: start}
        self.dist = dist

    def __repr__(self) -> str:
        return f"({self.start} -> {self.end}: {self.dist})"

nodes = {(len(forest_map[0])-2, len(forest_map)-1): Node((len(forest_map[0])-2, len(forest_map)-1))}
edges = []

seen = set()
s_node = Node((1, 0))
nodes[(1, 0)] = s_node
remaining = deque(((1, 0, 0, s_node),))
while remaining:
    cur = remaining.popleft()
    seen.add((cur[0], cur[1]))
    if (cur[0], cur[1]) == (len(forest_map[0])-2, len(forest_map)-1):
        n_edge = Edge(cur[3], nodes[(len(forest_map[0])-2, len(forest_map)-1)], cur[2])
        cur[3].edges.append(n_edge)
        nodes[(len(forest_map[0])-2, len(forest_map)-1)].edges.append(n_edge)
        edges.append(n_edge)
        continue
    added = 0
    moves = []
    for move in movement:
        n_x, n_y = cur[0]+move[0], cur[1]+move[1]
        if (n_x, n_y) in seen:
            if (n_x, n_y) in nodes and cur[2] > 1:
                n_edge = Edge(cur[3], nodes[(n_x, n_y)], cur[2]+1)
                edges.append(n_edge)
                cur[3].edges.append(n_edge)
                nodes[(n_x, n_y)].edges.append(n_edge)
            continue
        if in_bound_x(cur[0]+move[0]) and in_bound_y(cur[1]+move[1]) and forest_map[cur[1]+move[1]][cur[0]+move[0]] != "#":
            moves.append((n_x, n_y))
            added += 1
    # at a fork, create node, or find created
    if added > 1:
        n_node = Node((cur[0], cur[1]))
        nodes[(cur[0], cur[1])] = n_node
        n_edge = Edge(cur[3], n_node, cur[2])
        edges.append(n_edge)
        cur[3].edges.append(n_edge)
        n_node.edges.append(n_edge)
        for n_x, n_y in moves:
            remaining.append((n_x, n_y, 1, n_node))
    else:
        for n_x, n_y in moves:
            remaining.appendleft((n_x, n_y, cur[2]+1, cur[3])) # priority

longest = 0
def dfs(node: Node, dist: int, seen: set[Node]):
    global longest
    if node == nodes[(len(forest_map[0])-2, len(forest_map)-1)]:
        longest = max(longest, dist)
    for next in node.edges:
        if next.other[node] in seen:
            continue
        seen.add(next.other[node])
        dfs(next.other[node], dist + next.dist, seen)
        seen.remove(next.other[node])

dfs(nodes[(1, 0)], 0, set())
print(longest)
