from collections import deque

a = deque()
with open("input", "r") as file:
	line = file.readline().rstrip()
	[a.append(char) for char in line[:3]]
	for ind, char in enumerate(line[3:]):
		a.append(char)
		if len(set(a)) == 4:
			print(ind + 4)
			break
		a.popleft()