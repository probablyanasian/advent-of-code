import re

res = 0
with open("input") as inf:
    count = 0
    for line in inf:
        skip = False
        count += 1
        tot = [0, 0, 0]
        for subgame in line.split(";"):
            if (match := re.search(r'(\d+) red', subgame)):
                tot[0] = max(tot[0], int(match.group(1)))
            if (match := re.search(r'(\d+) green', subgame)):
                tot[1] = max(tot[1], int(match.group(1)))
            if (match := re.search(r'(\d+) blue', subgame)):
                tot[2] = max(tot[2], int(match.group(1)))
        res += tot[0]*tot[1]*tot[2]

print(res)