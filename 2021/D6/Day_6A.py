state = []
with open('D6_input.txt', 'r') as fopen:
	state = list(map(int, fopen.readline().rstrip().split(',')))

for i in range(256):
	for ind, fish_state in enumerate(state):
		if fish_state == 0:
			state[ind] = 6
			state.append(9)
		else:
			state[ind] -= 1
	
print(len(state))
