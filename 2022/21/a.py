class Monkey:
	def __init__(self, name:str, value:str) -> None:
		self.name = name
		spval = value.split(' ')
		self.hasval = False
		if len(spval) == 1:
			self.value = int(spval[0])
			self.hasval = True
		else:
			self.value = None
			self.l = spval[0]
			self.op = spval[1]
			self.r = spval[2]

	def __repr__(self) -> str:
		return f'{self.value if self.hasval else self.l + self.op + self.r}'

monkeydict: dict[str, Monkey]
monkeydict = {}
root_monkey = None
with open("input", "r") as file:
	for line in iter(file.readline, ''):
		name, value = line.rstrip().split(': ')
		new_monkey = Monkey(name, value)
		monkeydict[name] = new_monkey
		if name == 'root':
			root_monkey = new_monkey

while not root_monkey.hasval:
	monkey: Monkey
	for monkey in monkeydict.values():
		if not monkey.hasval:
			if monkeydict[monkey.l].hasval and monkeydict[monkey.r].hasval:
				monkey.hasval = True
				if monkey.op == '+':
					monkey.value = monkeydict[monkey.l].value + monkeydict[monkey.r].value
				elif monkey.op == '-':
					monkey.value = monkeydict[monkey.l].value - monkeydict[monkey.r].value
				elif monkey.op == '*':
					monkey.value = monkeydict[monkey.l].value * monkeydict[monkey.r].value
				elif monkey.op == '/':
					monkey.value = monkeydict[monkey.l].value / monkeydict[monkey.r].value

print(root_monkey.value)
