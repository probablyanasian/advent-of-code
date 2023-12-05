visited = set()
x, y = 0, 0
rx, ry = 0, 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		visited.add((x, y)) # only need one
		alt = False
		for char in line.rstrip():
			if alt:
				if char == '>':
					rx += 1
				elif char == '<':
					rx -= 1
				elif char == 'v':
					ry += 1
				elif char == '^':
					ry -= 1
				visited.add((rx, ry))
			else:
				if char == '>':
					x += 1
				elif char == '<':
					x -= 1
				elif char == 'v':
					y += 1
				elif char == '^':
					y -= 1
				visited.add((x, y))
			alt = not alt
print(len(visited))