
input_file = "p096_sudoku.txt"

def get_puzzles():
	puzzles = []
	with open(input_file) as f:
		puzzle_count = 0
		while puzzle_count < 50:
			name = f.readline()
			print(name)
			puzzle = ""
			for _ in range(9):
				puzzle += f.readline()[:9]
			puzzles.append((name, puzzle))
			puzzle_count += 1
	return puzzles
