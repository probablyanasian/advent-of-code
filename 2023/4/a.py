tot = 0
with open("input", "r") as inf:
	for line in inf:
		line = line.split(":")[1]
		win, have = line.split("|")
		win = set(map(int, win.split()))
		have = set(map(int, have.split()))
		wins = len(win.intersection(have))
		tot += (1 if wins else 0)*pow(2, wins-1)
		
print(tot)