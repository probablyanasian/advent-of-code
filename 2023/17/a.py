from collections import deque
import heapq
    
heatloss_map: list[list[int]]
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
in_bound_x = lambda x: x == bound_x(x)
in_bound_y = lambda y: y == bound_y(y)

    
# def do_step(step: Path, dir: int) -> Path:
#     new_walk = step.walk.copy()
#     new_walk.append((step.x, step.y))
#     if dir == 0:
#         return Path(step.x, step.y-1, step.loss+heatloss_map[step.y-1][step.x], 0, step.lm_dir_count + 1 if step.lm_dir == 0 else 1, new_walk)
#     if dir == 1:
#         return Path(step.x+1, step.y, step.loss+heatloss_map[step.y][step.x+1], 1, step.lm_dir_count + 1 if step.lm_dir == 1 else 1, new_walk)
#     if dir == 2:
#         return Path(step.x, step.y+1, step.loss+heatloss_map[step.y+1][step.x], 2, step.lm_dir_count + 1 if step.lm_dir == 2 else 1, new_walk)
#     if dir == 3:
#         return Path(step.x-1, step.y, step.loss+heatloss_map[step.y][step.x-1], 3, step.lm_dir_count + 1 if step.lm_dir == 3 else 1, new_walk)

# push (loss, x, y, dir)
# 0 ^, 1 >, 2 v, 3 <
seen = set()
heads = []
heapq.heappush(heads, (0, 0, 0, 0))
heapq.heappush(heads, (0, 0, 0, 3))
while heads:
    loss, x, y, dir = heapq.heappop(heads)
    if x == len(heatloss_map[0])-1 and y == len(heatloss_map)-1:
        print(loss)
        break
    if (x, y, dir) in seen:
        continue
    seen.add((x, y, dir))
    for n_dir in [(dir+1)%4, (dir-1)%4]: # turn right, left
        n_loss = loss
        for dist in range(1, 4):
            if n_dir == 0 and in_bound_y(y-dist):
                n_loss += heatloss_map[y-dist][x]
                heapq.heappush(heads, (n_loss, x, y-dist, 0))
            elif n_dir == 1 and in_bound_x(x+dist):
                n_loss += heatloss_map[y][x+dist]
                heapq.heappush(heads, (n_loss, x+dist, y, 1))
            elif n_dir == 2 and in_bound_y(y+dist):
                n_loss += heatloss_map[y+dist][x]
                heapq.heappush(heads, (n_loss, x, y+dist, 2))
            elif n_dir == 3 and in_bound_x(x-dist):
                n_loss += heatloss_map[y][x-dist]
                heapq.heappush(heads, (n_loss, x-dist, y, 3))
            else:
                break

