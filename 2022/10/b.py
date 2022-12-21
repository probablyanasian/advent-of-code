from collections import deque

cache = deque() # allows for delay
reg = 1
clock = -1
interesting = [20, 60, 100, 140, 180, 220]
int_val = []
screen = [[] for _ in range(6)]
with open("input", "r") as file:
	# for line in iter(file.readline, ''):
	while clock < 239:
		clock += 1
		if (clock % 40) <= reg+1 and (clock % 40) >= reg-1:
			screen[clock // 40].append('#')
		else:
			screen[clock // 40].append('.')
		if cache: # if cache has stuff
			reg += cache.popleft()
		else:
			cmd = file.readline().rstrip().split()
			# if cmd[0] == 'noop': # don't do anything, let clock tick
			if cmd[0] == 'addx':
				cache.append(int(cmd[1]))

for line in screen:
	print(''.join(line))
