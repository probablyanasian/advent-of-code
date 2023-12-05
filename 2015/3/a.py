visited = set()
x, y = 0, 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		visited.add((x, y))
		for char in line.rstrip():
			if char == '>':
				x += 1
			elif char == '<':
				x -= 1
			elif char == 'v':
				y += 1
			elif char == '^':
				y -= 1
			visited.add((x, y))
print(len(visited))