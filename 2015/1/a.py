floor = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		for char in line.rstrip():
			if char == '(':
				floor += 1
			else:
				 floor -=1

print(floor)