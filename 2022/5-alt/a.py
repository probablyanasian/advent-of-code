from collections import deque
stacks = []

with open("input", "r") as file:
	is_initialized = False
	for line in file:
		blocks = [line[s:s+4] for s in range(0, len(line), 4)]
		if not is_initialized:
			stacks = [deque() for _ in range(len(blocks)+1)] # +1 for ease of counting
			is_initialized = True
		for ind, val in enumerate(blocks):
			if val[1] == '1':
				break # done, exit
			if val[1] != ' ':
				stacks[ind+1].appendleft(val[1]) # +1 for ease of counting
		if val[1] == '1':
			break # exit

	file.readline() # discard empty line

	for line in file:
		line = line.rstrip()
		_, a, _, b, _, c = line.rstrip().split(" ")
		a, b, c = map(int, [a, b, c])
		for _ in range(a):
			stacks[c].append(stacks[b].pop())

for i in range(1,10):
	print(f'{stacks[i].pop()}', end="")