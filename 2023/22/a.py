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

# deps = []
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
    # deps.append(min_l)

# for layer in brick_stack:
#     for line in layer:
#         for cell in line:
#             if type(cell) == str:
#                 print(cell, end="")
#             else:
#                 print(cell[0], end="")
#         print("")
#     print("-----layer divider-----")

# print(bricks)
possible = [i for i in range(len(bricks))]
for layer in brick_stack:
    for line in layer:
        for cell in line:
            if type(cell) == list:
                if len(set(cell[1])) == 1:
                    if cell[1][0] in possible:
                        possible.remove(cell[1][0])

# print(possible)
print(len(possible))