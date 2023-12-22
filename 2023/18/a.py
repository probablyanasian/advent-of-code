from collections import deque
import itertools

cur_x, cur_y = 0, 0 # x, y: use top left origin
map_pts = [(cur_x, cur_y)]
with open("input", "r") as inf:
    for line in inf:
        dir, dist, color = line.rstrip().split(" ")
        if dir == "U":
            for d in range(1, int(dist)+1):
                map_pts.append((cur_x, cur_y-d))
            cur_y -= d
        elif dir == "D":
            for d in range(1, int(dist)+1):
                map_pts.append((cur_x, cur_y+d))
            cur_y += d
        elif dir == "L":
            for d in range(1, int(dist)+1):
                map_pts.append((cur_x-d, cur_y))
            cur_x -= d
        elif dir == "R":
            for d in range(1, int(dist)+1):
                map_pts.append((cur_x+d, cur_y))
            cur_x += d
    
xs, ys = zip(*map_pts)
min_xs = min(xs)
min_ys = min(ys)
x_range = max(xs) - min_xs + 3 # add borders
y_range = max(ys) - min_ys + 3 # add borders
map_pts = [(x - min_xs, y - min_ys) for x, y in map_pts]
pit_map = [["." for _ in range(x_range)] for _ in range(y_range)]
for x, y in map_pts:
    pit_map[y+1][x+1] = "#"

bound_x = lambda x: 0 if x < 0 else len(pit_map[0])-1 if x > len(pit_map[0])-1 else x 
bound_y = lambda y: 0 if y < 0 else len(pit_map)-1 if y > len(pit_map)-1 else y
in_bound_x = lambda x: x == bound_x(x)
in_bound_y = lambda y: y == bound_y(y)

movement = list(itertools.product((-1, 0, 1), repeat=2))
movement.remove((0, 0))

to_search = deque(((0, 0),))
seen = set()
while to_search:
    cur = to_search.popleft()
    if cur in seen:
        continue
    seen.add(cur)
    for move in movement:
        n_x, n_y = cur[0]+move[0], cur[1]+move[1]
        if in_bound_x(n_x) and in_bound_y(n_y):
            if pit_map[n_y][n_x] != "#":
                to_search.append((n_x, n_y))
                pit_map[n_y][n_x] = "%"

# for line in pit_map:
#     print("".join(line))


# print(seen)
print(x_range*y_range - len(seen))