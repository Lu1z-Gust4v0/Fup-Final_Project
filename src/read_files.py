from .args_parser import parse_input, raw_input
from .checkers import check_all_moves, check_input
from .helper_functions import grid_generator


def generate_plays(play_file, initial_grid):
    played_grid = initial_grid
    with open(play_file) as file:
        for line in file:

            # TODO: Fix generate_play functions, since it broke due to the changes 
            # in `parse_input` function
            row, column, value = parse_input(line)
            raw_row, raw_column, raw_value = raw_input(line)

            is_valid_hint, _ = check_input(row, column, value)
            is_valid_move, _ = check_all_moves(played_grid, row, column, value)
            # TODO: Perguntar ao miguel se mesmo uma jogada inválida no modo batch
            # Se ela deve entrar no grid mesmo assim
            if is_valid_hint and is_valid_move:
                played_grid[row][column] = value
            else:
                print(f"A jogada ({raw_column}{raw_row}) = {raw_value} eh invalida!")

    return played_grid


# Receives a PathBuf to config_file and return a grid filled with valid hints,
# a hint_counter and all invalid_hints
def populate_grid(config_file):
    with open(config_file) as file:
        # Initialize initial_grid, hint_counter and invalid_hints
        initial_grid = grid_generator(9, 9)
        hint_counter = 0

        # For each line in file parse the line
        for line in file:
            # Receive a line and pass it to parse_input that will return list of 
            # values already treaded. If the input is invalid 'parse_input' will return False.
            parsed_input = parse_input(line)

            # Check if the hint passed is in the adequate format.
            if not parsed_input or len(parsed_input) == 2: 
                return None, hint_counter, line
            
            row, column, value = parsed_input
            
            valid_move, motive = check_all_moves(initial_grid, row, column, value)

            # Check if the hint it is against the game rules.
            if not valid_move:
                return None, hint_counter, line

            initial_grid[row][column]["value"] = value  # pyright: ignore
            initial_grid[row][column]["is_hint"] = True

            hint_counter += 1

            
        return initial_grid, hint_counter, None
