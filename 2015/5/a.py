import re
nice = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		stripped = line.rstrip()
		if not re.match(r'.*(ab|cd|pq|xy).*', stripped) and re.match(r'.*(.)\1.*', stripped) and len(re.findall(r'[aeiou]', stripped)) >= 3:
			nice += 1

print(nice)