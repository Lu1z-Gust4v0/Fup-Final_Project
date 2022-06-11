from helper_functions import grid_generator


def parse_column(column):
    TEMPLATE_STRING = "ABCDEFGHI"
    column = column.upper().strip()

    if column in TEMPLATE_STRING:
        return TEMPLATE_STRING.index(column)

    return False


def parse_row(row):
    row = int(row.strip())
    if row >= 1 or row <= 9:
        return row - 1

    return False


def parse_value(value):
    value = int(value.strip())
    if value >= 1 or value <= 9:
        return value

    return False


def parse_input(input):
    splited_line = input.split(":")

    column, row = (splited_line[0]).split(",")
    value = splited_line[1]

    # Debug
    # print(f"col: {column} row: {row} value: {value}")

    parsed_row = parse_row(row)
    parsed_column = parse_column(column)
    parsed_value = parse_value(value)

    # Debug
    # print(f"col: {parsed_column} row: {parsed_row} value: {parsed_value}")

    return parsed_row, parsed_column, parsed_value


def check_hor_ver(matrix, target_row, target_col, value):
    is_valid_move = True
    motive = []
    for i in range(9):
        # Check horizontally
        if i != target_col:
            if matrix[target_row][i] == value:
                is_valid_move = False
                motive = ["row", target_row, i]
                break
        # Check vertically
        if i != target_row:
            if matrix[i][target_col] == value:
                is_valid_move = False
                motive = ["col", i, target_col]
                break

    return is_valid_move, motive


def check_block(matrix, target_row, target_col, value):
    is_valid_move = True
    motive = []
    row_block = int(target_row / 3)
    col_block = int(target_col / 3)

    for i in range(row_block * 3, row_block * 3 + 3):
        for j in range(col_block * 3, col_block * 3 + 3):
            if matrix[i][j] == value:
                is_valid_move = False
                motive = ["block", i, j]
                break

    return is_valid_move, motive


def populate_grid(config_file, play_file=False):
    with open(config_file) as file:
        initial_grid = grid_generator(9, 9)
        hint_counter = 0
        for line in file:
            row, column, value = parse_input(line)

            initial_grid[row][column] = value
            hint_counter += 1

        return initial_grid, hint_counter
