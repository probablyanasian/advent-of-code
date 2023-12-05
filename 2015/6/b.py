import re
lights = [[0 for _ in range(1000)] for _ in range(1000)]

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		stripped = line.rstrip()
		x1, y1, x2, y2 = map(int, re.findall(r'[^0-9]([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', stripped)[0])
		if stripped.startswith('turn on'):
			for y in range(y1, y2+1):
				for x in range(x1, x2+1):
					lights[y][x] += 1
		elif stripped.startswith('turn off'):
			for y in range(y1, y2+1):
				for x in range(x1, x2+1):
					lights[y][x] = max(0, lights[y][x]-1)
		elif stripped.startswith('toggle'):
			for y in range(y1, y2+1):
				for x in range(x1, x2+1):
					lights[y][x] += 2

tot = 0
for y in range(1000):
	tot += sum(lights[y])

print(tot)