with open('D2_input.txt', 'r') as fopen:
	horiz = 0
	depth = 0
	aim = 0	
	for line in fopen:
		cmd, val = line.rstrip().split()
		val = int(val)

		if cmd == 'forward':
			horiz += val
			depth += aim*val
		if cmd == 'down':
			aim += val
		if cmd == 'up':
			aim -= val
			
print(horiz, depth)
print(horiz*depth)
