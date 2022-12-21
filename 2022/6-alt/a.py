with open("input", "r") as file:
	line = file.readline().rstrip()
	for i in range(len(line)-4):
		if len(set(list(line[i:i+4]))) == 4:
			print(i+4)
			break