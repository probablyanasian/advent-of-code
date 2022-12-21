import re

def manhattan(p1, p2):
	sum = 0
	sum += abs(p1[0] - p2[0])
	sum += abs(p1[1] - p2[1])
	return sum

# sensors = set()
# beacons = set()
check = set()
max_val = 4000001 # +1 for range maths
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		s_x, b_x = map(int, re.findall(r'x=([-\d]*)', line))
		s_y, b_y = map(int, re.findall(r'y=([-\d*]*)', line))
		# sensors.add((s_x, s_y))
		# beacons.add((b_x, b_y))
		man = manhattan((s_x, s_y), (b_x, b_y))

		for i in range(man+1):
			# border up
			check.add((s_x-man-1+i, s_y+i))
			check.add((s_x+man+1-i, s_y+i))
			# border down
			check.add((s_x-man-1-i, s_y-i))
			check.add((s_x+man+1+i, s_y-i))
		print(line)

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		s_x, b_x = map(int, re.findall(r'x=([-\d]*)', line))
		s_y, b_y = map(int, re.findall(r'y=([-\d*]*)', line))
		# sensors.add((s_x, s_y))
		# beacons.add((b_x, b_y))
		man = manhattan((s_x, s_y), (b_x, b_y))
		to_rm = set()
		for val in check:
			if manhattan((s_x, s_y), val) <= man:
				to_rm.add(val)
		check -= to_rm
		print(line)

to_rm = set()
for val in check:
	if val[0] > max_val-1 or val[0] < 0:
		to_rm.add(val)
	elif val[1] > max_val-1 or val[1] < 0:
		to_rm.add(val)

check -= to_rm
print(check)