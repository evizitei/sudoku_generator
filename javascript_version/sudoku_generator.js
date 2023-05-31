console.log("Sudoku Generator Starting Up!")

const horizontal_cell_count = 9
const text_cells_in_ascii_grid = (4 * horizontal_cell_count +1)
const vertical_border_character = "-"

function verticalBorderString(){
    let bStr = ""
    for(let i = 0; i < text_cells_in_ascii_grid; i++){
        bStr = bStr + vertical_border_character
    }
    return bStr
}

function get_block_for_coordinates(row, col){
    /*
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
    */
    return (Math.floor(row / 3) * 3 + 1) + Math.floor(col / 3)
}

function sudoku_row_as_text_string(row_as_integer_list){
    let row_as_string_variable = ""
    for(let cell of row_as_integer_list){
        row_as_string_variable = row_as_string_variable + "| " + cell.print_value() + " "
    }
    row_as_string_variable = row_as_string_variable + "|"
    return row_as_string_variable
}


function sampleArray(array, k) {
    // Clone the original array to avoid modifying it
    const newArray = array.slice();
  
    // Shuffle the array using Fisher-Yates algorithm
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
  
    // Return the first K elements of the shuffled array
    return newArray.slice(0, k);
  }

class SudokuCell {
    constructor(r, col){
        this.row = r
        this.column = col
        this.block = get_block_for_coordinates(r, col)
        this.value = 0
        this.available_values = [1,2,3,4,5,6,7,8,9]
        this.print_empty = false
    }

    print_value(){
        if(this.print_empty){
            return " "
        }
        return this.value.toString()
    }
}
class SudokuBoard {
    constructor() {
        this.grid = []
        for(let i = 0; i < 9; i++){
            let newRow = []
            for(let j = 0; j < 9; j++){
                newRow.push(new SudokuCell(i, j))
            }
            this.grid.push(newRow)
        }
    }

    not_stuck() {
        for(let row of this.grid){
            for(let cell of row){
                if(cell.value === 0 && cell.available_values.length === 0){
                    return false
                }
            }
        }
        return true
    }

    choose_empty_cells(){
        let all_cells = []
        const number_of_puzzle_cells = 36
        for(let row of this.grid){
            for(let cell of row){
                all_cells.push(cell)
            }
        }
        let empty_cells = sampleArray(all_cells, number_of_puzzle_cells)
        for(let eCell of empty_cells){
            eCell.print_empty = true
        }
    } 
};

function generate_board_values(board){
    
}

let board = new SudokuBoard()

generate_board_values(board)


while(!board.not_stuck()){
    const cut_off_attempts = 100
    let attempts = 0
    board = new SudokuBoard()
    generate_board_values(board)
    attempts +=1
    if(attempts === 100){
        console.log("Bummer! Stuck before we could fully solve")
    }
}

board.choose_empty_cells()

console.log(verticalBorderString())
for(let i = 0; i < 9; i++){
    row_string = sudoku_row_as_text_string(board.grid[i])
    console.log(row_string)
    console.log(verticalBorderString())
}

console.log("Sudoku Generator Finished!")