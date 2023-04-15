print("Sudoku Generator Starting Up!")

horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

import random
import math

# changed to list comprehension that generates
# a list that contains nine lists of nine zeroes
sudoku_grid = [[0]*9 for x in range(9)]

def is_conflict_in_row(grid, val, row):
    list_for_row = grid[row]
    if val in list_for_row:
        return True
    return False

def is_conflict_in_column(grid, val, col):
    # changed to list comprehension that generates
    # a list containing all the numebrs at a specific
    # index for each of the nine rows
    list_for_col = [grid[row_num][col] for row_num in range(9)]
    if val in list_for_col:
        return True
    return False

def get_block_for_coordinates(row, col):
    # this should be a block number 1 through 9
    #
    # ORDER (each number is 3x3)
    #   1  2  3
    #   4  5  6
    #   7  8  9
    #
    #  row = 0, col = 0 => block = 1
    #  row = 1, col = 0 => block = 1
    #  row = 8, col = 8 => block = 9
    #  row = 4, col = 2 => block = 4
    return (math.floor(row / 3) * 3 + 1) + math.floor(col / 3)

def get_elements_for_sudoku_block(grid, block_number):
    #
    # block 1
    #  grid[0][0:3] + grid[1][0:3] + grid[2][0:3]
    # block 2
    #  grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
    # block 4
    #  grid[3][0:3] + grid[4][0:3] + grid[5][0:3]
    # block 7
    #  grid[6][0:3] + grid[7][0:3] + grid[8][0:3]
    row_offset = math.floor((block_number - 1) / 3) * 3
    col_offset = ((block_number % 3) - 1) * 3
    return grid[row_offset][col_offset:col_offset + 3] + grid[row_offset + 1][col_offset:col_offset + 3] + grid[row_offset + 2][col_offset:col_offset + 3]

def is_conflict_in_subgrid(grid, val, row, col):
    # THIS IS WHERE THER WORK WILL
    block_number = get_block_for_coordinates(row, col)
    list_for_subgrid = get_elements_for_sudoku_block(grid, block_number)
    if val in list_for_subgrid:
        return True
    return False

def conflict_exists(grid, val, row, col):
    # conflict could exist in a ROW, or a COL, or a BLOCK (3x3)
    # sub-grid.  Need to check all 3.
    if is_conflict_in_row(grid, val, row):
        return True
    if is_conflict_in_column(grid, val, col):
        return True
    if is_conflict_in_subgrid(grid, val, row, col):
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