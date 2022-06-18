def is_cell_hint(grid, row, column):
    return grid[row][column]["is_hint"]


# Check if the the move is horizontally and vertically allowed
# If not, returns False.
def check_hor_ver(grid, target_row, target_col, value):
    for i in range(9):
        # Check horizontally
        if grid[target_row][i]["value"] == value:
            return False

        # Check vertically
        if grid[i][target_col]["value"] == value:
            return False

    return True


# Check if the the move on the block is allowed
# If not, returns False.
def check_block(grid, target_row, target_col, value):
    # Because of previous treated input, the input range is on [0,8]
    # When we get the int result of division by 3, we get a range in [0,2]
    row_block = int(target_row / 3)
    col_block = int(target_col / 3)

    # We start our iteration in row_block * 3 to row_block * 3 + 3
    # If we receive a target_row of index "0" we will be in a row range of [0,3)
    for i in range(row_block * 3, row_block * 3 + 3):
        # We start our iteration in col_block * 3 to col_block * 3 + 3
        # If we receive a target_col of index "8" we will be in a col range of [6,9)
        for j in range(col_block * 3, col_block * 3 + 3):
            if grid[i][j]["value"] == value:
                return False

    return True


# We check all moves possible and if the we have a repeted instruction
def check_all_moves(grid, target_row, target_col, value):
    valid_hor_ver = check_hor_ver(grid, target_row, target_col, value)
    valid_block = check_block(grid, target_row, target_col, value)

    # Here we check if there is a repeted instruction and we overwrite it
    # If we didn't have this, our check_moves will return False, because they
    # Found a value on the existing grid with the same value we want to insert
    # In that way we didn't need to do a lot of if statements in our check fn
    if (
        grid[target_row][target_col]["value"] == value and 
        not is_cell_hint(grid, target_row, target_col)
    ):
        return True

    if not valid_hor_ver:
        return False
    
    if not valid_block:
        return False

    # We only check if it is a hint here because of the initial population of grid
    # If some hint or user_input is repeated it will return True on the first if statement
    if is_cell_hint(grid, target_row, target_col):
        return False

    return True


# Check if the grid is fully used, if not returns False
def check_grid_completed(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]["value"] == " ":
                return False

    return True

