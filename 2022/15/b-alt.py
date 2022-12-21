import re

def manhattan(p1, p2):
	sum = 0
	sum += abs(p1[0] - p2[0])
	sum += abs(p1[1] - p2[1])
	return sum

# sensors = set()
# beacons = set()
check = set()
sensors = []
max_val = 4000001 # +1 for range maths
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		s_x, b_x = map(int, re.findall(r'x=([-\d]*)', line))
		s_y, b_y = map(int, re.findall(r'y=([-\d*]*)', line))

		man = manhattan((s_x, s_y), (b_x, b_y))
		sensors.append(((s_x, s_y), man))

		to_add = set()
		for i in range(man+1):
			# border up
			to_add.add((s_x-man-1+i, s_y+i))
			to_add.add((s_x+man+1-i, s_y+i))
			# border down
			to_add.add((s_x-man-1-i, s_y-i))
			to_add.add((s_x+man+1+i, s_y-i))
		
		to_rm = set()
		for val in to_add:
			if val[0] > max_val-1 or val[0] < 0 or val[1] > max_val-1 or val[1] < 0:
				to_rm.add(val)
		to_add -= to_rm

		check.update(to_add)

for sensor in sorted(sensors, key=lambda x: x[1], reverse=True):
	to_rm = set()
	for val in check:
		if manhattan(sensor[0], val) <= sensor[1]:
			to_rm.add(val)
	check -= to_rm

print(check)