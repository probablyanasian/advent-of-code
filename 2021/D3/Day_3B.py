lines = []
with open('D3_input.txt', 'r') as fopen:
	lines = [line.rstrip() for line in fopen]

def oxy_gen(val_list):
	if len(val_list) == 1:
		return val_list[0]
	one_count = 0
	for val in val_list:
		if val[0] == '1':
			one_count += 1
	half = len(val_list)/2	
	if one_count < half:
		gt = '0'
	else:
		gt = '1'
	
	parse_list = [val[1:] for val in val_list if val[0] == gt]
	return gt + oxy_gen(parse_list)

def scrubber(val_list):
	if len(val_list) == 1:
		return val_list[0]
	one_count = 0
	for val in val_list:
		print(val)
		if val[0] == '1':
			one_count += 1
	half = len(val_list)/2	
	if one_count >= half:
		lt = '0'
	else:
		lt = '1'
	
	parse_list = [val[1:] for val in val_list if val[0] == lt]
	return lt + scrubber(parse_list)

oxy = oxy_gen(lines)
scr = scrubber(lines)
print(oxy, int(oxy, 2))
print(scr, int(scr, 2))
print(int(oxy, 2)*int(scr, 2))
