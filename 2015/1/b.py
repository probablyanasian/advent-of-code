floor = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		for ind, char in enumerate(line.rstrip()):
			if char == '(':
				floor += 1
			else:
				floor -=1
			if floor == -1:
				print(ind+1)
				break
print(floor)