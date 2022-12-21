class Node:
	def __init__(self, loc:tuple[int, int, int], mat:bool) -> None:
		self.x = loc[0]
		self.y = loc[1]
		self.z = loc[2]
		self.material = mat # true for obsidian
		self.traversed = False
		if self.material:
			self.traversed = True
		
graph = [[[Node((x,y,z), False) for z in range(22)] for y in range(22)] for x in range(22)]
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		loc = tuple(map(int, line.rstrip().split(',')))
		graph[loc[0]][loc[1]][loc[2]] = Node(loc, True)

def crawl(block:tuple[int, int, int]):
	to_search = set()
	for dir in [1, -1]:
		if loc[0] >= 0 and loc[0] <= 21 and not graph[block[0] + dir][block[1]][block[2]].traversed:
			to_search.add((block[0] + dir, block[1], block[2]))
		if loc[1] >= 0 and loc[1] <= 21 and not graph[block[0]][block[1] + dir][block[2]].traversed:
			to_search.add((block[0], block[1] + dir, block[2]))
		if loc[2] >= 0 and loc[2] <= 21 and not graph[block[0]][block[1]][block[2] + dir].traversed:
			to_search.add((block[0], block[1], block[2] + dir))

	return to_search

def check(block:tuple[int, int, int]):
	obs_touched = 0
	for dir in [1, -1]:
		if graph[block[0] + dir][block[1]][block[2]].material:
			obs_touched += 1
		if graph[block[0]][block[1] + dir][block[2]].material:
			obs_touched += 1
		if graph[block[0]][block[1]][block[2] + dir].material:
			obs_touched += 1
	return obs_touched

outside = set((0, 0, 0))
to_search = crawl((0, 0, 0))
graph[0][0][0].traversed = True
touched = 0
while len(to_search) > 0:
	temp = set()
	for loc in to_search:
		touched += check(loc)
		outside.add(loc)
		graph[loc[0]][loc[1]][loc[2]].traversed = True
		temp.update(crawl(loc))
	to_search = temp.copy()

print(touched)