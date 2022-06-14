def check_hor_ver(matrix, target_row, target_col, value, line):
    for i in range(9):
        # Not check for the value on same col
        if i != target_col:
            # Check horizontally
            if matrix[target_row][i] == value:
                return False, ["bad row move", target_row, i, value, line]
        # Not check for value on same row
        if i != target_row:

            # Check vertically
            if matrix[i][target_col] == value:
                return False, ["bad column move", i, target_col, value, line]

    return True, []


def check_block(matrix, target_row, target_col, value, line):
    row_block = int(target_row / 3)
    col_block = int(target_col / 3)

    for i in range(row_block * 3, row_block * 3 + 3):
        if i != target_row:
            for j in range(col_block * 3, col_block * 3 + 3):
                if j != target_col:
                    if matrix[i][j] == value:
                        return False, ["bad block move", i, j, value, line]

    return True, []


def check_all_moves(matrix, target_row, target_col, value, line):
    (is_good_hor_ver, mot_hor) = check_hor_ver(
        matrix, target_row, target_col, value, line
    )
    (is_good_block, mot_block) = check_block(
        matrix, target_row, target_col, value, line
    )
    if is_good_hor_ver is False:
        return False, mot_hor
    elif is_good_block is False:
        return False, mot_block

    return True, []


def check_hint(row, column, value, line):
    if row is False:
        return False, ["bad row hint", row, column, value, line]
    elif column is False:
        return False, ["bad column hint", row, column, value, line]
    elif value is False:
        return False, ["bad value hint", row, column, value, line]

    return True, []
