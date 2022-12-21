class Node:
	def __init__(self, value) -> None:
		self.value = value

	def __repr__(self) -> str:
		return f'{self.value}'
		
l = []
zero_node = None
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		new_node = Node(int(line.rstrip()))
		l.append(new_node)
		if new_node.value == 0:
			zero_node = new_node

enc = l.copy()
n: Node
for n in l:
	n_ind = enc.index(n)
	item = enc.pop(n_ind)
	assert item == n
	enc.insert((n_ind + n.value) % len(enc), n)

print(enc)
zero_ind = enc.index(zero_node)

sum = 0
for ind in [1000, 2000, 3000]:
	x: Node
	x = enc[(zero_ind+ind)%len(enc)]
	sum += x.value
	print(x)

print(sum)
