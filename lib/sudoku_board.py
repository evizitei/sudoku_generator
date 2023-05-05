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
    
    def assign(self, new_value):
        self.value = new_value
        self.available_values = []
    
    def constrain(self, canceled_value):
        if canceled_value in self.available_values:
            self.available_values.remove(canceled_value)

class SudokuBoard:
    def __init__(self):
        self.grid = [[0]*9 for x in range(9)]
        for row in range(9):
            for col in range(9):
                self.grid[row][col] = SudokuCell(row, col)
    
    def not_solved(self):
        for row in self.grid:
            for cell in row:
                if cell.value == 0:
                    return True
        return False
    
    def not_stuck(self):
        for row in self.grid:
            for cell in row:
                if cell.value == 0 and len(cell.available_values) == 0:
                    return False
        return True


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
    
    def get_cells_for_sudoku_block(self, block_number):
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
        list_of_cells = self.grid[row_offset][col_offset:col_offset + 3] + self.grid[row_offset + 1][col_offset:col_offset + 3] + self.grid[row_offset + 2][col_offset:col_offset + 3]
        return list_of_cells
    
    def get_elements_for_sudoku_block(self, block_number):
        cells = self.get_cells_for_sudoku_block(block_number)
        return [c.value for c in cells]
  
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

    def propogate_constraints(self, row, col, new_value):
        # propogate row
        for i in range(9):
            cell = self.grid[row][i]
            cell.constrain(new_value)
        # propogate col
        for i in range(9):
            cell = self.grid[i][col]
            cell.constrain(new_value)
        # propogate block
        block_num = get_block_for_coordinates(row, col)
        block_cells = self.get_cells_for_sudoku_block(block_num)
        for cell in block_cells:
            cell.constrain(new_value)
        
    """
    def assign_viable_value(self, row, col):
        proposed_value = 0
        cutoff_attempts = 20
        attempts = 0
        while self.conflict_exists(proposed_value, row, col) and attempts < cutoff_attempts:
            proposed_value = random.randrange(1,10)
            attempts += 1
        if attempts == 20:
            proposed_value = 0
        # old version:
        # self.grid[row][col].value = proposed_value
        cell_in_question = self.grid[row][col]
        cell_in_question.assign(proposed_value)
        self.propogate_constraints(row, col, cell_in_question.value)
    """
    def assign_value(self, cell, value):
        cell.assign(value)
        self.propogate_constraints(cell.row, cell.column, cell.value)


      
    def cells_with_one_option(self):
        easy_options = []
        for row in self.grid:
            for cell in row:
                if(len(cell.available_values) == 1):
                    easy_options.append(cell)
        return easy_options
    
    def select_cell_with_fewest_options(self):
        lowest_non_zero_choice = 9
        for row in self.grid:
            for cell in row:
                choices = len(cell.available_values)
                if(choices > 0 and choices < lowest_non_zero_choice):
                    lowest_non_zero_choice = choices
        elgible_cells = []
        for row in self.grid:
            for cell in row:
                if(len(cell.available_values) == lowest_non_zero_choice):
                    elgible_cells.append(cell)
        return random.choice(elgible_cells)
