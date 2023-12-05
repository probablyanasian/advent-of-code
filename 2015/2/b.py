tot = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		l, w, h = map(int, line.rstrip().split('x'))
		tot += 2*sum(sorted([l, w, h])[:2]) + l*w*h
print(tot)