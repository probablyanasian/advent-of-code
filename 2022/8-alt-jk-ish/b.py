trees = []

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		trees.append(list(map(int, list(line))))

max = 0
for y in range(1, len(trees)-1):
	for x in range(1, len(trees[0])-1):
		up_view = 0
		down_view = 0
		left_view = 0
		right_view = 0
		height = trees[y][x]

		for y_up in range(y):
			up_view += 1
			if trees[y-y_up-1][x] >= height:
				break
		for y_down in range(y+1, len(trees)):
			down_view += 1
			if trees[y_down][x] >= height:
				break
		for x_up in range(x):
			left_view += 1
			if trees[y][x-x_up-1] >= height:
				break
		for x_down in range(x+1, len(trees[0])):
			right_view += 1
			if trees[y][x_down] >= height:
				break
		# print(f'{up_view} {down_view} {left_view} {right_view} {(up_view*down_view*left_view*right_view)}')
		total_view = (up_view*down_view*left_view*right_view)
		if total_view > max:
			max = total_view

print(max)