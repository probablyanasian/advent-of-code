tot = 0
with open('D3_input.txt', 'r') as fopen:
	ctr = []
	for line in fopen:
		tot += 1
		line_val = line.rstrip()
		for ind, bin in enumerate(line_val):
			if len(ctr) <= ind:
				ctr.append(0)
			if bin == '1':
				ctr[ind] += 1

gamma = ''
epsilon = ''
for val in ctr:
	if val > tot/2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(gamma, int(gamma, 2))
print(epsilon, int(epsilon, 2))
print(int(gamma, 2)*int(epsilon, 2))
