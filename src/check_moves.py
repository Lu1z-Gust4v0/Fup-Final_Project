def check_hor_ver(matrix, target_row, target_col, value, line):
    is_valid_move = True
    motive = []
    for i in range(9):
        # Check horizontally
        if i != target_col:
            if matrix[target_row][i] == value:
                is_valid_move = False
                motive = ["bad row move", target_row, i, value, line]
                break
        # Check vertically
        if i != target_row:
            if matrix[i][target_col] == value:
                is_valid_move = False
                motive = ["bad column move", i, target_col, value, line]
                break

    return is_valid_move, motive


def check_block(matrix, target_row, target_col, value, line):
    is_valid_move = True
    motive = []
    row_block = int(target_row / 3)
    col_block = int(target_col / 3)

    for i in range(row_block * 3, row_block * 3 + 3):
        for j in range(col_block * 3, col_block * 3 + 3):
            if matrix[i][j] == value:
                is_valid_move = False
                motive = ["bad block move", i, j, value, line]
                break

    return is_valid_move, motive


def check_all_moves(matrix, target_row, target_col, value, line):
    is_valid_move = True
    motive = []
    (is_good_hor_ver, mot_hor) = check_hor_ver(
        matrix, target_row, target_col, value, line
    )
    (is_good_block, mot_block) = check_block(
        matrix, target_row, target_col, value, line
    )
    if is_good_hor_ver is False:
        motive = mot_hor
        is_valid_move = False
    elif is_good_block is False:
        motive = mot_block
        is_valid_move = False

    return is_valid_move, motive


def check_hint(row, column, value, line):
    is_valid_hint = True
    motive = []

    if row is False:
        motive = ["bad row hint", row, column, value, line]
        is_valid_hint = False

    elif column is False:
        motive = ["bad column hint", row, column, value, line]
        is_valid_hint = False
    elif value is False:
        motive = ["bad value hint", row, column, value, line]
        is_valid_hint = False

    return is_valid_hint, motive
