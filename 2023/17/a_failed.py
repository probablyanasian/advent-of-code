from collections import deque
from functools import cache

heatloss_map = []
with open("input", "r") as inf:
    for line in inf:
        heatloss_map.append(list(map(int, line.rstrip())))

bound_x = (
    lambda x: 0
    if x < 0
    else len(heatloss_map[0]) - 1
    if x > len(heatloss_map[0]) - 1
    else x
)
bound_y = (
    lambda y: 0 if y < 0 else len(heatloss_map) - 1 if y > len(heatloss_map) - 1 else y
)


class Path():
    def __init__(self, x, y, loss, dir, count, walk):
        self.x = x
        self.y = y
        self.loss = loss
        self.lm_dir = dir
        self.lm_dir_count = count
        self.walk = walk
    
    def __repr__(self):
        return f"{self.x}, {self.y}, {self.loss}"
    
def do_step(step: Path, dir: int) -> Path:
    new_walk = step.walk.copy()
    new_walk.append((step.x, step.y))
    if dir == 0:
        return Path(step.x, step.y-1, step.loss+heatloss_map[step.y-1][step.x], 0, step.lm_dir_count + 1 if step.lm_dir == 0 else 1, new_walk)
    if dir == 1:
        return Path(step.x+1, step.y, step.loss+heatloss_map[step.y][step.x+1], 1, step.lm_dir_count + 1 if step.lm_dir == 1 else 1, new_walk)
    if dir == 2:
        return Path(step.x, step.y+1, step.loss+heatloss_map[step.y+1][step.x], 2, step.lm_dir_count + 1 if step.lm_dir == 2 else 1, new_walk)
    if dir == 3:
        return Path(step.x-1, step.y, step.loss+heatloss_map[step.y][step.x-1], 3, step.lm_dir_count + 1 if step.lm_dir == 3 else 1, new_walk)

# step -> (x, y, dir, num)
# 0 ^, 1 >, 2 v, 3 <
global_seen = dict()
best_so_far = 999999999999999999
@cache
def solve(step: Path) -> int:
    global global_seen
    global best_so_far
    # x = [["." for _ in range(len(heatloss_map[0]))] for _ in range(len(heatloss_map))]
    global_seen[(step.x, step.y, step.lm_dir, step.lm_dir_count)] = step.loss
    if step.loss > best_so_far:
        return best_so_far
    if step.x == len(heatloss_map[0])-1 and step.y == len(heatloss_map)-1:
        print(step.loss)
        return step.loss

    possible_dirs = [1, 2, 0, 3]
    possible_dirs.remove((step.lm_dir+2)%4)
    if step.lm_dir_count == 3:
        possible_dirs.remove(step.lm_dir)
    if 0 in possible_dirs:
        if bound_y(step.y-1) == step.y or (step.x, step.y-1, 0, step.lm_dir_count + 1 if step.lm_dir == 0 else 1) in global_seen and global_seen[(step.x, step.y-1, 0, step.lm_dir_count + 1 if step.lm_dir == 0 else 1)] < step.loss+heatloss_map[step.y-1][step.x]:
            possible_dirs.remove(0)
    if 1 in possible_dirs:
        if bound_x(step.x+1) == step.x or (step.x+1, step.y, 1, step.lm_dir_count + 1 if step.lm_dir == 1 else 1) in global_seen and global_seen[(step.x+1, step.y, 1, step.lm_dir_count + 1 if step.lm_dir == 1 else 1)] < step.loss+heatloss_map[step.y][step.x+1]:
            possible_dirs.remove(1)
    if 2 in possible_dirs:
        if bound_y(step.y+1) == step.y or (step.x, step.y+1, 2, step.lm_dir_count + 1 if step.lm_dir == 2 else 1) in global_seen and global_seen[(step.x, step.y+1, 2, step.lm_dir_count + 1 if step.lm_dir == 2 else 1)] < step.loss+heatloss_map[step.y+1][step.x]:
            possible_dirs.remove(2)
    if 3 in possible_dirs:
        if bound_x(step.x-1) == step.x or (step.x-1, step.y, 3, step.lm_dir_count + 1 if step.lm_dir == 3 else 1) in global_seen and global_seen[(step.x-1, step.y, 3, step.lm_dir_count + 1 if step.lm_dir == 3 else 1)] < step.loss+heatloss_map[step.y][step.x-1]:
            possible_dirs.remove(3)

    if not possible_dirs:
        return 999999999999999999999 # some max value
    
    for dir in possible_dirs:
        best_so_far = min(best_so_far, solve(do_step(step, dir)))
    return best_so_far


right = solve(Path(0, 0, 0, 0, 1, []))
print("done right")
# global_seen = dict()
down = solve(Path(0, 0, 0, 3, 1, []))

print(min(right, down))