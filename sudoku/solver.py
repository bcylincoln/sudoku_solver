import matplotlib.pyplot as plt
import networkx as nx
from board_constants import *
from itertools import combinations
from read_txt import get_puzzles

GAME_SIZE = 9

class Cell:
	def __init__(self, cell_id):
		game_size = 9
		self.cell_id = cell_id
		self.domain = set(range(1,GAME_SIZE+1))

class Game:
	def __init__(self):
		self.game_board = []		#flat list of all cells, row by row
		self.constraint_graph = nx.Graph()
	
	def populate_board(self):
		for i in range(GAME_SIZE ** 2):
			self.game_board.append(Cell(i))

		self.constraint_graph.add_nodes_from(range(81))

		for i in range(GAME_SIZE):
			edges = combinations(ROW_LIST[i], 2)
			self.constraint_graph.add_edges_from(edges)
			edges = combinations(COL_LIST[i], 2)
			self.constraint_graph.add_edges_from(edges)
			edges = combinations(BOX_LIST[i], 2)
			self.constraint_graph.add_edges_from(edges)

	def enforce_unary_constraints(self, constraints_dict):
		for cell_id, val in constraints_dict.items():
			self.game_board[cell_id].domain = set([val])
			for n in self.constraint_graph[cell_id]:
				self.game_board[n].domain.discard(val)

	def pprint(self):
		i = 0
		for _ in range(GAME_SIZE):
			row = ""
			for _ in range(GAME_SIZE):
				domain = self.game_board[i].domain
				if len(domain) == 1:
					elem = domain.pop()
					domain.add(elem)
					row += str(elem)
				else:
					row += "_"
				i += 1
			print(row)

	def select_unassigned_variable(self, assignment):
		for i in range(GAME_SIZE ** 2):
			if not assignment.get(i, False):
				return i

	def is_consistent(self, variable, value, assignment):
		neighbors = self.constraint_graph[variable]
		for n in neighbors:
			if value == assignment.get(n, 0):
				return False
		return True 

def backtracking_search(game):
	return recursive_backtracking({}, game)

def recursive_backtracking(assignment, game):
	if len(assignment) == GAME_SIZE ** 2:
		return assignment

	var = game.select_unassigned_variable(assignment)
	for value in game.game_board[var].domain:
		# if value is consistent with assignment given csp constraints:
		if game.is_consistent(var, value, assignment):
			assignment[var] = value
			result = recursive_backtracking(assignment, game)
			if result != -1:
				return result
			assignment.pop(var)
	return -1

def read_euler_puzzle(puzzle):
	i = 0
	d = {}
	for ch in puzzle:
		if ch != "0":
			d[i] = int(ch)
		i += 1
	return d

def print_assignment(assignment):
	if assignment == -1:
		print("Failure")
		return

	i = 0
	for _ in range(GAME_SIZE):
		row = ""
		for _ in range(GAME_SIZE):
			row += str(assignment[i])
			i += 1
		print(row)

# game = Game()
# game.populate_board()

# grid_49 = read_euler_puzzle(GRID_49)

# game.enforce_unary_constraints(grid_49)
# assignment = backtracking_search(game)
# print_assignment(assignment)

solution_counter = 0
for name, puzzle in get_puzzles():
	game = Game()
	game.populate_board()
	grid = read_euler_puzzle(puzzle)
	game.enforce_unary_constraints(grid)
	assignment = backtracking_search(game)

	euler_solution = int(str(assignment[0]) + str(assignment[1]) + str(assignment[2]))
	solution_counter += euler_solution

	print(name)
	print_assignment(assignment)

print(solution_counter)


