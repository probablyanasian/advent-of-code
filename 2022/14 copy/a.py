rocks = set()

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		waypoints = list([tuple(map(int, coord.split(','))) for coord in line.rstrip().split(' -> ')])
		prev = waypoints[0]
		for pt in waypoints[1:]:
			for x in range(min(prev[0], pt[0]), max(prev[0], pt[0])+1):
				for y in range(min(prev[1], pt[1]), max(prev[1], pt[1])+1):
					rocks.add(tuple([x, y]))
			prev = pt

filled = rocks.copy()
max_h = max(rocks, key=lambda x: x[1])[1]
sand = 0
while True:
	sand_pt = [500, 0]
	while True:
		if sand_pt[1] > max_h:
			break
		if tuple([sand_pt[0], sand_pt[1]+1]) not in filled:
			sand_pt[1] += 1
		elif tuple([sand_pt[0]-1, sand_pt[1]+1]) not in filled:
			sand_pt[0] -= 1
			sand_pt[1] += 1
		elif tuple([sand_pt[0]+1, sand_pt[1]+1]) not in filled:
			sand_pt[0] += 1
			sand_pt[1] += 1
		else:
			filled.add(tuple(sand_pt))
			break
	if sand_pt[1] > max_h:
			break
	sand += 1

print(sand)

y_sort = sorted(filled, key=lambda x: x[1])
x_sort = sorted(filled, key=lambda x: x[0])
graph = [['.' for _ in range((x_sort[-1][0]-x_sort[0][0])+2)] for _ in range(y_sort[-1][1]+3)]

for tup in rocks:
	graph[tup[1]][tup[0]-x_sort[0][0]] = '#'

for tup in filled-rocks:
	graph[tup[1]][tup[0]-x_sort[0][0]] = 'o'

with open('out.txt', 'w+') as fileout:
	for line in graph:
		fileout.write(''.join(line) + '\n')