from functools import cache
import re

class Node:
	def __init__(self, id:str, flowrate:int, nodes:list[str]):
		self.id = id
		self.flowrate = flowrate
		self.connected = nodes
		self.opened = False
		self.traversal = []
		self.traversal_weights = dict()
		self.visited = False # used for weights

	def open(self):
		self.opened = True
		return self

	def __repr__(self):
		return f'{self.id}: {self.traversal_weights}'

nodes = {}
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		valves = re.findall(r'([A-Z]{2})', line)
		flow = int(re.findall(r'rate=([0-9]*);', line)[0])
		node = Node(valves[0], flow, valves[1:])
		nodes[valves[0]] = node

# shite djikstra instead of floyd warshall b/c I'm unintelligent
start_node: Node
for start_node in nodes.values():
	round = 1
	start_node.visited = True
	to_visit = [nodes[n_node] for n_node in start_node.connected]
	dist = {}
	while len(to_visit) != 0:
		node: Node
		temp = set()
		for node in to_visit:
			if node.visited:
				continue
			if node.flowrate != 0:
				dist[node.id] = round
			node.visited = True
			temp.update(set([nodes[n_node] for n_node in node.connected]))
		round += 1
		to_visit = list(temp.copy())
	start_node.traversal_weights = dist
	for node in nodes.values():
		node.visited = False

print(nodes)
print(len(nodes['AA'].traversal_weights))
curloc = 'AA'
time = 30

node: Node
@cache
def find_best(node: Node, t:int, left:frozenset):
	return max([node.flowrate*(t-1) + find_best(nodes[n_node], t-1-node.traversal_weights[n_node], left-{n_node}) for n_node in left if node.traversal_weights[n_node] < t] + [node.flowrate*(t-1)])

#31 to account fof AA node traversal time
print(find_best(nodes['AA'], 31, frozenset([node.id for node in nodes.values() if node.flowrate != 0])))