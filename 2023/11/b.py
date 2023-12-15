galax_map = []
galaxies = []
has_galax_col = {}
has_galax_row = {}
with open("input", "r") as inf:
    row = 0
    for line in inf:
        galax_map.append(list(line.rstrip()))
        for idx, val in filter(lambda x: x[1] == "#", enumerate(line.rstrip())):
            galaxies.append([idx, row])
            has_galax_col[idx] = True
            has_galax_row[row] = True
        row += 1
r_c = 0
c_c = 0
exp_value = 1_000_000-1
for idx in range(len(galax_map[0])):
    if idx not in has_galax_row:
        for gidx, galax in enumerate(galaxies):
            if galax[1] > r_c+idx:
                galaxies[gidx][1] += exp_value
        r_c += exp_value
    if idx not in has_galax_col:
        for gidx, galax in enumerate(galaxies):
            if galax[0] > c_c+idx:
                galaxies[gidx][0] += exp_value
        c_c += exp_value


def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

total = 0
for idx, galax in enumerate(galaxies):
    for oidx in range(idx+1, len(galaxies)):
        total += manhattan(galax, galaxies[oidx])

print(total)