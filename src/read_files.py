from .args_parser import parse_input, raw_input
from .checkers import check_all_moves
from .helper_functions import grid_generator


def populate_moves(moves_file, initial_grid):
    game_grid = initial_grid

    with open(moves_file) as file:
        for line in file:
            
            parsed_input = parse_input(line)
            raw_output = raw_input(line)

            # raw_output is a falsy value when the format is invalid
            if not raw_output:
                print("Formato invalido de jogada.")
                continue

            raw_row, raw_column, raw_value = raw_output

            # parsed_input is a falsy value when, at least, one of the 
            # values provided by the user is invalid.  
            if not parsed_input:
                print(f"A jogada ({raw_column},{raw_row}) = {raw_value} eh invalida!")
                continue

            row, column, value = parsed_input
            valid_move = check_all_moves(game_grid, row, column, value)

            # Check if the move is against the game rules.
            if not valid_move:
                print(f"A jogada ({raw_column},{raw_row}) = {raw_value} eh invalida!")
                continue
            
            game_grid[row][column]["value"] = value
            
    return game_grid


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
            
            valid_move = check_all_moves(initial_grid, row, column, value)

            # Check if the hint it is against the game rules.
            if not valid_move:
                return None, hint_counter, line

            initial_grid[row][column]["value"] = value  # pyright: ignore
            initial_grid[row][column]["is_hint"] = True

            hint_counter += 1

            
        return initial_grid, hint_counter, None
