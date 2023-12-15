from collections import deque

pipes = []
start = False
with open("tinput", "r") as inf:
    y = 0
    for line in inf:
        pipes.append(list(line.rstrip()))
        if not start:
            if "S" in line:
                start = (line.index("S"), y)
            y += 1

bound_x = lambda x: 0 if x < 0 else len(pipes[0])-1 if x > len(pipes[0])-1 else x 
bound_y = lambda y: 0 if y < 0 else len(pipes)-1 if y > len(pipes)-1 else y 

dirs_allowed = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(0, -1), (1, 0)},
    "J": {(0, -1), (-1, 0)},
    "7": {(0, 1), (-1, 0)},
    "F": {(0, 1), (1, 0)},
    ".": {},
    "S": {(1, 0), (-1, 0), (0, 1), (0, -1)},
}

entry_allowed = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(0, 1), (-1, 0)},
    "J": {(0, 1), (1, 0)},
    "7": {(0, -1), (1, 0)},
    "F": {(0, -1), (-1, 0)},
    ".": {},
}

searched = set()
steps = [[*start, 0, "S"]]
to_search = deque((start,("SEP", "SEP")))
step = 1
while len(to_search) > 1: # sep marker
    x, y = to_search.popleft()
    if x == "SEP":
        to_search.append(("SEP", "SEP"))
        step += 1
        # print(f"==={step}===")
        continue

    searched.add((x, y))
    # print(dirs_allowed[pipes[y][x]])
    for move in dirs_allowed[pipes[y][x]]:
        new_x = bound_x(x + move[0])
        new_y = bound_y(y + move[1])
        # print(move)
        # print(pipes[new_y][new_x])
        if (new_x, new_y) in searched:
            continue
        if move in entry_allowed[pipes[new_y][new_x]]:
            to_search.append((new_x, new_y))
            steps[-1].append(move)
            steps.append([new_x, new_y, step, move]) # tracing
            if (pipes[y][x]) == "S":
                break
print(step - 1)

steps[-1].append((start[0] - steps[-1][0], start[1] - steps[-1][1]))

# walk and determine direction
turn_c = 0 # l += 1, r -=1
for x, y, s, enter, exit in steps:
    if pipes[y][x] == "L":
        if enter == (0, 1):
            turn_c += 1
        else:
            turn_c -= 1
    if pipes[y][x] == "J":
        if enter == (1, 0):
            turn_c += 1
        else:
            turn_c -= 1
    if pipes[y][x] == "7":
        if enter == (0, -1):
            turn_c += 1
        else:
            turn_c -= 1
    if pipes[y][x] == "F":
        if enter == (-1, 0):
            turn_c += 1
        else:
            turn_c -= 1

ccw = []
if turn_c > 0:
    ccw = steps[::-1]
else:
    ccw = steps

for step in ccw:
    pass

print(turn_c)
move_to_arrow = {
    (1, 0):  "→",
    (-1, 0): "←",
    (0, 1):  "↓",
    (0, -1): "↑",
    (0, 0): "X",
    "S": "S",
}

tracemap = [["." for _ in range(len(pipes[0]))] for _ in range(len(pipes))]
for x, y, s, d, pd in steps:
    tracemap[y][x] = move_to_arrow[pd]
for line in tracemap:
    print("".join(line))
