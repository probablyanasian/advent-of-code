import re

class Pointer:
	def __init__(self, graph) -> None:
		self.x = 0
		self.y = 0
		self.dir = 0 
		cur = graph[0][0]
		while graph[self.y][self.x] != '.':
			self.x += 1

	def turn(self, dir):
		if dir == 'L':
			self.dir -= 1
		elif dir == 'R':
			self.dir += 1
		self.dir %= 4
	
	def move(self, graph, count) -> None:
		while count > 0:
			if self.dir == 0: 
				if (self.x + 1) == len(graph[self.y]): # right edge
					tmpx = 0
					while graph[self.y][tmpx] == ' ':
						tmpx += 1
					if graph[self.y][tmpx] == '.':
						self.x = tmpx
					else:
						count = 0
				else:
					n_sp = graph[self.y][self.x+1]
					if n_sp == '.':
						self.x += 1
					elif n_sp == '#':
						count = 0
			elif self.dir == 2:
				n_sp = graph[self.y][self.x-1]
				if self.x == 0 or n_sp == ' ': # left edge
					if graph[self.y][-1] == '.':
						self.x = -1 % len(graph[self.y])
				else:
					if n_sp == '.':
						self.x -= 1
						self.x %= len(graph[self.y])
					elif n_sp == '#':
						count = 0
			elif self.dir == 1:
				if self.y + 1 == len(graph) or self.x >= len(graph[self.y+1]) or graph[self.y+1][self.x] == ' ':
					tmpy = 0
					while True:
						if self.x >= len(graph[tmpy]) or graph[tmpy][self.x] == ' ':
							tmpy += 1
						elif graph[tmpy][self.x] == '.':
							self.y = tmpy
							break
						elif graph[tmpy][self.x] == '#':
							count = 0
							break
				else:
					n_sp = graph[self.y+1][self.x]
					if n_sp == '.':
						self.y += 1
					elif n_sp == '#':
						count = 0
			elif self.dir == 3:
				if self.y == 0 or graph[self.y-1][self.x] == ' ': # top edge
					tmpy = -1
					while True:
						if self.x >= len(graph[tmpy]) or graph[tmpy][self.x] == ' ':
							tmpy -= 1
						elif graph[tmpy][self.x] == '.':
							self.y = tmpy % len(graph)
							break
						elif graph[tmpy][self.x] == '#':
							count = 0
							break
				else:
					n_sp = graph[self.y-1][self.x]
					if n_sp == '.':
						self.y -= 1
					elif n_sp == '#':
						count = 0
			count -= 1

	def __repr__(self) -> str:
		return f'{self.y}, {self.x}, {self.dir}, {((self.y+1)*1000) + ((self.x+1)*4) + (self.dir)}'
graph = []
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		graph.append(tuple(line.rstrip()))
		if line.rstrip() == '':
			ins = file.readline().rstrip()

fw = re.findall(r'([0-9]+)', ins)
tr = re.findall(r'([RL])+', ins)

ptr = Pointer(graph)

for ind in range(len(tr)):
	ptr.move(graph, int(fw[ind]))
	ptr.turn(tr[ind])

ptr.move(graph, int(fw[-1])) # stray last one

print(ptr)