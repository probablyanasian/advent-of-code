import re

tot = (12, 13, 14)
res = 0
with open("input") as inf:
    count = 0
    for line in inf:
        skip = False
        count += 1
        for subgame in line.split(";"):
            if (match := re.search(r'(\d+) red', subgame)):
                if int(match.group(1)) > tot[0]:
                    skip = True
                    break
            if (match := re.search(r'(\d+) green', subgame)):
                if int(match.group(1)) > tot[1]:
                    skip = True
                    break
            if (match := re.search(r'(\d+) blue', subgame)):
                if int(match.group(1)) > tot[2]:
                    skip = True
                    break
        if not skip:
            res += count

print(res)