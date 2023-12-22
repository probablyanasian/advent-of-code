import re
import itertools
from collections import deque

workflows = {"A": ["A"], "R": ["R"]}
parts = []

with open("input", "r") as inf:
    wf_sect = True
    for line in inf:
        if line == "\n":
            wf_sect = False
            break
        if wf_sect:
            idx = line.index("{")
            workflows[line[:idx]] = line.rstrip()[idx+1:-1].split(",")

parts = deque([{"wf_left": ["in"], "x_min": 1, "x_max": 4000, "m_min": 1, "m_max": 4000, "a_min": 1, "a_max": 4000, "s_min": 1, "s_max": 4000}])

total = 0
while parts:
    cur = parts.pop()
    workflow = cur["wf_left"]
    while True:
        if workflow[0] == "A":
            total += (cur["x_max"]-cur["x_min"]+1)*(cur["m_max"]-cur["m_min"]+1)*(cur["a_max"]-cur["a_min"]+1)*(cur["s_max"]-cur["s_min"]+1)
            break
        elif workflow[0] == "R":
            break
        elif ":" not in workflow[0]:
            workflow = workflows[workflow[0]].copy()
            continue
        
        rcv, l = workflow[0].split(":")
        r, c, v = rcv[0], rcv[1], int(rcv[2:])
        if c == ">":
            if cur[r+"_min"] > v:
                workflow = workflows[l].copy()
            elif cur[r+"_max"] > v:
                cpy = cur.copy()
                cpy["wf_left"] = workflow.copy() # deepcopy
                cpy[r+"_max"] = v
                parts.append(cpy)

                cur[r+"_min"] = v+1
                workflow = workflows[l].copy()
            else:
                workflow.pop(0)
        if c == "<":
            if cur[r+"_max"] < v:
                workflow = workflows[l].copy()
            elif cur[r+"_min"] < v:
                cpy = cur.copy()
                cpy["wf_left"] = workflow.copy() # deepcopy
                cpy[r+"_min"] = v
                parts.append(cpy)

                cur[r+"_max"] = v-1
                workflow = workflows[l].copy()
            else:
                workflow.pop(0)

print(total)