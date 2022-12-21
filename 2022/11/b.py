from collections import deque

class Item:
	def __init__(self, value):
		self.mod_translation = {}
		self.value = int(value)
		self.mod_table = []
	
	def get(self, modulo):
		if modulo in self.mod_translation:
			return self.mod_table[self.mod_translation[modulo]]

	def __mul__(self, other):
		if self == other:
			for key in self.mod_translation.keys():
				mod_value = self.mod_table[self.mod_translation[key]]
				self.mod_table[self.mod_translation[key]] *= mod_value
				self.mod_table[self.mod_translation[key]] %= key
		elif isinstance(other, int):
			for key in self.mod_translation.keys():
				self.mod_table[self.mod_translation[key]] *= other
				self.mod_table[self.mod_translation[key]] %= key
		return self

	def __add__(self, other):
		if self == other:
			for key in self.mod_translation.keys():
				mod_value = self.mod_table[self.mod_translation[key]]
				self.mod_table[self.mod_translation[key]] += mod_value
				self.mod_table[self.mod_translation[key]] %= key
		elif isinstance(other, int):
			for key in self.mod_translation.keys():
				self.mod_table[self.mod_translation[key]] += other
				self.mod_table[self.mod_translation[key]] %= key
		return self

	def __repr__(self):
		return f'Item({self.value})'

class Monkey:
	def __init__(self):
		self.items = deque() # popleft as queue, end is right aligned
		self.number = 0
		self.op = ''
		self.op_val = ''
		self.div_val = 1
		self.true_monkey = 0
		self.false_monkey = 0
		self.inspection_count = 0

	def calc_ret_which(self):
		if not self.items:
			return
		self.inspection_count += 1
		if self.op == '+':
			if self.op_val == 'old':
				print('did')
				self.items[0] += self.items[0]
			else:
				self.items[0] += int(self.op_val)
		elif self.op == '*':
			if self.op_val == 'old':
				self.items[0] *= self.items[0]
			else:
				self.items[0] *= int(self.op_val)

		if (self.items[0].get(self.div_val) == 0):
			return self.true_monkey
		else:
			return self.false_monkey

	def __repr__(self):
		return f'Monkey_{self.number} inspected {self.inspection_count}'

monkey_list: list[Monkey]
monkey_list = []
divs = []
items = []
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		_, monkey_num = line.rstrip(':\n').split()
		new_monkey = Monkey()
		monkey_list.append(new_monkey)
		new_monkey.number = len(monkey_list)-1
		monkey_items = list(map(Item, file.readline().rstrip().split(': ')[1].split(', ')))
		items.extend(monkey_items)
		new_monkey.items.extend(monkey_items)
		new_monkey.op, new_monkey.op_val = file.readline().rstrip().split('= old ')[1].split(' ')
		new_monkey.div_val = int(file.readline().rstrip().split(' ')[-1])
		divs.append(new_monkey.div_val)
		new_monkey.true_monkey = int(file.readline().rstrip().split(' ')[-1])
		new_monkey.false_monkey = int(file.readline().rstrip().split(' ')[-1])
		file.readline() # discard newline

div_dict = {}
for ind, div in enumerate(sorted(divs)):
	div_dict[div] = ind

item: Item
for item in items:
	item.mod_table = [item.value for _ in range(len(divs))]
	item.mod_translation = div_dict
print(item.mod_translation)

# print(monkey_list)

for round in range(10000):
	monkey: Monkey # typehint
	for monkey in monkey_list:
		while monkey.items:
			move = monkey.calc_ret_which() # necessary bc rhs evals first
			monkey_list[move].items.append(monkey.items.popleft())

srt = sorted(monkey_list, key=lambda x: x.inspection_count, reverse=True)
print(srt[0].inspection_count * srt[1].inspection_count)