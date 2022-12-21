state = [0 for _ in range(9)]
with open('D6_input.txt', 'r') as fopen:
	fishes = list(map(int, fopen.readline().rstrip().split(',')))
	for fish in fishes:
		state[fish] += 1

for i in range(256):
	new_state = [0 for _ in range(9)]
	for ind in range(len(state)-1, -1, -1):
		if ind == 0:
			new_state[8] += state[ind]
			new_state[6] += state[ind]
		else:
			new_state[ind-1] += state[ind]
	state = new_state

print(sum(state))
