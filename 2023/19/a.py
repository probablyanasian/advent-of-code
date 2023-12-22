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
            continue
        if wf_sect:
            idx = line.index("{")
            workflows[line[:idx]] = line.rstrip()[idx+1:-1].split(",")
        else:
            item = {}
            vals = re.findall(r"=(\d*)", line)
            item["x"] = int(vals[0])
            item["m"] = int(vals[1])
            item["a"] = int(vals[2])
            item["s"] = int(vals[3])
            parts.append(item)

print(workflows)

total = 0
for part in parts:
    workflow = workflows["in"].copy()
    while True:
        if workflow[0] == "A":
            total += sum(part.values())
            break
        elif workflow[0] == "R":
            break
        elif ":" not in workflow[0]:
            workflow = workflows[workflow[0]].copy()
            continue
        
        rcv, l = workflow[0].split(":")
        r, c, v = rcv[0], rcv[1], int(rcv[2:])
        if c == ">":
            if part[r] > v:
                workflow = workflows[l].copy()
            else:
                workflow.pop(0)
        if c == "<":
            if part[r] < v:
                workflow = workflows[l].copy()
            else:
                workflow.pop(0)

print(total)