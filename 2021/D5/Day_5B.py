grid = [[0 for _ in range(1000)] for _ in range(1000)]
with open('D5_input.txt', 'r') as fopen:
	for line in fopen:
		pt_a, pt_b = line.rstrip().split(' -> ')
		pt_a = list(map(int, pt_a.split(',')))
		pt_b = list(map(int, pt_b.split(',')))

		if pt_a[0] == pt_b[0]:
			if pt_a[1] > pt_b[1]:
				pt_a, pt_b = pt_b, pt_a
			for i in range(pt_a[1], pt_b[1]+1):
				grid[i][pt_a[0]] += 1

		elif pt_a[1] == pt_b[1]:
			if pt_a[0] > pt_b[0]:
				pt_a, pt_b = pt_b, pt_a
			for i in range(pt_a[0], pt_b[0]+1):
				grid[pt_a[1]][i] += 1

		else:
			if pt_a[0] > pt_b[0]:
				pt_a, pt_b = pt_b, pt_a
			if pt_a[1] > pt_b[1]:
				for i in range(pt_a[1]-pt_b[1]+1):
					grid[pt_a[1]-i][pt_a[0]+i] += 1
			else:
				for i in range(pt_b[1]-pt_a[1]+1):
					grid[pt_a[1]+i][pt_a[0]+i] += 1

ctr = 0
for row in grid:
	for item in row:
		if item >= 2:
			ctr += 1

print(ctr)
