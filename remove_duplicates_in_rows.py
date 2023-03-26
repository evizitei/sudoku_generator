print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)

print("-" * text_cells_in_ascii_grid)

# moved where it makes more sense
import random

def build_row_of_sudoku_cells():
    # got rid of duplicates by explicitly defining
    # the list items, instead of generating one integer at a time
    sudoku_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(sudoku_row)
    return sudoku_row

def sudoku_row_as_text_string():
    row_as_string_variable = ""
    row_as_integer_list = build_row_of_sudoku_cells()
    for cell_value in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell_value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

for i in range (horizontal_cell_count):
    row_string = sudoku_row_as_text_string()
    print(row_string)
    print("-" * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")