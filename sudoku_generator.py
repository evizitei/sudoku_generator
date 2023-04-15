print("Sudoku Generator Starting Up!")

horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

import random

# changed to list comprehension that generates
# a list that contains nine lists of nine zeroes
sudoku_grid = [[0]*9 for x in range(9)]

def conflict_exists(grid, val, row, col):
    list_for_row = grid[row]
    if val in list_for_row:
        return True
    # changed to list comprehension that generates
    # a list containing all the numebrs at a specific
    # index for each of the nine rows
    list_for_col = [grid[row_num][col] for row_num in range(9)]
    if val in list_for_col:
        return True
    return False

def generate_viable_value(grid, row, col):
    proposed_value = 0
    cutoff_attempts = 20
    attempts = 0
    while conflict_exists(grid, proposed_value, row, col) and attempts < cutoff_attempts:
        proposed_value = random.randrange(1,10)
        attempts += 1
    if attempts == 20:
        proposed_value = 0
    grid[row][col] = proposed_value

def sudoku_row_as_text_string(row_as_integer_list):
    row_as_string_variable = ""
    for cell_value in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell_value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

for row in range(9):
    for col in range(9):
        generate_viable_value(sudoku_grid, row, col)

print(vertical_border_character * text_cells_in_ascii_grid)
for i in range(9):
    row_string = sudoku_row_as_text_string(sudoku_grid[i])
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")