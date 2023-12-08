
times = []
dists = []
with open("input", "r") as inf:
	times = [x for x in map(int, inf.readline().split()[1:])]
	dists = [x for x in map(int, inf.readline().split()[1:])]

tot = 1
for idx, time in enumerate(times):
	res = 0
	for t in range(time):
		if (t*(time-t)) > dists[idx]:
			res += 1
	tot *= res
print(tot)