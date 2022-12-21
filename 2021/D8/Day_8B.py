tot = 0
letters = 'abcdefg'
numbers = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
			'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
with open('D8_input.txt', 'r') as fopen:
	for line in fopen:
		mapping = {let: '' for let in letters}
		sigs, out = line.rstrip().split('|')
		sigs = sigs.split()
		out = out.split()
		len_dict = {str(val):[] for val in range(2,8)}
		len_not_dict = {str(val):[] for val in range(2,8)}
		for sig in sigs:
			len_dict[str(len(sig))].append(sig)
			for let in letters:
				if let not in sig:
					len_not_dict[str(len(sig))].append(let)
		len_red_not_dict = {key: set(len_not_dict[key]) for key in len_not_dict}

		for char in len_dict['3'][0]:
			if char not in len_dict['2'][0]:
				mapping['a'] = char

		for char in mapping:
			if char not in ''.join(len_not_dict['6'] + len_dict['4'] + list(mapping['a'])):
				mapping['g'] = char

		for char in len_dict['4'][0]:
			if char not in ''.join(len_not_dict['6'] + len_dict['2']):
				mapping['b'] = char
			
		for char in len_dict['4'][0]:
			if char not in ''.join(len_not_dict['6'] + list(mapping['b'])):
				mapping['f'] = char

		for char in len_not_dict['5']:
			if char not in ''.join(len_dict['2'] + list(mapping['b'] + mapping['f'])):
				mapping['e'] = char

		for char in len_not_dict['5']:
			if char not in ''.join(list(mapping['b'] + mapping['e'] + mapping['f'])):
				mapping['c'] = char

		for char in len_not_dict['6']:
			if char not in ''.join(list(mapping['c'] + mapping['e'])):
				mapping['d'] = char

		inv_mapping = {val: key for key, val in mapping.items()}

		out_val = ''
		for val in out:
			srt_val = sorted([inv_mapping[char] for char in val])
			out_val += numbers[''.join(srt_val)]
		
		tot += int(out_val)

print(tot)