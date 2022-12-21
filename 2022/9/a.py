head = [0, 0]
tail = [0, 0]

tail_loc = set()

def calc_tail(head, tail):
	diff_x = head[0] - tail[0]
	diff_y = head[1] - tail[1]

	if diff_x == 0: # same vertical plane
		if diff_y >= 2: # two above (should never need gt)
			tail[1] += 1 # move up
		elif diff_y <= -2: # same deal
			tail[1] -= 1
		return tail # done UD same plane

	if diff_y == 0: # same horizontal plane
		if diff_x >= 2: # two right (should never need gt)
			tail[0] += 1 # move right
		elif diff_x <= -2: # same deal
			tail[0] -= 1
		return tail # done LR same plane

	if diff_x >= 2:
		if diff_y >= 1: # above diag
			tail[0] += 1 # move UR diag
			tail[1] += 1
		if diff_y <= -1:
			tail[0] += 1 # move DR diag
			tail[1] -= 1
		return tail # done

	elif diff_x <= -2:
		if diff_y >= 1: # above diag
			tail[0] -= 1 # move UL diag
			tail[1] += 1
		if diff_y <= -1:
			tail[0] -= 1 # move DL diag
			tail[1] -= 1
		return tail

	if diff_y >= 2:
		if diff_x >= 1: # above diag
			tail[0] += 1 # move UR diag
			tail[1] += 1
		if diff_x <= -1:
			tail[0] -= 1 # move UL diag
			tail[1] += 1
		return tail # done

	elif diff_y <= -2:
		if diff_x >= 1: # above diag
			tail[0] += 1 # move DR diag
			tail[1] -= 1
		if diff_x <= -1:
			tail[0] -= 1 # move DL diag
			tail[1] -= 1
		return tail
	
	return tail

with open("tinput", "r") as file:
	for line in iter(file.readline, ''):
		direction, count = line.rstrip().split()
		count = int(count)
		if direction == "U":
			for _ in range(count):
				head[1] += 1
				tail = calc_tail(head, tail)
				tail_loc.add(tuple(tail))
		if direction == "D":
			for _ in range(count):
				head[1] -= 1
				tail = calc_tail(head, tail)
				tail_loc.add(tuple(tail))
		if direction == "L":
			for _ in range(count):
				head[0] -= 1
				tail = calc_tail(head, tail)
				tail_loc.add(tuple(tail))
		if direction == "R":
			for _ in range(count):
				head[0] += 1
				tail = calc_tail(head, tail)
				tail_loc.add(tuple(tail))

print(len(tail_loc))