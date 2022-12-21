trees = []

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		trees.append(list(map(int, list(line))))

total = len(trees) * len(trees[1])
print(total)
sum = 0
for y in range(1, len(trees)-1):
	for x in range(1, len(trees[0])-1):
		y_up_visible = True
		y_down_visible = True
		x_up_visible = True
		x_down_visible = True
		height = trees[y][x]
		# print(f'{list(range(y))=}')
		# print(list(range(y+1, len(trees))))
		# print(list(range(x)))
		# print(list(range(x+1, len(trees[0]))))

		for y_up in range(y):
			if trees[y_up][x] >= height:
				y_up_visible = False
				break
		for y_down in range(y+1, len(trees)):
			if trees[y_down][x] >= height:
				y_down_visible = False
				break
		for x_up in range(x):
			if trees[y][x_up] >= height:
				x_up_visible = False
				break
		for x_down in range(x+1, len(trees[0])):
			if trees[y][x_down] >= height:
				x_down_visible = False
				break
		if not(y_up_visible or y_down_visible or x_up_visible or x_down_visible):
			sum += 1

print(total - sum)