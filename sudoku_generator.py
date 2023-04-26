from lib.sudoku_board import SudokuBoard

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

for row in range(9):
    for col in range(9):
        board.assign_viable_value(row, col)

print(vertical_border_character * text_cells_in_ascii_grid)
for i in range(9):
    row_string = sudoku_row_as_text_string(board.grid[i])
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")