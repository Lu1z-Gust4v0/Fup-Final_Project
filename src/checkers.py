# Check if the the move is horizontally and vertically allowed
# If not, returns False and a motive
def check_hor_ver(matrix, target_row, target_col, value):
    for i in range(9):
        # Check horizontally
        # TODO: deixar algo tipo matrix[i][j]["value"] == value
        if matrix[target_row][i] == value:
            return False, ["bad row move", target_row, i, value]

        # Check vertically
        if matrix[i][target_col] == value:
            return False, ["bad column move", i, target_col, value]

    return True, []


# Check if the the move on the block is allowed
# If not, returns False and a motive
def check_block(matrix, target_row, target_col, value):
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
            if matrix[i][j] == value:
                return False, ["bad block move", i, j, value]

    return True, []


# We check all moves possible and if the we have a repeted instruction
def check_all_moves(matrix, target_row, target_col, value):
    is_valid_hor_ver, mot_hor = check_hor_ver(matrix, target_row, target_col, value)
    is_valid_block, mot_block = check_block(matrix, target_row, target_col, value)

    # Here we check if there is a repeted instruction and we overwrite it
    # If we didn't have this, our check_moves will return False, because they
    # Found a value on the existing matrix with the same value we want to insert
    # In that way we didn't need to do a lot of if statements in our check fn
    if matrix[target_row][target_col] == value:
        return True, []
    if is_valid_hor_ver is False:
        return False, mot_hor
    elif is_valid_block is False:
        return False, mot_block
    # TODO: check for matrix[target_row][target_col]["is_hint"] == True

    return True, []


# Check if our input is explicitly False and return False if it is
# Because of the parsed_input can return 0 as an index, this is needed
def check_input(row, column, value):
    if row is False:
        return False, ["bad row hint", row, column, value]
    elif column is False:
        return False, ["bad column hint", row, column, value]
    elif value is False:
        return False, ["bad value hint", row, column, value]

    return True, []


# Check if the grid is fully used, if not returns False
def check_grid_completed(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]["value"] == " ":
                return False

    return True