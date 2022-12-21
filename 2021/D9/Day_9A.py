grid = []
with open('D9_input.txt', 'r') as fopen:
	for line in fopen:
		grid.append([int(char) for char in line.rstrip()])

tot = 0
for row_ind, row in enumerate(grid):
	for col_ind, col_val in enumerate(row):
		low = True
		if row_ind == 0:
			if col_val >= grid[row_ind+1][col_ind]:
				low = False
		elif row_ind == len(grid)-1:
			if col_val >= grid[row_ind-1][col_ind]:
				low = False
		elif col_val >= grid[row_ind+1][col_ind] or col_val >= grid[row_ind-1][col_ind]:
				low = False
		
		if col_ind == 0:
			if col_val >= grid[row_ind][col_ind+1]:
				low = False
		elif col_ind == len(grid[0])-1:
			if col_val >= grid[row_ind][col_ind-1]:
				low = False
		elif col_val >= grid[row_ind][col_ind+1] or col_val >= grid[row_ind][col_ind-1]:
				low = False
		
		if low:
			tot += (col_val + 1)

print(tot)
