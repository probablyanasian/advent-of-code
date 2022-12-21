from functools import cache
import re

bps = []
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		bp = tuple(map(int, re.findall(r'([0-9]+)', line.rstrip())))
		bps.append(bp)

@cache
def find_best(bp:tuple[int], res:tuple[int]=(0,0,0,0), prev_poss=(False, False, False), state:tuple[int,int,int,int]=(1,0,0,0), t:int=24):
	if t == 0:
		# if state == (1, 4, 2, 2):
		# 	print(state, res)
		return res[3]
	poss = (res[0] >= bp[1], res[0] >= bp[2], res[0] >= bp[3] and res[1] >= bp[4])
	nothing, buy_ore, buy_clay, buy_obs, buy_geo = res[3], res[3], res[3], res[3], res[3] # init

	if res[0] >= bp[5] and res[2] >= bp[6]: # always go here
		new_poss = (poss[0], poss[1], poss[2])
		new_res = (res[0]-bp[5]+state[0], res[1]+state[1], res[2]-bp[6]+state[2], res[3]+state[3])
		return find_best(bp, new_res, new_poss, (state[0], state[1], state[2], state[3]+1), t-1)
	else:
		new_poss = poss
		new_res = (res[0]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
		nothing = find_best(bp, new_res, new_poss, (state[0], state[1], state[2], state[3]), t-1)
	if (not prev_poss[0]) and res[0] >= bp[1]: # means reached position and didn't skip on buying
		new_poss = (False, poss[1], poss[2])
		new_res = (res[0]-bp[1]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
		buy_ore = find_best(bp, new_res, new_poss, (state[0]+1, state[1], state[2], state[3]), t-1)
	if (not prev_poss[1]) and res[0] >= bp[2]:
		new_poss = (poss[0], False, poss[2])
		new_res = (res[0]-bp[2]+state[0], res[1]+state[1], res[2]+state[2], res[3]+state[3])
		buy_clay = find_best(bp, new_res, new_poss, (state[0], state[1]+1, state[2], state[3]), t-1)
	if (not prev_poss[2]) and res[0] >= bp[3] and res[1] >= bp[4]:
		new_poss = (poss[0], poss[1], False)
		new_res = (res[0]-bp[3]+state[0], res[1]-bp[4]+state[1], res[2]+state[2], res[3]+state[3])
		buy_obs = find_best(bp, new_res, new_poss, (state[0], state[1], state[2]+1, state[3]), t-1)
	return max(nothing, buy_ore, buy_clay, buy_obs, buy_geo)

sum = 0
for bp in bps:
	val = find_best(bp)
	print(val)
	print(bp[0] * val)
	sum += bp[0] * val

print(sum)