import random

def generate_board_values(board):
    while board.not_solved() and board.not_stuck():
        easy_options = board.cells_with_one_option()
        if len(easy_options) > 0:
            cell = random.choice(easy_options)
            board.assign_value(cell, cell.available_values[0])
        else:
            cell = board.select_cell_with_fewest_options()
            board.assign_value(cell, random.choice(cell.available_values))

def sudoku_row_as_text_string(row_as_integer_list):
    row_as_string_variable = ""
    for cell in row_as_integer_list:
        row_as_string_variable = row_as_string_variable + "| " + str(cell.print_value()) + " "
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable