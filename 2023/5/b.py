import enum

state = 0
seeds = []
changed = []
with open("input", "r") as inf:
	for line in inf:
		if state == 0:
			temp_sds = list(map(int, line.rstrip().split()[1:]))
			for x in range(0, len(temp_sds), 2):
				seeds.extend((temp_sds[x], temp_sds[x]+temp_sds[x+1]-1))
			changed = [False for _ in range(len(seeds))]
			state += 1
			inf.readline() # remove blank
			inf.readline() # remove next header

		elif state == 1:
			if line != "\n":
				dest, src, rng = map(int, line.split())

				# FIND DECISION BOUNDARY, L, IN, R
				for idx, seed in enumerate(seeds):
					if idx % 2 == 1:
						continue
					bound_a = None
					bound_b = None
					if not changed[idx]:
						if (seeds[idx] - src) < 0:
							bound_a = 0 # left of region
						elif (seeds[idx] - src) < rng:
							bound_a = 1 # inside
						else:
							bound_a = 2 # right of region

						if (seeds[idx+1] - src) < 0:
							bound_b = 0 # left of region
						elif (seeds[idx+1] - src) < rng:
							bound_b = 1 # inside
						else:
							bound_b = 2 # right of region

						if (bound_a == 0 and bound_b == 0) or (bound_a == 2 and bound_b == 2):
							continue # outside of mapped range
						else:
							# something overlaps, need to find out how and break the chunk
							if (bound_a == 1 and bound_b == 1):
								# fully mapped, easy
								seeds[idx] = (seeds[idx] - src) + dest
								seeds[idx+1] = (seeds[idx+1] - src) + dest
								changed[idx] = True
							elif (bound_a == 0 and bound_b == 1):
								# right overlap
								# create new boundary
								seeds.append(dest)
								seeds.append((seeds[idx+1] - src) + dest)
								# shrink right
								seeds[idx+1] = src - 1
								changed.extend((True, True))
							elif (bound_a == 1 and bound_b == 2):
								# left_overlap
								# create new boundary
								seeds.extend(((seeds[idx] - src) + dest, dest + rng - 1))
								# shrink left
								seeds[idx] = src + rng
								changed.extend((True, True))
							elif (bound_a == 0 and bound_b == 2):
								#internal fracture
								seeds.extend((src+rng, seeds[idx+1])) # add right-most frag 
								seeds[idx+1] = src - 1 # set left-most frag right bound
								# add internal frag
								seeds.extend((dest, dest+rng-1))
								# shrink right
								changed.extend((True, True, True, True))

			else:
				inf.readline() # remove header
				changed = [False for _ in range(len(seeds))]

print(min(seeds))