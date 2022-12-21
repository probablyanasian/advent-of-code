class Node:
	def __init__(self, h_char:str, y:int, x:int):
		self.y = y
		self.x = x
		self.visited = False
		self.isgoal = False
		self.distance = 0
		if h_char == 'S':
			self.height = ord('a')
		elif h_char == 'E':
			self.visited = True
			self.height = ord('z')
		else:
			self.height = ord(h_char)

		if self.height == ord('a'):
			self.isgoal = True
	def traversable(self, other):
		if not self.visited and self.height >= other.height-1:
			return True
		return False

	def __repr__(self) -> str:
		return f'{self.y} {self.x} {chr(self.height)}'

graph: list[Node]
graph = []

start_node = Node('A', -1, -1)
with open("input", "r") as file:
	y_ind = -1
	for line in iter(file.readline, ''):
		graph.append([])
		y_ind += 1
		for x_ind, h in enumerate(line.rstrip()):
			graph[y_ind].append(Node(h, y_ind, x_ind))
			if h == 'E':
				start_node = graph[y_ind][x_ind]

# max values *are* visitable
max_y = len(graph)-1
max_x = len(graph[0])-1

print(start_node)
round = 0
last_round_visited = [start_node]
visited_end = False
while not visited_end:
	round += 1 # distance to reach
	temp_visited = []
	for cur_node in last_round_visited:
		check_nodes = []
		if cur_node.x - 1 >= 0: # L traversal
			check_nodes.append(graph[cur_node.y][cur_node.x-1])
		if cur_node.x + 1 <= max_x: # R traversal
			check_nodes.append(graph[cur_node.y][cur_node.x+1])
		if cur_node.y - 1 >= 0: # U traversal
			check_nodes.append(graph[cur_node.y-1][cur_node.x])
		if cur_node.y + 1 <= max_y: # D traversal
			check_nodes.append(graph[cur_node.y+1][cur_node.x])

		for check_node in check_nodes:
			check_node: Node
			if check_node.traversable(cur_node):
				check_node.distance = round
				check_node.visited = True
				temp_visited.append(check_node)
				if check_node.isgoal:
					visited_end = True
					print(check_node.distance)
	last_round_visited = temp_visited.copy()
	temp_visited.clear()