from collections import deque
from copy import deepcopy

bricks = []
with open("input", "r") as inf:
    for idx, line in enumerate(inf):
        bricks.append(list(map(lambda x: tuple(map(int, x.split(","))), line.rstrip().split("~"))))
        bricks[-1].append(idx)

max_x, max_y, max_z = 0, 0, 0
for brick in bricks:
    for x, y, z in brick[:2]:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

brick_stack = [[["." for _ in range(max_x+1)] for _ in range(max_y+1)] for _ in range(max_z+1)]
for y in range(max_y+1):
    for x in range(max_x+1):
        brick_stack[0][y][x] = "#"

bricks.sort(key=lambda x: x[0][2])

deps = {}
for brick in bricks:
    b_s, b_e, b_i = brick
    z_s = b_s[2]
    min_l = []
    hit_min = False
    if b_s[0] != b_e[0]:
        while True:
            for l in range(b_s[0], b_e[0]+1):
                if brick_stack[z_s-1][b_s[1]][l] != ".":
                    min_l.append(brick_stack[z_s-1][b_s[1]][l][0])
                    hit_min = True
            if hit_min:
                break
            z_s -= 1
        for l in range(b_s[0], b_e[0]+1):
            brick_stack[z_s][b_s[1]][l] = [b_i, min_l]
    elif b_s[1] != b_e[1]:
        while True:
            for l in range(b_s[1], b_e[1]+1):
                if brick_stack[z_s-1][l][b_s[0]] != ".":
                    min_l.append(brick_stack[z_s-1][l][b_s[0]][0])
                    hit_min = True
            if hit_min:
                break
            z_s -= 1
        for l in range(b_s[1], b_e[1]+1):
            brick_stack[z_s][l][b_s[0]] = [b_i, min_l]
    else:
        while True:
            if brick_stack[z_s-1][b_s[1]][b_s[0]] != ".":
                min_l.append(brick_stack[z_s-1][b_s[1]][b_s[0]][0])
                break
            z_s -= 1
        for l in range(b_e[2]-b_s[2]+1):
            brick_stack[z_s+l][b_s[1]][b_s[0]] = [b_i, min_l]
    
    deps[b_i] = list(set(min_l))

possible_affected = 0
# copy out, pop off until none left, count affected
for s, e, potential in bricks:
    c_deps = deepcopy(deps)
    cascade = deque((potential,))
    seen = set()
    while cascade:
        cur = cascade.popleft()
        for k in c_deps:
            if cur in c_deps[k]:
                c_deps[k].remove(cur)
            if len(c_deps[k]) == 0 and k not in seen:
                cascade.append(k)
                seen.add(k)
    possible_affected += len(seen) # start

print(possible_affected)