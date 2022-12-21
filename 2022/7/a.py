from collections import deque

directory = {'/': {}}
dir_pointer = deque()
dir_pointer.append(directory['/'])

with open("input", "r") as file:
	for line in iter(file.readline, ''):
		line = line.rstrip()
		if line.startswith('$ cd'):
			if line[5:] == '/':
				dir_pointer.clear()
				dir_pointer.append(directory['/'])
			elif line[5:] == '..':
				dir_pointer.pop()
			else:
				dir_pointer.append(dir_pointer[-1][line[5:]])
		elif line.startswith('$ ls'):
			while True:
				last_pos = file.tell()
				cur_line = file.readline().rstrip()
				if cur_line == '' or cur_line.startswith('$ '):
					break
				cur_split = cur_line.split(" ")
				if cur_split[0] == 'dir':
					dir_pointer[-1][cur_split[1]] = {}
				else:
					dir_pointer[-1][cur_split[1]] = int(cur_split[0])
			file.seek(last_pos)

directories = []
def get_dirs(pointer: dict):
	if isinstance(pointer, int):
		return
	for key in pointer.keys():
		if isinstance(pointer[key], dict):
			get_dirs(pointer[key])
			directories.append(pointer[key])

get_dirs(directory['/'])

def calc_size(pointer: dict):
	if isinstance(pointer, int):
		return pointer
	
	sum = 0
	for key in pointer.keys():
		sum += calc_size(pointer[key])
	
	return sum

print('total size: ' + str(calc_size(directory['/'])))

sum = 0
for dir_pointer in directories:
	if (size := calc_size(dir_pointer)) < 100000:
		sum += size

print('total sum of under 100000s: ' + str(sum))