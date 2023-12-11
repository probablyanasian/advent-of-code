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

cur_loc = "AAA"
cur_ins = 0
cnt = 0
while cur_loc != "ZZZ":
    cur_loc = mapping[cur_loc][conv[ins[cur_ins]]]
    cnt += 1
    cur_ins += 1
    if cur_ins >= len(ins):
        cur_ins = 0
print(cnt)