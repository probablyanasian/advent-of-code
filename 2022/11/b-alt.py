from collections import deque

class Monkey:
	mod_composite = 0
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
				self.items[0] += self.items[0]
			else:
				self.items[0] += int(self.op_val)
		elif self.op == '*':
			if self.op_val == 'old':
				self.items[0] *= self.items[0]
			else:
				self.items[0] *= int(self.op_val)
		self.items[0] %= self.mod_composite

		if (self.items[0] % self.div_val == 0):
			return self.true_monkey
		else:
			return self.false_monkey

	def __repr__(self):
		return f'Monkey {self.number} inspected {self.inspection_count}'

monkey_list: list[Monkey]
monkey_list = []
mod_composite = 1
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		_, monkey_num = line.rstrip(':\n').split()
		new_monkey = Monkey()
		monkey_list.append(new_monkey)
		new_monkey.number = len(monkey_list)-1
		new_monkey.items.extend(map(int, file.readline().rstrip().split(': ')[1].split(', ')))
		new_monkey.op, new_monkey.op_val = file.readline().rstrip().split('= old ')[1].split(' ')
		new_monkey.div_val = int(file.readline().rstrip().split(' ')[-1])
		mod_composite *= new_monkey.div_val
		new_monkey.true_monkey = int(file.readline().rstrip().split(' ')[-1])
		new_monkey.false_monkey = int(file.readline().rstrip().split(' ')[-1])
		file.readline() # discard newline

Monkey.mod_composite = mod_composite
# print(monkey_list)

for _ in range(10000):
	monkey: Monkey # typehint
	for monkey in monkey_list:
		while monkey.items:
			move = monkey.calc_ret_which() # necessary bc rhs evals first
			monkey_list[move].items.append(monkey.items.popleft())
srt = sorted(monkey_list, key=lambda x: x.inspection_count, reverse=True)
print(srt)
print(srt[0].inspection_count * srt[1].inspection_count)