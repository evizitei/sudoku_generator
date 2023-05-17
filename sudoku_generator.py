from lib.sudoku_board import SudokuBoard
from lib.sudoku_utils import generate_board_values, sudoku_row_as_text_string


print("Sudoku Generator Starting Up!")

horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

board = SudokuBoard()

generate_board_values(board)

# loop to regen the board up to 100 times when it gets stuck
while not board.not_stuck():
    cut_off_attempts = 100
    attempts = 0
    board = SudokuBoard()
    generate_board_values(board)
    attempts +=1
    if attempts == 100:
        print("Bummer! Stuck before we could fully solve")

board.choose_empty_cells()

print(vertical_border_character * text_cells_in_ascii_grid)
for i in range(9):
    row_string = sudoku_row_as_text_string(board.grid[i])
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)


print("Sudoku Generator Finished!")