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
# a hint_counter and all wrong_hints
def populate_grid(config_file):
    with open(config_file) as file:
        # Initialize initial_grid, hint_counter and wrong_hints
        initial_grid = grid_generator(9, 9)
        hint_counter = 0
        wrong_hints = []

        # For each line in file parse the line
        for line in file:
            # Receive a line and pass it to parse_input that will return a row, column, and value
            # alredy treated for our usage
            parsed_input = parse_input(line)

            # TODO: Be able to print the specific error made by the user
            # Temporary code
            if not parsed_input: 
                print("Folha de dicas invalida")
                wrong_hints.append("erro")
                break
            
            row, column, value = parsed_input
            # # Checks if the hint input is valid and return a Boolean and a motive
            # is_valid_hint, hint_motive = check_input(row, column, value)
            # # Checks if the move is valid and return a Boolean and a motive
            # is_valid_move, move_motive = check_all_moves(
            #     initial_grid, row, column, value
            # )

            # Checks if both hint and move is valid, if both valid initial_grid receives that value
            # if is_valid_hint and is_valid_move:
            initial_grid[row][column]["value"] = value  # pyright: ignore
            initial_grid[row][column]["is_hint"] = True

            hint_counter += 1

            # Append to wrong_hints list the motive why isn't valid and which line it occurs
            # elif is_valid_hint is False:
            #     hint_motive.append(hint_counter)
            #     wrong_hints.append(hint_motive)
            # else:
            #     move_motive.append(hint_counter)
            #     wrong_hints.append(move_motive)

        return initial_grid, hint_counter, wrong_hints
