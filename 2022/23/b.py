from functools import cache

class Elf:
	def __init__(self, y:int, x:int) -> None:
		self.y = y
		self.x = x

	def get_y(self):
		return self.y
	
	def get_x(self):
		return self.x
	
	def get_loc(self):
		return (self.y, self.x)

	@cache
	def decision(self, locs, cyc):
		n = (self.y-1, self.x) in locs
		s = (self.y+1, self.x) in locs
		e = (self.y, self.x+1) in locs
		w = (self.y, self.x-1) in locs
		ne = (self.y-1, self.x+1) in locs
		nw = (self.y-1, self.x-1) in locs
		se = (self.y+1, self.x+1) in locs
		sw = (self.y+1, self.x-1) in locs
		if not (n or s or e or w or ne or nw or se or sw):
			return self.get_loc()
		opts = [
		 (not(n or ne or nw), (self.y-1, self.x)),
		 (not(s or se or sw), (self.y+1, self.x)),
		 (not(w or nw or sw), (self.y, self.x-1)),
		 (not(e or ne or se), (self.y, self.x+1))
		]

		for ind in range(4):
			if opts[(cyc+ind) % 4][0]:
				return opts[(cyc+ind) % 4][1]
		
		return self.get_loc()

	def set_loc(self, loc):
		self.y = loc[0]
		self.x = loc[1]

	def __repr__(self) -> str:
		return f'{self.y} {self.x}'

elves: list[Elf]
elves = []
with open("input", "r") as file:
	y = 0
	for line in iter(file.readline, ''):
		for ind, char in enumerate(line.rstrip()):
			if char == '#':
				elves.append(Elf(y, ind))
		y += 1

curlocs = frozenset({elf.get_loc() for elf in elves})
cyc = 0
for _ in range(1000):
	move = {}
	move_set = set()
	for elf in elves:
		move[elf.decision(curlocs, cyc)] = move[elf.decision(curlocs, cyc)] + 1 if elf.decision(curlocs, cyc) in move else 1
		move_set.add(elf.decision(curlocs, cyc))
	if curlocs == move_set:
		break
	# 	print(elf)
	# print('')
	tmplocs = set()
	for elf in elves:
		if move[elf.decision(curlocs, cyc)] == 1:
			elf.set_loc(elf.decision(curlocs, cyc))
		tmplocs.add(elf.get_loc())
	curlocs = frozenset(tmplocs.copy())
	cyc += 1

print(cyc+1)