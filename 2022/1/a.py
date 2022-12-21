max = 0
count = 0
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		if line != "":
			count += int(line)
		else:
			if count > max:
				max = count
			count = 0

print(max)