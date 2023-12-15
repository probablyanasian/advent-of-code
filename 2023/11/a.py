galax_map = []
has_galax_col = {}
has_galax_row = {}
with open("input", "r") as inf:
    row = 0
    for line in inf:
        galax_map.append(list(line.rstrip()))
        for idx, val in filter(lambda x: x[1] == "#", enumerate(line.rstrip())):
            has_galax_col[idx] = True
            has_galax_row[row] = True
        row += 1

# expand cols and rows
for idx in range(len(galax_map[0])-1, -1, -1):
    if idx not in has_galax_col:
        line: list[str]
        for line in galax_map:
            line.insert(idx, ".")

fill_row = ["." for _ in range(len(galax_map[0]))]
for idx in range(len(galax_map[0])-1, -1, -1):
    if idx not in has_galax_row:
        galax_map.insert(idx, fill_row)

galaxies = [(row, col) for row, line in enumerate(galax_map) for col, sym in enumerate(line) if sym == "#"]

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

total = 0
for idx, galax in enumerate(galaxies):
    for oidx in range(idx+1, len(galaxies)):
        total += manhattan(galax, galaxies[oidx])

print(total)