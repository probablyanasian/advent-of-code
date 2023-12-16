platform = []
with open("input", "r") as inf:
    for line in inf:
        platform.append(line.rstrip())

total_value = 0
for idx in range(len(platform[0])):
    hold = 0
    for row, val in enumerate(platform):
        if val[idx] == "O":
            total_value += len(platform)-hold
            hold += 1
        elif val[idx] == "#":
            hold = row+1

print(total_value)