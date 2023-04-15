
print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

# moved where it makes more sense
import random

# create a variable in memory called "sudoku_grid", which is
# right now just a list with 81 zeros (one for each cell).
sudoku_list = [0] * 9 * 9

# since grid is a list of 81 cells, 
def conflict_exists(grid, val, row, col):
    list_for_row = grid[(row*9):((row*9) + 9)]
    if val in list_for_row:
        return True
    #list_for_col = [grid[inner_row][col] for inner_row in range(9)]
    list_for_col = []
    for row_num in range(9):
        list_for_col.append(grid[row_num * 9 + col])
    if val in list_for_col:
        return True
    return False

# This function promises that when you invoke it and give it a pointer to a 
# nested list representing a sudoku board, and specify a cell to modify (with row/col)
# it will generate values to try until it finds one that fits and put that one in the 
# target cell.
#
# The mechanism is pretty brute force, it just guesses random values and sees if they have any conflicts in the sudoku
# board already until one fits (or until it's stuck).
# It accepts 3 arguments:
#.  - grid = a pointer to a nested list that represents a sudoku board.
#.           we would expect it to be a list of 9 rows, with row in the list
#.           being itself a list of 9 integers representing cells in that row.
#.           A zero in a given cell means nothing has been assigned to it yet.
#.  - row = a number between 0 and 8 specifying the row of the cell we're trying to choose a value for.
#.  - col = a number between 0 and 8 specifying the column of the cell we're trying to choose a value for
def generate_viable_value(grid, row, col):
    proposed_value = 0
    cutoff_attempts = 20
    attempts = 0
    while conflict_exists(grid, proposed_value, row, col) and attempts < cutoff_attempts:
        proposed_value = random.randrange(1,10)
        attempts += 1
    if attempts == 20:
        proposed_value = 0
    print("PUTTING AT ", row, " ", col, " -> ", proposed_value)
    grid[row * 9 + col] = proposed_value

def sudoku_row_as_text_string(row_as_integer_list):
    row_as_string_variable = ""
    for cell_value in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell_value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

for row in range(9):
    for col in range(9):
        generate_viable_value(sudoku_list, row, col)

print(vertical_border_character * text_cells_in_ascii_grid)
for i in range(9):
    row_string = sudoku_row_as_text_string(sudoku_list[i*9:i*9+9])
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")