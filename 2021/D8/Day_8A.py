ctr = 0
with open('D8_input.txt', 'r') as fopen:
	for line in fopen:
		sig, out = line.rstrip().split('|')
		sig = sig.split()
		out = out.split()
		for val in out:
			if len(val) in [2, 3, 4, 7]:
				ctr += 1

print(ctr)
