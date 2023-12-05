import re
nice = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		stripped = line.rstrip()
		if re.match(r'.*([a-z][a-z]).*\1', stripped) and re.match(r'.*([a-z]).\1', stripped):
			nice += 1

print(nice)