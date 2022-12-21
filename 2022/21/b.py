class Monkey:
	def __init__(self, name:str, value:str) -> None:
		self.name = name
		spval = value.split(' ')
		self.hasval = False
		if len(spval) == 1:
			self.value = int(spval[0])
			self.hasval = True
			self.valstr = f'{self.value}'
			if self.name == 'humn':
				self.valstr = 'humn'
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
				if monkey.name == 'root':
					monkey.valstr = f'{monkeydict[monkey.l].valstr} == {monkeydict[monkey.r].valstr}'
				elif monkey.op == '+':
					monkey.value = monkeydict[monkey.l].value + monkeydict[monkey.r].value
					if 'humn' in monkeydict[monkey.l].valstr or 'humn' in monkeydict[monkey.r].valstr:
						monkey.valstr = f'({monkeydict[monkey.l].valstr}+{monkeydict[monkey.r].valstr})'
					else:
						monkey.valstr = str(monkey.value)
				elif monkey.op == '-':
					monkey.value = monkeydict[monkey.l].value - monkeydict[monkey.r].value
					if 'humn' in monkeydict[monkey.l].valstr or 'humn' in monkeydict[monkey.r].valstr:
						monkey.valstr = f'({monkeydict[monkey.l].valstr}-{monkeydict[monkey.r].valstr})'
					else:
						monkey.valstr = str(monkey.value)
				elif monkey.op == '*':
					monkey.value = monkeydict[monkey.l].value * monkeydict[monkey.r].value
					if 'humn' in monkeydict[monkey.l].valstr or 'humn' in monkeydict[monkey.r].valstr:
						monkey.valstr = f'({monkeydict[monkey.l].valstr}*{monkeydict[monkey.r].valstr})'
					else:
						monkey.valstr = str(monkey.value)
				elif monkey.op == '/':
					monkey.value = monkeydict[monkey.l].value / monkeydict[monkey.r].value
					if 'humn' in monkeydict[monkey.l].valstr or 'humn' in monkeydict[monkey.r].valstr:
						monkey.valstr = f'({monkeydict[monkey.l].valstr}/{monkeydict[monkey.r].valstr})'
					else:
						monkey.valstr = str(monkey.value)

rootl, rootr = root_monkey.valstr.split(' == ')
humn = rootl if 'humn' in rootl else rootr
checkval = monkeydict[root_monkey.r].value if humn == rootl else monkeydict[root_monkey.l].value

while humn != 'humn':
	humn = humn[1:-1] # unwrap one layer of parens
	i = 0
	op = ''
	while op == '':
		if humn[i] in {'+', '-', '*', '/'}:
			op = humn[i]
			break
		elif humn[i] == '(': # ltr guarantees lparen
			break
		i += 1
	i = -1 if not op else i
	while op == '':
		if humn[i] in {'+', '-', '*', '/'}:
			op = humn[i]
			break
		elif humn[i] == '>': # ltr guarantees lparen
			break
		i -= 1
	humnl = humn[:i]
	humnr = humn[i+1:]
	humn = humnl if 'humn' in humnl else humnr
	val = float(humnr) if 'humn' in humnl else float(humnl)
	if op == '+':
		checkval -= val
	elif op == '*':
		checkval /= val
	elif op == '-':
		if humn == humnl:
			checkval += float(humnr)
		else:
			checkval = float(humnl) - checkval
	elif op == '/':
		if humn == humnl:
			checkval *= float(humnr)
		else:
			checkval = float(humnl) / checkval

print(checkval)