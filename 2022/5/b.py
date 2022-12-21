from collections import deque
stacks = [deque() for _ in range(10)] # ease of counting
[stacks[1].append(i) for i in "RNFVLJSM"]
[stacks[2].append(i) for i in "PNDZFJWH"]
[stacks[3].append(i) for i in "WRCDG"]
[stacks[4].append(i) for i in "NBS"]
[stacks[5].append(i) for i in "MZWPCBFN"]
[stacks[6].append(i) for i in "PRMW"]
[stacks[7].append(i) for i in "RTNGLSW"]
[stacks[8].append(i) for i in "QTHFNBV"]
[stacks[9].append(i) for i in "LMHZNF"]

with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		a, b, c = map(int, line.split(" "))
		tempstack = deque()
		for _ in range(a):
			tempstack.append(stacks[b].pop())
		for _ in range(a):
			stacks[c].append(tempstack.pop())

for i in range(1,10):
	print(f'{stacks[i].pop()}', end="")