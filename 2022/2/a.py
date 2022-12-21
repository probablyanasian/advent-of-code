score = 0
conv = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		a, b = line.split(" ")
		a = conv[a]
		b = conv[b]
		if (b-a == 0):
			score += b+1 + 3 # chosen + draw
		elif ((b-a)%3 == 1):
			score += b+1 + 6
		else:
			score += b+1

print(score)