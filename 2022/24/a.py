from functools import cache
from collections import deque

class Blizzard:
	def __init__(self, coord, dir) -> None:
		self.y = coord[0]
		self.x = coord[1]
		self.dir = dir
	
	def move(self, graph):
		if self.dir == 0:
			if self.x == len(graph[self.y]) - 2:
				self.x = 1
			else:
				self.x += 1
		elif self.dir == 2:
			if self.x == 1:
				self.x = len(graph[self.y]) - 2
			else:
				self.x-= 1
		elif self.dir == 1:
			if self.y == len(graph) - 2:
				self.y = 1
			else:
				self.y += 1
		elif self.dir == 3:
			if self.y == 1:
				self.y = len(graph) - 2
			else:
				self.y -= 1
		return self.get_loc()

	def get_loc(self):
		return (self.y, self.x)

	def __repr__(self) -> str:
		return f'({self.y}, {self.x})'

graph = []
blizz: list[Blizzard]
blizz = []
with open("input", "r") as file:
	y=0
	for line in iter(file.readline, ''):
		line = line.rstrip()
		graph.append(tuple(line))
		for ind, char in enumerate(list(line)):
			if char == '>':
				blizz.append(Blizzard((y, ind), 0))
			if char == '<':
				blizz.append(Blizzard((y, ind), 2))
			if char == '^':
				blizz.append(Blizzard((y, ind), 3))
			if char == 'v':
				blizz.append(Blizzard((y, ind), 1))
		y+= 1

graph = tuple(graph) # hashable
blizz = tuple(blizz)

blizzlocs = {i: {bliz.move(graph) for bliz in blizz} for i in range(1000)} # preload

goal = (len(graph)-1, len(graph[0])-2)

walk_queue = deque() # left aligned queue
walk_queue.append((0, 1, 0)) # start
round = -1 # cause counting
fin = False
while round < 10_000 and not fin: # quench a runaway
	round += 1
	# print(walk_queue)
	queue_set = set()
	for _ in range(len(walk_queue)): # consume this round
		curloc = walk_queue.popleft()
		blizzloc = blizzlocs[curloc[2]]
		if (curloc[0], curloc[1]) == goal:
			print(curloc)
			print(round)
			fin = True
			break
		if not((curloc[0]+1, curloc[1]) in blizzloc) and graph[curloc[0]+1][curloc[1]] != '#':
			queue_set.add((curloc[0]+1, curloc[1], curloc[2]+1))

		if not((curloc[0]-1, curloc[1]) in blizzloc) and curloc[0] > 1:
			queue_set.add((curloc[0]-1, curloc[1], curloc[2]+1))

		if not((curloc[0], curloc[1]+1) in blizzloc) and graph[curloc[0]][curloc[1]+1] != '#':
			queue_set.add((curloc[0], curloc[1]+1, curloc[2]+1))

		if not((curloc[0], curloc[1]-1) in blizzloc) and curloc[1] > 1:
			queue_set.add((curloc[0], curloc[1]-1, curloc[2]+1))
		
		if not((curloc[0], curloc[1]) in blizzloc):
			queue_set.add((curloc[0], curloc[1], curloc[2]+1))
	walk_queue.extend(queue_set)
