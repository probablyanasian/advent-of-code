score = 0
conv = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		a, b = line.split(" ")
		a = conv[a]
		if (b == "Y"):
			score += a+1 + 3 # chosen + draw
		elif (b == "Z"):
			score += (a+1)%3 + 1 + 6 # chosen + win
		else:
			score += (a-1)%3 + 1 # chosen + loss

print(score)