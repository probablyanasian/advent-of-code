grid = []
with open('D9_input_test.txt', 'r') as fopen:
	for line in fopen:
		grid.append([1 if int(char) == 9 else 0 for char in line.rstrip()])

def get_zero_ind(grid):
	for row_ind, row in enumerate(grid):
		for col_ind, col_val in enumerate(row):
			if col_val == 0:
				return (row_ind, col_ind)

def recurse(posx, posy):
	

rel_dict = {}
inc = 1
basins = []
while sum(row.count(0) for row in grid):
	zero_row, zero_col = get_zero_ind(grid)
