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

movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

potentials = deque()
new = set((start,))
seen = {}
old = [0, ]
for step in range(1, 131*3+1):
    potentials.extend(new)
    new = set()
    while potentials:
        cur = potentials.popleft()
        for move in movement:
            n_x, n_y = cur[0]+move[0], cur[1]+move[1]
            if garden_map[n_y%len(garden_map)][n_x%(len(garden_map[0]))] != "#":
                new.add((n_x, n_y))
    old.append(len(new))

poly = lambda n,a,b,c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
print(poly(26501365 // 131, old[65], old[65+131], old[65+131*2])) # hardcoded because I don't care anymore, 65 is constant offset, 131 is period