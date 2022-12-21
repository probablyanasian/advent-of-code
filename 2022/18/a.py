blocks = set()

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		blocks.add(tuple(map(int, line.rstrip().split(','))))

covered = 0
for block in blocks:
	for dir in [1, -1]:
		if (block[0] + dir, block[1], block[2]) in blocks:
			covered += 1
		if (block[0], block[1] + dir, block[2]) in blocks:
			covered += 1
		if (block[0], block[1], block[2] + dir) in blocks:
			covered += 1

print(covered)
sa = 6*len(blocks) - covered
print(sa)