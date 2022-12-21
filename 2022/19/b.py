from functools import cache
import re

bps = []
with open("input2", "r") as file:
	for line in iter(file.readline, ''):
		bp = tuple(map(int, re.findall(r'([0-9]+)', line.rstrip())))
		bps.append(bp)

@cache
def summation(t:int):
	if t == 0:
		return 0
	return t+summation(t-1)

@cache
def find_best(bp:tuple[int], res:tuple[int]=(0,0,0,0), prev_poss=(False, False, False), state:tuple[int,int,int,int]=(1,0,0,0), best=0, t:int=32):
	if t == 0:
		return res[3]
	if res[3] + summation(t+state[3]) - summation(state[3]) < best:
		return res[3]
	# if state == (1, 3, 1, 0):
	# 	print(25-t, res, prev_poss)
	poss = (prev_poss[0] or res[0] >= bp[1], prev_poss[1] or res[0] >= bp[2], prev_poss[2] or (res[0] >= bp[3] and res[1] >= bp[4]))
	nothing, buy_ore, buy_clay, buy_obs, buy_geo = res[3], res[3], res[3], res[3], res[3] # init

	if res[0] >= bp[5] and res[2] >= bp[6]: # always go here, prune rest
		new_res = (res[0]-bp[5]+state[0], res[1]+state[1], res[2]-bp[6]+state[2], res[3]+state[3])
		return find_best(bp, new_res, prev_poss, (state[0], state[1], state[2], state[3]+1), best, t-1)
	else:
		if not prev_poss[2] and res[0] >= bp[3] and res[1] >= bp[4] and state[3] < bp[6]: # obs
			new_res = (res[0]-bp[3]+state[0], res[1]-bp[4]+state[1], res[2]+state[2], res[3]+state[3])
			buy_obs = find_best(bp, new_res, (False, False, False), (state[0], state[1], state[2]+1, state[3]), best, t-1)
			best = max(best, buy_obs)
		if not prev_poss[1] and res[0] >= bp[2] and state[2] < bp[4]: # clay
			new_res = (res[0]-bp[2]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
			buy_clay = find_best(bp, new_res, (False, False, False), (state[0], state[1]+1, state[2], state[3]), best, t-1)
			best = max(best, buy_clay)
		if not prev_poss[0] and res[0] >= bp[1] and state[0] < (bp[2] + bp[3] + bp[5]): # ore
			new_res = (res[0]-bp[1]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
			buy_ore = find_best(bp, new_res, (False, False, False), (state[0]+1, state[1], state[2], state[3]), best, t-1)
			best = max(best, buy_ore)
		new_res = (res[0]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
		nothing = find_best(bp, new_res, poss, state, best, t-1)
	return max(nothing, buy_ore, buy_clay, buy_obs, buy_geo)

tot = 1
for bp in bps:
	val = find_best(bp)
	print(val)
	tot *= val
print(tot)