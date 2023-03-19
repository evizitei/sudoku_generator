print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
import random
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)

print("-" * text_cells_in_ascii_grid)

#generate a random number 1-9
def random_number():
    cell = random.randint(1, 9)
    return cell

#make a row of 9 cells with cell walls    
def row():
    for i in range(horizontal_cell_count):
        print("| " + str(random_number()), end = " ")
    print("|")

#repeat the row 9 times
for i in range (horizontal_cell_count):
    row()
    print("-" * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")


