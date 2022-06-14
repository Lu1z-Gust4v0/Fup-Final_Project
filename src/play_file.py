from .args_parser import parse_input, raw_input
from .check_moves import check_all_moves, check_hint


def generate_plays(play_file, initial_grid):
    played_grid = initial_grid
    with open(play_file) as file:
        for line in file:
            row, column, value = parse_input(line)
            raw_row, raw_column, raw_value = raw_input(line)

            is_valid_hint, _ = check_hint(row, column, value, line)
            is_valid_move, _ = check_all_moves(played_grid, row, column, value, line)
            # TODO: Perguntar ao miguel se mesmo uma jogada inválida no modo batch
            # Se ela deve entrar no grid mesmo assim
            if is_valid_hint and is_valid_move:
                played_grid[row][column] = value
            else:
                print(f"A jogada ({raw_column}{raw_row}) = {raw_value} eh invalida!")

    return played_grid


def check_grid_completed(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]["value"] == " ":
                return False

    return True
