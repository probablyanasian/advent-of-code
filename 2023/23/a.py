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

longest = 0
def dfs(cur, path, seen):
    global longest
    if cur == (len(forest_map[0])-2, len(forest_map)-1):
        longest = max(len(path), longest)
    if forest_map[cur[1]][cur[0]] == ".":
        possible_moves = [move for move in movement if in_bound_x(cur[0]+move[0]) and in_bound_y(cur[1]+move[1]) and forest_map[cur[1]+move[1]][cur[0]+move[0]] != "#"]
    else:
        possible_moves = [{">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[forest_map[cur[1]][cur[0]]]]
    for move in possible_moves:
        n_x, n_y = cur[0]+move[0], cur[1]+move[1]
        if (n_x, n_y) not in seen:
            path.append((n_x, n_y))
            seen.add((n_x, n_y))
            dfs((n_x, n_y), path, seen)
            # prevent need to deepcopy
            seen.remove((n_x, n_y))
            path.pop()

dfs((1, 0), [], set((1, 0)))
print(longest)