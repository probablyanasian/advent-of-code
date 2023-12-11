val = {
	"A": 13,
	"K": 12,
	"Q": 11,
	"J": 1,
	"T": 10,
}

def char_to_score(x: str) -> int:
	if x.isdigit():
		return int(x)
	return val[x]

def str_to_score(x: str) -> int:
	t = 0
	for c in x:
		t *= 14
		t += char_to_score(c)
	return t

def sublen(x: str) -> int:
	p = ""
	t = 0
	m = [0]
	for c in x.replace("J", ""):
		if c == p:
			t += 1
			p = c
		else:
			m.append(t)
			t = 1
			p = c
		# print(c, t, m)
	m.append(t)
	m.sort()
	m[-1] += x.count('J')
	if m[-1] == 5:
		return 7
	elif m[-1] == 4:
		return 6
	elif m[-1] == 3:
		if m[-2] == 2:
			return 5
		return 4
	elif m[-1] == 2:
		if m[-2] == 2:
			return 3
		return 2
	return 1
			

hands = []
with open("input", "r") as inf:
	for line in inf:
		hands.append((line.split()))

hands = sorted(hands, key=lambda x: str_to_score(x[0]))
hands = sorted(hands, key=lambda x: sublen("".join(sorted(x[0]))))
print(sum(map(lambda x: int(x[1][1])*(x[0]+1), enumerate(hands))))