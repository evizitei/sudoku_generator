print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
import random
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)

print("-" * text_cells_in_ascii_grid)

# generate a random number 1-9
# the return value is a single integer
def random_number():
    cell = random.randint(1, 9)
    return cell


# In order to make sure there are no duplicates
# or other constraint violations within a sudoku row,
# it seems useful to first build the row as a list of integers
# that can be easily compared to one another, and then later
# turn that list of integers into a printed line of text.
#  This function just builds the integer list (and this
#  would be a great spot to work on keeping out duplicates)
def build_row_of_sudoku_cells():
    sudoku_row = []
    for i in range(horizontal_cell_count):
        sudoku_row.append(random_number())
    return sudoku_row

#make a row of 9 cells with cell walls.
# we now do this by building up a string variable and returning
# it so that all the "printing" happens in one place. The sole concern
# of this function is to take a list of integers, and format it into a string
# that can be presented to the user anywhere strings are useful.
def sudoku_row_as_text_string():
    row_as_integer_list = build_row_of_sudoku_cells()
    row_as_string_variable = "" # starts empty
    for cell_value in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell_value) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable

#repeat the row 9 times
for i in range (horizontal_cell_count):
    row_string = sudoku_row_as_text_string()
    print(row_string)
    print("-" * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")
