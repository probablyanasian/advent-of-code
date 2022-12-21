reg = 1
clock = 1
interesting = [20, 60, 100, 140, 180, 220]
int_val = []
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		cmd = line.rstrip().split()
		if cmd[0] == 'noop':
			if clock in interesting:
				int_val.append(reg)
			clock += 1
		if cmd[0] == 'addx':
			if clock in interesting or (clock+1) in interesting:
				int_val.append(reg)
			clock += 2
			reg += int(cmd[1])

print(int_val)
for i in range(len(interesting)):
	int_val[i] *= interesting[i]
print(int_val)
print(sum(int_val))