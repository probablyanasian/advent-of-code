from collections import deque
import itertools

dir_map = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}

cur_x, cur_y = 0, 0 # x, y: use top left origin
map_pts = [(0, 0)]
tot_dist = 0
with open("input", "r") as inf:
    for line in inf:
        dir, dist, color = line.rstrip().split(" ")
        dir = dir_map[color[-2]]
        dist = int(color[2:7], base=16)
        if dir == "U":
            cur_y -= dist
        elif dir == "D":
            cur_y += dist
        elif dir == "L":
            cur_x -= dist
        elif dir == "R":
            cur_x += dist
        tot_dist += dist
        map_pts.append((cur_x, cur_y))

area = 0
for idx in range(len(map_pts)-1):
    area += map_pts[idx][0]*map_pts[idx+1][1]-map_pts[idx+1][0]*map_pts[idx][1]
print((area+tot_dist)//2+1)
