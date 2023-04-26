import random

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
    return ((row // 3) * 3 + 1) + (col // 3)


class SudokuCell:
    def __init__(self, r, col, val=0):
        self.row = r
        self.column = col
        self.block = get_block_for_coordinates(r, col)
        self.value = val
        self.available_values = [1,2,3,4,5,6,7,8,9]

class SudokuBoard:
    def __init__(self):
        self.grid = [[0]*9 for x in range(9)]
        for row in range(9):
            for col in range(9):
                self.grid[row][col] = SudokuCell(row, col)
        

    def is_conflict_in_row(self, val, row):
        list_for_row = [cell.value for cell in self.grid[row]]
        if val in list_for_row:
            return True
        return False
    
    def is_conflict_in_column(self, val, col):
        list_for_col = [self.grid[row_num][col].value for row_num in range(9)]
        if val in list_for_col:
            return True
        return False
    
    def get_elements_for_sudoku_block(self, block_number):
        #
        # block 1
        #  grid[0][0:3] + grid[1][0:3] + grid[2][0:3]
        # block 2
        #  grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
        # block 4
        #  grid[3][0:3] + grid[4][0:3] + grid[5][0:3]
        # block 7
        #  grid[6][0:3] + grid[7][0:3] + grid[8][0:3]
        row_offset = ((block_number - 1) // 3) * 3
        col_offset = ((block_number - 1) %3) * 3
        row_of_cells = self.grid[row_offset][col_offset:col_offset + 3] + self.grid[row_offset + 1][col_offset:col_offset + 3] + self.grid[row_offset + 2][col_offset:col_offset + 3]
        return [cell.value for cell in row_of_cells]
  
    def is_conflict_in_subgrid(self, val, row, col):
      block_number = get_block_for_coordinates(row, col)
      list_for_subgrid = self.get_elements_for_sudoku_block(block_number)
      if val in list_for_subgrid:
          return True
      return False
  
    def conflict_exists(self, val, row, col):
        if self.is_conflict_in_row(val, row):
            return True
        if self.is_conflict_in_column(val, col):
            return True
        if self.is_conflict_in_subgrid(val, row, col):
            return True
        return False

    def assign_viable_value(self, row, col):
        proposed_value = 0
        cutoff_attempts = 20
        attempts = 0
        while self.conflict_exists(proposed_value, row, col) and attempts < cutoff_attempts:
            proposed_value = random.randrange(1,10)
            attempts += 1
        if attempts == 20:
            proposed_value = 0
        self.grid[row][col].value = proposed_value