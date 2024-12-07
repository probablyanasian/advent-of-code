import itertools
from collections import deque
import sys
sys.setrecursionlimit(9999999)

hailstones = []
with open("input", "r") as inf:
    for line in inf:
        loc, velo = line.rstrip().split(" @ ")
        x, y, z = loc.split(", ")
        v_x, v_y, v_z = velo.split(", ")
        hailstones.append((int(x), int(y), int(z), int(v_x), int(v_y), int(v_z)))

def between(x, low=200000000000000, high=400000000000000):
    return x < high and x > low

def collide(a, b):
    x_1, y_1, _, v_x1, v_y1, _ = a
    x_2, y_2, _, v_x2, v_y2, _ = b
    # misread the problem for way too long
    # if v_x1 - v_x2 == 0 or v_y1 - v_y2 == 0:
    #     return False
    # t_x = (x_2-x_1)/(v_x1-v_x2)
    # t_y = (y_2-y_1)/(v_y1-v_y2)
    # print(t_x, t_y)

    if v_x1*v_y2-v_y1*v_x2 == 0:
        return False
    t_1 = (v_y2*(x_2-x_1) - v_x2*(y_2-y_1)) / (v_x1*v_y2 - v_x2*v_y1)
    t_2 = (v_y1*(x_2-x_1) - v_x1*(y_2-y_1)) / (v_x1*v_y2 - v_x2*v_y1)
    return (t_1 > 0 and t_2 > 0 and between(x_1+v_x1*t_1)) and between(y_1+v_y1*t_1)

collisions = 0
for ida, icea in enumerate(hailstones[:-1]):
    for iceb in hailstones[ida+1:]:
        if collide(icea, iceb):
            collisions += 1

print(collisions)