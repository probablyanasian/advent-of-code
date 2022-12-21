from functools import cmp_to_key
import json

def in_order(left: list, right: list) -> bool:
	if len(left) == 0 and len(right) == 0: return # null
	if len(left) == 0: return True
	if len(right) == 0: return False
	if isinstance(left[0], int) and isinstance(right[0], int): # ints
		if left[0] < right[0]:
			return True
		elif right[0] < left[0]:
			return False
		else:
			return in_order(left[1:], right[1:])
	elif isinstance(left[0], list) and isinstance(right[0], list): # lists
		if (ret := in_order(left[0], right[0])) != None:
			return ret
		return in_order(left[1:], right[1:])
	elif isinstance(left[0], list) and isinstance(right[0], int): # list int
		if (ret := in_order(left[0], [right[0]])) != None:
			return ret
		return in_order(left[0][1:], list())
	elif isinstance(left[0], int) and isinstance(right[0], list): # int list
		if (ret := in_order([left[0]], right[0])) != None:
			return ret
		return in_order(list(), right[0][1:])
	return True # should never get here anyways

def compare(left, right):
	if in_order(left, right):
		return -1
	else:
		return 1

inputs = []
sum = 0
ind = 0
with open("input", "r") as file:
	for line in iter(file.readline, ''): # loop till end
		ind += 1
		first = json.loads(line.rstrip())
		second = json.loads(file.readline().rstrip())
		inputs.append(first)
		inputs.append(second)
		if res := in_order(first, second):
			sum += ind
		file.readline() # discard

# divider packets
inputs.append([[2]])
inputs.append([[6]])

inputs.sort(key=cmp_to_key(compare))

print((inputs.index([[2]])+1) * (inputs.index([[6]])+1))