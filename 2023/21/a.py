import itertools
from collections import deque

garden_map = []
cur_x, cur_y = 0, 0
start = (0, 0)
with open("input", "r") as inf:
    for line in inf:
        garden_map.append(list(line.rstrip()))
        if "S" in line:
            start = (line.index("S"), cur_y)
        cur_y += 1

# for line in garden_map:
#     print("".join(line))

bound_x = lambda x: 0 if x < 0 else len(garden_map[0])-1 if x > len(garden_map[0])-1 else x
bound_y = lambda y: 0 if y < 0 else len(garden_map)-1 if y > len(garden_map)-1 else y
in_bound_x = lambda x: x == bound_x(x)
in_bound_y = lambda y: y == bound_y(y)

movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

potentials = deque()
new = set((start,))
for _ in range(64):
    potentials.extend(new)
    new = set()
    while potentials:
        cur = potentials.popleft()
        if cur == "MARKER":
            break
        for move in movement:
            n_x, n_y = cur[0]+move[0], cur[1]+move[1]
            if in_bound_x(n_x) and in_bound_y(n_y) and garden_map[n_y][n_x] != "#":
                new.add((n_x, n_y))
        
print(len(set(new)))