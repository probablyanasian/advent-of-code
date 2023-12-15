from collections import deque

pipes = []
start = False
with open("input", "r") as inf:
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
steps[-1].append((start[0] - steps[-1][0], start[1] - steps[-1][1]))

print(step - 1)

exp_mapping = {
    "|": [".X.", ".X.", ".X."],
    "-": ["...", "XXX", "..."],
    "L": [".X.", ".XX", "..."],
    "J": [".X.", "XX.", "..."],
    "7": ["...", "XX.", ".X."],
    "F": ["...", ".XX", ".X."],
    "S": [".X.", "XXX", ".X."],
}

# expand out, with a blank boundary
expand = [["." for _ in range(3*len(pipes[0])+2)] for _ in range(3*len(pipes)+2)]
for x, y, s, enter, exit in steps:
    for off_y in range(3):
        for off_x in range(3):
            expand[y*3+off_y+1][x*3+off_x+1] = exp_mapping[pipes[y][x]][off_y][off_x]

bound_x_exp = lambda x: 0 if x < 0 else len(expand[0])-1 if x > len(expand[0])-1 else x 
bound_y_exp = lambda y: 0 if y < 0 else len(expand)-1 if y > len(expand)-1 else y 

# # fill
searched = set()
to_search = [(0, 0)]
while len(to_search) > 0:
    x, y = to_search.pop()
    for move in dirs_allowed["S"]:
        new_x = bound_x_exp(x+move[0])
        new_y = bound_y_exp(y+move[1])

        if (new_x, new_y) in searched:
            continue

        if expand[new_y][new_x] == ".":
            expand[new_y][new_x] = "X"
        else:
            continue
        searched.add((new_x, new_y))
        to_search.append((new_x, new_y))

inners = 0
for y in range(len(pipes)):
    for x in range(len(pipes[0])):
        if expand[3*y+2][3*x+2] == ".":
            inners += 1
print(inners)

# move_to_arrow = {
#     (1, 0):  "→",
#     (-1, 0): "←",
#     (0, 1):  "↓",
#     (0, -1): "↑",
#     (0, 0): "X",
#     "S": "S",
# }

# tracemap = [["." for _ in range(len(pipes[0]))] for _ in range(len(pipes))]
# for x, y, s, enter, exit in steps:
#     tracemap[y][x] = move_to_arrow[exit]
# for line in tracemap:
#     print("".join(line))
