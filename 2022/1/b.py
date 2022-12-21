max = 0
count = 0
arr = []
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		if line != "":
			count += int(line)
		else:
			arr.append(count)
			count = 0

print(sum(sorted(arr)[-3:]))
