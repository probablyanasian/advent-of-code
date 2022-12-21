import re

def manhattan(p1, p2):
	sum = 0
	sum += abs(p1[0] - p2[0])
	sum += abs(p1[1] - p2[1])
	return sum

# sensors = set()
# beacons = set()
y_val = 2000000
beacon_x = set()
beacon_excl = set()
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		s_x, b_x = map(int, re.findall(r'x=([-\d]*)', line))
		s_y, b_y = map(int, re.findall(r'y=([-\d*]*)', line))
		# sensors.add((s_x, s_y))
		# beacons.add((b_x, b_y))
		if b_y == y_val:
			beacon_x.add(b_x)
		man = manhattan((s_x, s_y), (b_x, b_y))
		x_spread = man - abs(s_y-y_val)
		print(range(s_x-x_spread, s_x+x_spread))
		for x in range(s_x-x_spread, s_x+x_spread+1):
			beacon_excl.add(x)

print(len(beacon_excl-beacon_x))
# x_sorted = sorted(sensors+beacons, key=lambda x: x[0])
# y_sorted = sorted(sensors+beacons, key=lambda x: x[1])

