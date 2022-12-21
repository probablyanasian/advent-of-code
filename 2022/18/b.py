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

max_x = max(blocks, key=lambda x: x[0])[0]
max_y = max(blocks, key=lambda x: x[1])[1]
max_z = max(blocks, key=lambda x: x[2])[2]

internal = 0
for x in range(max_x+1):
	for y in range(max_y+1):
		for z in range(max_z+1):
			int_cov = 0
			block = (x, y, z)
			for dir in [1, -1]:
				if (block[0] + dir, block[1], block[2]) in blocks:
					int_cov += 1
				if (block[0], block[1] + dir, block[2]) in blocks:
					int_cov += 1
				if (block[0], block[1], block[2] + dir) in blocks:
					int_cov += 1
			if int_cov == 6 and not block in blocks:
				internal += 1

print(covered)
sa = 6*len(blocks) - covered
print(sa)
print(sa - (6*internal))