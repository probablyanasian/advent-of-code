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
max_h = max(rocks, key=lambda x: x[1])[1] + 1 # sub 1 to emulate floor
sand = 0
while True:
	sand_pt = [500, 0]
	while True:
		if sand_pt[1] == max_h:
			filled.add(tuple(sand_pt))
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
	sand += 1
	if (500, 0) in filled:
		break

print(sand)
