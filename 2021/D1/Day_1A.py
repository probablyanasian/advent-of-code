with open('D1_input.txt', 'r') as fopen:
	tot = 0
	prev = int(fopen.readline().rstrip())
	for line in fopen:
		line = int(line)
		if line >= prev:
			tot += 1
		prev = line

print(tot)
