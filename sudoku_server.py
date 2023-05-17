from flask import Flask
from lib.sudoku_board import SudokuBoard
from lib.sudoku_utils import generate_board_values, sudoku_row_as_text_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/alternate/path")
def different_content():
    return "<p>Hello, other stuff!</p>"

@app.route("/sudoku")
def sudoku_raw():
    horizontal_cell_count = 9
    text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
    vertical_border_character = "-"
    board = SudokuBoard()
    generate_board_values(board)
    while not board.not_stuck():
        cut_off_attempts = 100
        attempts = 0
        board = SudokuBoard()
        generate_board_values(board)
        attempts +=1
        if attempts == 100:
            print("Bummer! Stuck before we could fully solve")
    board.choose_empty_cells()
    board_output = vertical_border_character * text_cells_in_ascii_grid
    for i in range(9):
        row_string = sudoku_row_as_text_string(board.grid[i])
        board_output = board_output + "\n" + row_string + (vertical_border_character * text_cells_in_ascii_grid)
    return "<p>" + board_output + "</p>"