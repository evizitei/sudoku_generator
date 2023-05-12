from lib.sudoku_board import SudokuBoard
import random

print("Sudoku Generator Starting Up!")

horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

board = SudokuBoard()

def generate_board_values(board):
    while board.not_solved() and board.not_stuck():
        easy_options = board.cells_with_one_option()
        if len(easy_options) > 0:
            cell = random.choice(easy_options)
            board.assign_value(cell, cell.available_values[0])
        else:
            cell = board.select_cell_with_fewest_options()
            board.assign_value(cell, random.choice(cell.available_values))

def sudoku_row_as_text_string(row_as_integer_list):
    row_as_string_variable = ""
    for cell in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell.print_value()) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

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