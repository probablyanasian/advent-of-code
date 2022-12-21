# representation of a rock, conceptually upside down
class Rock():
	def __init__(self, r_type:int, max_h:int):
		self.coords = []
		spawn_height = max_h + 4
		if r_type % 5 == 1:
			self.coords = [[spawn_height, 2], [spawn_height, 3], [spawn_height, 4], [spawn_height, 5]]
		elif r_type % 5 == 2:
			self.coords = [[spawn_height, 3], [spawn_height+1, 2], [spawn_height+1, 3], [spawn_height+1, 4], [spawn_height+2, 3]]
		elif r_type % 5 == 3:
			self.coords = [[spawn_height, 2], [spawn_height, 3], [spawn_height, 4], [spawn_height+1, 4], [spawn_height+2, 4]]
		elif r_type % 5 == 4:
			self.coords = [[spawn_height, 2], [spawn_height+1, 2], [spawn_height+2, 2], [spawn_height+3, 2]]
		elif r_type % 5 == 0: # for mod 5ing
			self.coords = [[spawn_height, 2], [spawn_height, 3], [spawn_height+1, 2], [spawn_height+1, 3]]

	def check(self, positions:list[list[int]], board:list[list[str]]) -> bool:
		for pos in positions:
			if pos[1] < 0 or pos[1] > 6: # OOB
				return False
			if board[pos[0]][pos[1]] == '#': # Filled
				return False
		return True

	def move(self, dir_char:str, board:list[list[str]]):
		if dir_char == '>':
			if self.check(upd := [[coord[0], coord[1]+1] for coord in self.coords], board):
				self.coords = upd
		elif dir_char == '<':
			if self.check(upd := [[coord[0], coord[1]-1] for coord in self.coords], board):
				self.coords = upd
		elif dir_char == 'd': # down handler
			if self.check(upd := [[coord[0]-1, coord[1]] for coord in self.coords], board):
				self.coords = upd
			else:
				return True
		return False
	
with open("input", "r") as file:
	ins = list(file.readline().rstrip())

rock_ctr = 1
ins_ptr = 0
max_h = 0
period = 349
#7, 349
rock = Rock(rock_ctr, max_h)
board = [['#' for _ in range(7)]] # floor
board.extend([['.' for _ in range(7)] for _ in range(4)]) # prep board
important = []
up_to = []
while rock_ctr <= (10000*5):
	rock.move(ins[ins_ptr], board)
	if rock.move('d', board):
		for coord in rock.coords:
			board[coord[0]][coord[1]] = '#' # fill
		rock_ctr += 1
		if (temp := max(rock.coords, key=lambda x: x[0])[0]) > max_h:
			max_h = temp 
		rock = Rock(rock_ctr, max_h)
		board.extend([['.' for _ in range(7)] for _ in range((max_h+8) - len(board))])
		if ((rock_ctr % (5 * period)) == 1):
			important.append(max_h)
		if (rock_ctr > (5*period)) and rock_ctr <= (5*period*2):
			up_to.append(max_h-important[0])
	ins_ptr += 1
	ins_ptr %= len(ins)

diff = important[1] - important[0]
cycles = (1000000000000 // (5*period)) - 1
left = 1000000000000 % (5*period)
print(important[0] + (diff*cycles) + up_to[left])