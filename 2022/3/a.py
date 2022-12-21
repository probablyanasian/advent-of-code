sum = 0
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		l = len(line)
		a = set(line[:l//2])
		b = set(line[l//2:])
		common = a.intersection(b)
		for val in common:
			if (char := ord(val)) >= 97:
				sum += char - 96
			else:
				sum += char - 38

print(sum)