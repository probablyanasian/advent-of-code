from collections import deque

mirror_map = []
with open("input", "r") as inf:
    for line in inf:
        mirror_map.append(line.rstrip())

bound_x = (
    lambda x: 0
    if x < 0
    else len(mirror_map[0]) - 1
    if x > len(mirror_map[0]) - 1
    else x
)
bound_y = (
    lambda y: 0 if y < 0 else len(mirror_map) - 1 if y > len(mirror_map) - 1 else y
)

# > 1, v 2, < 3, ^ 4
passed = set()
path = []
to_search = deque(((0, 0, 1),))
while len(to_search) > 0:
    cur = to_search.popleft()
    if cur in passed:
        continue
    path.append(cur)
    passed.add(cur)
    if mirror_map[cur[1]][cur[0]] == ".":
        if cur[2] == 1:
            if bound_x(cur[0] + 1) != cur[0]:
                to_search.append((cur[0] + 1, cur[1], cur[2]))
        elif cur[2] == 3:
            if bound_x(cur[0] - 1) != cur[0]:
                to_search.append((cur[0] - 1, cur[1], cur[2]))
        elif cur[2] == 2:
            if bound_x(cur[1] + 1) != cur[1]:
                to_search.append((cur[0], cur[1] + 1, cur[2]))
        elif cur[2] == 4:
            if bound_x(cur[1] - 1) != cur[1]:
                to_search.append((cur[0], cur[1] - 1, cur[2]))
        continue

    if mirror_map[cur[1]][cur[0]] == "/":
        if cur[2] == 1:
            if bound_x(cur[1] - 1) != cur[1]:
                to_search.append((cur[0], cur[1] - 1, 4))
        elif cur[2] == 3:
            if bound_x(cur[1] + 1) != cur[1]:
                to_search.append((cur[0], cur[1] + 1, 2))
        elif cur[2] == 2:
            if bound_x(cur[0] - 1) != cur[0]:
                to_search.append((cur[0] - 1, cur[1], 3))
        elif cur[2] == 4:
            if bound_x(cur[0] + 1) != cur[0]:
                to_search.append((cur[0] + 1, cur[1], 1))
        continue

    if mirror_map[cur[1]][cur[0]] == "\\":
        if cur[2] == 1:
            if bound_x(cur[1] + 1) != cur[1]:
                to_search.append((cur[0], cur[1] + 1, 2))
        elif cur[2] == 3:
            if bound_x(cur[1] - 1) != cur[1]:
                to_search.append((cur[0], cur[1] - 1, 4))
        elif cur[2] == 2:
            if bound_x(cur[0] + 1) != cur[0]:
                to_search.append((cur[0] + 1, cur[1], 1))
        elif cur[2] == 4:
            if bound_x(cur[0] - 1) != cur[0]:
                to_search.append((cur[0] - 1, cur[1], 3))
        continue

    if mirror_map[cur[1]][cur[0]] == "|":
        if cur[2] == 1 or cur[2] == 3:
            if bound_x(cur[1] - 1) != cur[1]:
                to_search.append((cur[0], cur[1] - 1, 4))
            if bound_x(cur[1] + 1) != cur[1]:
                to_search.append((cur[0], cur[1] + 1, 2))
        elif cur[2] == 2:
            if bound_x(cur[1] + 1) != cur[1]:
                to_search.append((cur[0], cur[1] + 1, cur[2]))
        elif cur[2] == 4:
            if bound_x(cur[1] - 1) != cur[1]:
                to_search.append((cur[0], cur[1] - 1, cur[2]))
        continue

    if mirror_map[cur[1]][cur[0]] == "-":
        if cur[2] == 1:
            if bound_x(cur[0] + 1) != cur[0]:
                to_search.append((cur[0] + 1, cur[1], cur[2]))
        elif cur[2] == 3:
            if bound_x(cur[0] - 1) != cur[0]:
                to_search.append((cur[0] - 1, cur[1], cur[2]))
        elif cur[2] == 2 or cur[2] == 4:
            if bound_x(cur[0] + 1) != cur[0]:
                to_search.append((cur[0] + 1, cur[1], 1))
            if bound_x(cur[0] - 1) != cur[0]:
                to_search.append((cur[0] - 1, cur[1], 3))
        continue

# dir_map = {
#     1: ">",
#     2: "v",
#     3: "<",
#     4: "^",
# }
# output_map = [["." for _ in range(len(mirror_map[0]))] for _ in range(len(mirror_map))]
# for item in path:
#     output_map[item[1]][item[0]] = "#"

# for line in output_map:
#     print("".join(line))

print(len(set((i[0], i[1]) for i in passed)))
