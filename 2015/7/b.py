from collections import deque
ins = deque()
registers = {}

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		ins.append(line)

check = lambda x: int(x) if x.isdigit() else registers[x] if x in registers else None

while len(ins) >= 1:
	line = ins.popleft()
	split = line.split(' ')
	if split[1] == '->' and (val := check(split[0])) is not None:
		registers[split[2]] = val & 0xFFFF
	elif split[0] == 'NOT' and (val := check(split[1])) is not None:
		registers[split[3]] = (0xFFFF ^ val) & 0xFFFF # same effect for a 16 bit integer
	else:
		val1 = check(split[0])
		val2 = check(split[2])
		if val1 is not None and val2 is not None:
			if split[1] == 'AND':
				registers[split[4]] = (val1 & val2) & 0xFFFF
			elif split[1] == 'OR':
				registers[split[4]] = (val1 | val2) & 0xFFFF
			elif split[1] == 'LSHIFT':
				registers[split[4]] = (val1 << val2) & 0xFFFF
			elif split[1] == 'RSHIFT':
				registers[split[4]] = (val1 >> val2) & 0xFFFF
		else:
			ins.append(line)

print(registers['a'])