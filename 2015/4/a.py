import hashlib

app = 0
inp = open('input', 'r').read().rstrip()

while True:
	if hashlib.md5(f'{inp}{app}'.encode('utf-8')).hexdigest().startswith('00000'):
		print(app)
		break
	app += 1
