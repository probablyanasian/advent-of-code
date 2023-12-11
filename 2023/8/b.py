ins = ""
mapping = {}
with open("input", "r") as inf:
    ins = inf.readline().rstrip()
    inf.readline()
    for line in inf:
        k, v = line.split(" = ")
        mapping[k] = tuple(v[1:-2].split(", "))

conv = {
    "L": 0,
    "R": 1,
}

cur_locs = [x for x in mapping if x[-1] == "A"]
cycs = []
for idx, val in enumerate(cur_locs):
    cur_ins = 0
    cnt = 0
    while cur_locs[idx][-1] != "Z":
        cur_locs[idx] = mapping[cur_locs[idx]][conv[ins[cur_ins]]]
        cnt += 1
        cur_ins += 1
        if cur_ins >= len(ins):
            cur_ins = 0
    cycs.append(cnt)

import math
print(math.lcm(*cycs))