import re

str_sum = 0
mem_sum = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		stripped = line.rstrip()
		str_sum += len(stripped)
		mem_tot = len(stripped) - 2 # encapping double quotes
		mem_tot -= len(re.findall(r'\\"|\\\\', stripped)) # escaped double quote or slash
		mem_tot -= len(re.findall(r'(\\x[0-9a-f]{2})', stripped)) * 3
		mem_sum += mem_tot
		
print(str_sum - mem_sum)
