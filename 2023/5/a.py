import enum

state = 0
seeds = []
changed = []
with open("input", "r") as inf:
	for line in inf:
		if state == 0:
			seeds = list(map(int, line.rstrip().split()[1:]))
			changed = [False for _ in range(len(seeds))]
			state += 1
			inf.readline() # remove blank
			inf.readline() # remove next header
		elif state == 1:
			if line != "\n":
				dest, src, rng = map(int, line.split())
				print("mapping")
				print(dest, src, rng)
				for idx, seed in enumerate(seeds):
					if (seed - src) < rng and (seed - src) >= 0 and not changed[idx]:
						seeds[idx] = (seed - src) + dest
						changed[idx] = True
			else:
				print(inf.readline()) # remove header
				changed = [False for _ in range(len(seeds))]
		print(f"SEEDS {seeds}")

print(min(seeds))