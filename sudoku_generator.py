print("Sudoku Generator Starting Up!")

# one for each character position, space margins around them,
# and border spots for pipes.
horizontal_cell_count = 9
text_cells_in_ascii_grid = (4 * horizontal_cell_count + 1)
print("-" * text_cells_in_ascii_grid)
for i in range(9):
  print("| 0 " * horizontal_cell_count + "|")
  print("-" * text_cells_in_ascii_grid)

print("Sudoku Generator Finished!")
