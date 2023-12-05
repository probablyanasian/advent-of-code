tot = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		l, w, h = map(int, line.rstrip().split('x'))
		tot += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(tot)