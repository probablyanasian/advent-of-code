gameorder = []
gamecards = []
with open('D4_input.txt', 'r') as fopen:
    gameorder = fopen.readline().rstrip().split(',')
    fopen.readline() # discard
    ctr = 0
    card = []
    for line in fopen:
        card.append(line.rstrip().split())
        ctr += 1
        if ctr % 6 == 0:
            card.pop(5)
            gamecards.append(card)
            ctr = 0
            card = []

def verify_win(card):
    for i in range(len(card)):
        if len(set(card[i])) == 1 and 'X' in set(card[i]):
            return True
    for col in range(len(card[0])):
        check = []
        for row in range(len(card)):
            check.append(card[row][col])
        if len(set(check)) == 1 and 'X' in set(check):
            return True
    return False

def mark_card(card, value):
    for row in range(len(card)):
        for col in range(len(card[0])):
            if card[row][col] == value:
                card[row][col] = 'X'
    return card

val = False
lose = []
for number in gameorder:
    poplist = []
    for ind, card in enumerate(gamecards):
        gamecards[ind] = mark_card(card, number)
        if verify_win(card):
            poplist.append(ind)
        if len(gamecards) == 1 and len(poplist) == 1:
            lose = gamecards[0]
            print(gamecards)
            val = True
            break
    if val: break
    for ind in reversed(poplist):
        gamecards.pop(ind)

def sum_card(card):
    sum = 0
    for row in range(len(card)):
        for col in range(len(card[0])):
            if card[row][col] != 'X':
                sum += int(card[row][col])
    return sum

print(number, int(number)*sum_card(lose))
