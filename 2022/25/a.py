import re

def int_to_snafu(num:int, accum:str=''):
	if num == 0:
		return accum
	mod_val = num % 5
	new_num = num // 5
	if mod_val <= 2:
		return int_to_snafu(new_num, str(mod_val) + accum)
	elif mod_val == 3:
		return int_to_snafu(new_num+1, '=' + accum)
	elif mod_val == 4:
		return int_to_snafu(new_num+1, '-' + accum)

sum = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		a = int(re.sub(r'[-=]', '0', line.rstrip()), 5)
		b = int(re.sub(r'[1-2]', '0', line.rstrip()).replace('-', '1').replace('=', '2'), 5)
		sum += a - b

print(int_to_snafu(sum))