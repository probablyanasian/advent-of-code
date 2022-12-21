from collections import deque

a = deque()
with open("input", "r") as file:
	line = file.readline().rstrip()
	[a.append(char) for char in line[:13]]
	for ind, char in enumerate(line[13:]):
		a.append(char)
		if len(set(a)) == 14:
			print(ind + 14)
			break
		a.popleft()