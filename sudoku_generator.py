from lib.sudoku_board import SudokuBoard
import random

print("Sudoku Generator Starting Up!")

horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

board = SudokuBoard()

def sudoku_row_as_text_string(row_as_integer_list):
    row_as_string_variable = ""
    for cell in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell.value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

while board.not_solved() and board.not_stuck():
    easy_options = board.cells_with_one_option()
    if len(easy_options) > 0:
        cell = random.choice(easy_options)
        board.assign_value(cell, cell.available_values[0])
    else:
        # TODO: Right now this does no backtracking,
        # but it will for sure get lodged at some point in most solves.
        cell = board.select_cell_with_fewest_options()
        board.assign_value(cell, random.choice(cell.available_values))

if not board.not_stuck():
    print("Bummer! Stuck before we could fully solve")
    # TODO: Option: instead of backgtracking, we could put in a loop here that 
    # regenerates the board from scratch up to 100 times to try to get a non-stuck version.


# TODO: This is the place we would start deciding WHICH CELLS NOT TO PRINT
# in order to actually make this a puzzle that humans could solve.
# Maybe start by just picking 18 cells at random and choosing not to print their value?
# Might require re-working how the printing below works
print(vertical_border_character * text_cells_in_ascii_grid)
for i in range(9):
    row_string = sudoku_row_as_text_string(board.grid[i])
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)


print("Sudoku Generator Finished!")