import re

tot = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		stripped = line.rstrip()
		tot += len(re.findall(r'"|\\', stripped)) + 2
		
print(tot)
