grid = []
with open('D9_input_test.txt', 'r') as fopen:
	for line in fopen:
		grid.append([1 if int(char) == 9 else 0 for char in line.rstrip()])

def get_zero_ind(grid):
	for row_ind, row in enumerate(grid):
		for col_ind, col_val in enumerate(row):
			if col_val == 0:
				return (row_ind, col_ind)
	return IndexError()

rel_dict = {}
inc = 1
while sum(row.count(0) for row in grid):
	zero_row, zero_col = get_zero_ind(grid)
	basins = set()
	if zero_row == 0:
		if grid[zero_row+1][zero_col] not in [0, 1]:
			basins.add(grid[zero_row+1][zero_col])
	elif zero_row == len(grid)-1:
		if grid[zero_row-1][zero_col] not in [0, 1]:
			basins.add(grid[zero_row-1][zero_col])
	else:
		if grid[zero_row+1][zero_col] not in [0, 1]:
			basins.add(grid[zero_row+1][zero_col])
		if grid[zero_row-1][zero_col] not in [0, 1]:
			basins.add(grid[zero_row-1][zero_col])

	if zero_col == 0:
		if grid[zero_row][zero_col+1] not in [0, 1]:
			basins.add(grid[zero_row][zero_col+1])
	elif zero_col == len(grid[0])-1:
		if grid[zero_row][zero_col-1] not in [0, 1]:
			basins.add(grid[zero_row][zero_col-1])
	else:
		if grid[zero_row][zero_col+1] not in [0, 1]:
			basins.add(grid[zero_row][zero_col+1])
		if grid[zero_row][zero_col-1] not in [0, 1]:
			basins.add(grid[zero_row][zero_col-1])

	if len(basins) == 0:
		inc += 1
		grid[zero_row][zero_col] = inc
		rel_dict[str(inc)] = []
	elif len(basins) == 1:
		grid[zero_row][zero_col] = list(basins)[0]
	else:
		if str(min(basins)) in rel_dict:
			rel_dict[str(min(basins))] += [str(basin) for basin in basins if basin != min(basins)]
		else:
			rel_dict[str(min(basins))] = [str(basin) for basin in basins if basin != min(basins)]
		grid[zero_row][zero_col] = min(basins)

# delete duplicates
for key in rel_dict:
	rel_dict[key] = list(set(rel_dict[key]))

def crawl(start, crawled, rel_dict):
	if start not in rel_dict:
		return []
	crawled.append(start)
	for val in rel_dict[start]:
		if val in crawled:
			return []
		crawled.append(val)
		crawled += crawl(val, crawled, rel_dict)
	return crawled

consumed = set()
reduced_rel_dict = {}
for key in list(rel_dict):
	if key in consumed:
		continue
	crawl_vals = set(crawl(str(key), [], rel_dict))
	consumed.update(crawl_vals)
	reduced_rel_dict[key] = list(set([int(val) for val in crawl_vals]))

for key in list(rel_dict):
	if key in consumed:
		continue
	crawl_vals = set(crawl(str(key), [], rel_dict))
	consumed.update(crawl_vals)
	reduced_rel_dict[key] = list(set([int(val) for val in crawl_vals]))

basin_size = []
for basin in reduced_rel_dict:
	basin_size.append(sum(1 if val in reduced_rel_dict[basin] else 0 for row in grid for val in row))

top_three = sorted(basin_size, reverse=True)[:3]
print(top_three[0]*top_three[1]*top_three[2])

print(sorted(basin_size, reverse=True))


for line in grid:
	print(line)

print('==========================')
print(reduced_rel_dict)