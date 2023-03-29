
print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
vertical_border_character = "-"

print(vertical_border_character * text_cells_in_ascii_grid)

# moved where it makes more sense
import random

def build_row_of_sudoku_cells():
    # got rid of duplicates by explicitly defining
    # the list items, instead of generating one integer at a time
    sudoku_row = []
    while len(sudoku_row) < 9:
        new_value = random.randrange(1,10)
        if new_value not in sudoku_row:
            sudoku_row.append(new_value)
    return sudoku_row

#make a row of 9 cells with cell walls.
def sudoku_row_as_text_string():
    row_as_string_variable = ""
    row_as_integer_list = build_row_of_sudoku_cells()
    for cell_value in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell_value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

#repeat the row 9 times
for i in range (horizontal_cell_count):
    row_string = sudoku_row_as_text_string()
    print(row_string)
    print(vertical_border_character * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")
