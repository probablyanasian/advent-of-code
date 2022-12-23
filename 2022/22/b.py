import math
import re

class Node:
	def __init__(self, char, y, x, fiducial=False) -> None:
		self.char = char
		self.y = y
		self.x = x
		self.fiducial = fiducial
	
	def get_value(self) -> int:
		return ((self.y+1)*1000) + ((self.x+1)*4)
	
	def __repr__(self) -> str:
		# return f'{self.char}'
		return f'({self.y}, {self.x})'

class Pointer:
	def __init__(self) -> None:
		self.x = 1
		self.y = 1
		self.dir = 0

	def turn(self, dir):
		if dir == 'L':
			self.dir -= 1
		elif dir == 'R':
			self.dir += 1
		self.dir %= 4
	
	def move(self, graph, count) -> None:
		while count > 0:
			if self.dir == 0:
				n_sp = graph[0][self.y][self.x+1].char
				if n_sp == '.':
					self.x += 1
				elif n_sp == '#':
					count = 0
				elif n_sp == '':
					if graph[1][self.y][edgelen+1].char == '.':
						graph = rotate(graph, 0)
						self.x = 1
					else:
						count = 0
			if self.dir == 2:
				n_sp = graph[0][self.y][self.x-1].char
				if n_sp == '.':
					self.x -= 1
				elif n_sp == '#':
					count = 0
				elif n_sp == '':
					if graph[1][self.y][0].char == '.':
						graph = rotate(graph, 2)
						self.x = edgelen # no need to sub b/c left pad space
					else:
						count = 0
			if self.dir == 1:
				n_sp = graph[0][self.y+1][self.x].char
				if n_sp == '.':
					self.y += 1
				elif n_sp == '#':
					count = 0
				elif n_sp == '':
					if graph[1][edgelen+1][self.x].char == '.':
						graph = rotate(graph, 1)
						self.y = 1
					else:
						count = 0
			if self.dir == 3:
				n_sp = graph[0][self.y-1][self.x].char
				if n_sp == '.':
					self.y -= 1
				elif n_sp == '#':
					count = 0
				elif n_sp == '':
					if graph[1][0][self.x].char == '.':
						graph = rotate(graph, 3)
						self.y = edgelen
					else:
						count = 0
			count -= 1
		return graph

	def get_value(self, graph) -> str:
		return f'{graph[0][self.y][self.x].get_value() + self.dir}'
flatgraph = []
size = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		graph_line = tuple(line.rstrip())
		for chr in graph_line:
			if chr != ' ': size += 1
		flatgraph.append(graph_line)
		if line.rstrip() == '':
			ins = file.readline().rstrip()

edgelen = int(math.sqrt(size // 6))

cubegraph = [[['' for _ in range(edgelen+2)] for _ in range(edgelen+2)] for _ in range(edgelen+2)] # use z, y, x coords z is bottom up.

# b/c I'm too dumb to understand matrices; linalg is next semester; sent help pls.
def rotate(graph, dir):
	tmpgraph = [[[Node('', -1, -1) for _ in range(edgelen+2)] for _ in range(edgelen+2)] for _ in range(edgelen+2)]
	if dir == 0:
		for dir_a in range(1, edgelen+1):
			for dir_b in range(1, edgelen+1):
				tmpgraph[edgelen-dir_b+1][edgelen+1][dir_a] = graph[dir_a][edgelen+1][dir_b]
				tmpgraph[edgelen-dir_a+1][0][dir_b] = graph[dir_b][0][dir_a]

				tmpgraph[edgelen-dir_b+1][dir_a][0] = graph[0][dir_a][dir_b]
				tmpgraph[edgelen+1][dir_a][dir_b] = graph[dir_b][dir_a][0]
				tmpgraph[edgelen-dir_b+1][dir_a][edgelen+1] = graph[edgelen+1][dir_a][dir_b]
				tmpgraph[0][dir_a][dir_b] = graph[dir_b][dir_a][edgelen+1]
		return tmpgraph
	elif dir == 2:
		for dir_a in range(1, edgelen+1):
			for dir_b in range(1, edgelen+1):
				tmpgraph[dir_a][edgelen+1][dir_b] = graph[edgelen-dir_b+1][edgelen+1][dir_a]
				tmpgraph[dir_b][0][dir_a] = graph[edgelen-dir_a+1][0][dir_b]
				
				tmpgraph[0][dir_a][dir_b] = graph[edgelen-dir_b+1][dir_a][0]
				tmpgraph[dir_b][dir_a][0] = graph[edgelen+1][dir_a][dir_b]
				tmpgraph[edgelen+1][dir_a][dir_b] = graph[edgelen-dir_b+1][dir_a][edgelen+1]
				tmpgraph[dir_b][dir_a][edgelen+1] = graph[0][dir_a][dir_b]
		return tmpgraph

	elif dir == 1:
		for dir_a in range(1, edgelen+1):
			for dir_b in range(1, edgelen+1):
				tmpgraph[edgelen-dir_b+1][dir_a][edgelen+1] = graph[dir_a][dir_b][edgelen+1]
				tmpgraph[edgelen-dir_b+1][dir_a][0] = graph[dir_a][dir_b][0]
				
				tmpgraph[0][dir_a][dir_b] = graph[dir_a][edgelen+1][dir_b]
				tmpgraph[edgelen-dir_a+1][edgelen+1][dir_b] = graph[edgelen+1][dir_a][dir_b]
				tmpgraph[edgelen+1][dir_a][dir_b] = graph[dir_a][0][dir_b]
				tmpgraph[dir_a][0][dir_b] = graph[0][edgelen-dir_a+1][dir_b]
		return tmpgraph
	
	elif dir == 3:
		for dir_a in range(1, edgelen+1):
			for dir_b in range(1, edgelen+1):
				tmpgraph[dir_a][dir_b][edgelen+1] = graph[edgelen-dir_b+1][dir_a][edgelen+1]
				tmpgraph[dir_a][dir_b][0] = graph[edgelen-dir_b+1][dir_a][0]
				
				tmpgraph[dir_a][edgelen+1][dir_b] = graph[0][dir_a][dir_b]
				tmpgraph[edgelen+1][dir_a][dir_b] = graph[edgelen-dir_a+1][edgelen+1][dir_b]
				tmpgraph[dir_a][0][dir_b] = graph[edgelen+1][dir_a][dir_b]
				tmpgraph[0][edgelen-dir_a+1][dir_b] = graph[dir_a][0][dir_b]
		return tmpgraph

# since I wasn't getting close to the leaderboard anyways; I wanted to do this algorithmically and handle any input.
def wrap(flatgraph, cubegraph, edge_tl, lastdir=-1):
	fiducial = True
	for y in range(edgelen):
		for x in range(edgelen):
			cubegraph[0][y+1][x+1] = Node(flatgraph[edge_tl[0]+y][edge_tl[1]+x], edge_tl[0]+y, edge_tl[1]+x, fiducial)
			fiducial = False
	if (edge_tl[1] + edgelen) < len(flatgraph[edge_tl[0]]) and lastdir != 2: # check right side
		cubegraph = rotate(wrap(flatgraph, rotate(cubegraph, 0), (edge_tl[0], edge_tl[1]+edgelen), 0), 2)
	if edge_tl[1] != 0 and flatgraph[edge_tl[0]][edge_tl[1] - edgelen] != ' ' and lastdir != 0: # check left side
		cubegraph = rotate(wrap(flatgraph, rotate(cubegraph, 2), (edge_tl[0], edge_tl[1]-edgelen), 2), 0)
	if edge_tl[1] < len(flatgraph[edge_tl[0]+edgelen]) and flatgraph[edge_tl[0]+edgelen][edge_tl[1]] != ' ' and lastdir != 3: # check bottom
		cubegraph = rotate(wrap(flatgraph, rotate(cubegraph, 1), (edge_tl[0]+edgelen, edge_tl[1]), 1), 3)
	if edge_tl[0] != 0 and edge_tl[1] < len(flatgraph[edge_tl[0]-edgelen]) and flatgraph[edge_tl[0]-edgelen][edge_tl[1]] != ' ' and lastdir != 1: # check top
		cubegraph = rotate(wrap(flatgraph, rotate(cubegraph, 3), (edge_tl[0]-edgelen, edge_tl[1]), 3), 1)
	return cubegraph

# topleft edge
tmpx = 0
tmpy = 0
cur = flatgraph[0][0]
while flatgraph[tmpy][tmpx] != '.':
	tmpx += 1

cubegraph = wrap(flatgraph, cubegraph, (tmpy, tmpx))

fw = re.findall(r'([0-9]+)', ins)
tr = re.findall(r'([RL])+', ins)

ptr = Pointer()

for ind in range(len(tr)):
	cubegraph = ptr.move(cubegraph, int(fw[ind]))
	ptr.turn(tr[ind])

cubegraph = ptr.move(cubegraph, int(fw[-1])) # stray last one
if cubegraph[0][1][edgelen].fiducial:
	ptr.turn('L')
elif cubegraph[0][edgelen][1].fiducial:
	ptr.turn('R')
elif cubegraph[0][edgelen][edgelen].fiducial:
	ptr.turn('L')
	ptr.turn('L') # ha, two left turns make a right.
print(ptr.get_value(cubegraph))