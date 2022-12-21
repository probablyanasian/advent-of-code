with open('D2_input.txt', 'r') as fopen:
	h = 0
	d = 0
	for line in fopen:
		cmd, val = line.rstrip().split()
		val = int(val)

		if cmd == 'forward':
			h += val
		if cmd == 'down':
			d += val
		if cmd == 'up':
			d -= val
print(h, d)
print(h*d)
