sum = 0
i = 0
arr = [set(), set(), set()]
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		arr[i] = set(line)
		i += 1
		if (i == 3):
			i = 0
			commonA = arr[0].intersection(arr[1])
			common = commonA.intersection(arr[2])
			for val in common:
				if (char := ord(val)) >= 97:
					sum += char - 96
				else:
					sum += char - 38

print(sum)