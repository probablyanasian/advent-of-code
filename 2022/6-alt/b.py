with open("input", "r") as file:
	line = file.readline().rstrip()
	for i in range(len(line)-14):
		if len(set(list(line[i:i+14]))) == 14:
			print(i+14)
			break