with open("tinput", "r") as inf:
	time = int("".join(inf.readline().split()[1:]))
	dist = int("".join(inf.readline().split()[1:]))


res = 0
for t in range(time):
	if (t*(time-t)) > dist:
		res += 1
print(res)