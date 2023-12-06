from functools import cache

@cache
def win_card(card_num: int) -> int:
	win, have = cards[card_num].split("|")
	win = set(map(int, win.split()))
	have = set(map(int, have.split()))
	wins = len(win.intersection(have))
	return 1 + sum(map(win_card, [card_num + i for i in range(1, wins+1)]))

cards = []

tot = 0
with open("input", "r") as inf:
	for line in inf:
		card, line = line.split(":")
		cards.append(line)

print(sum(map(win_card, [i for i in range(len(cards))])))