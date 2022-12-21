sum = 0
with open("input", "r") as file:
	for line in file:
		line = line.rstrip()
		a, b = line.split(',')
		a_1, a_2 = map(int, a.split('-'))
		b_1, b_2 = map(int, b.split('-'))
		if a_1 < b_1 and a_2 < b_1:
			continue
		elif a_1 > b_2 and a_2 > b_2:
			continue
		sum += 1

print(sum)