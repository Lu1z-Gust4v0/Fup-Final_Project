from .helper_functions import grid_generator
from .check_moves import check_all_moves, check_block, check_hint, check_hor_ver


def parse_column(column):
    TEMPLATE_STRING = "ABCDEFGHI"
    column = column.upper().strip()

    if column in TEMPLATE_STRING:
        return TEMPLATE_STRING.index(column)

    return False


def parse_row(row):
    row = int(row.strip())
    if row >= 1 and row <= 9:
        return row - 1

    return False


def parse_value(value):
    value = int(value.strip())
    if value >= 1 and value <= 9:
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


def populate_grid(config_file, play_file=False):
    with open(config_file) as file:
        initial_grid = grid_generator(9, 9)
        hint_counter = 0
        wrong_hints = []

        for line in file:
            row, column, value = parse_input(line)
            # Não mude isso daqui lg é para saber se as entradas tao erradas por causa
            # das condicoes do sudoku
            is_good_input, hint_motive = check_hint(row, column, value, line)
            is_good_move, move_motive = check_all_moves(
                initial_grid, row, column, value, line
            )

            if is_good_input and is_good_move:
                initial_grid[row][column] = value
            elif is_good_input is False:
                wrong_hints.append(hint_motive)
            else:
                wrong_hints.append(move_motive)

            hint_counter += 1

        return initial_grid, hint_counter, wrong_hints
