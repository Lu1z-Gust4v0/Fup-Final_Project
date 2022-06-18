from .args_parser import parse_input, raw_input
from .checkers import check_all_moves, is_cell_hint, check_grid_completed
from .frontend import display_grid


def interactive_mode(game_grid):

    game_finished = False

    while not game_finished:

        display_grid(game_grid)

        user_input = input("Faca uma jogada: ")

        parsed_input = parse_input(user_input)

        if not parsed_input:
            print("Jogada invalida, tente novamente.")
            continue

        if len(parsed_input) == 3:

            row, column, value = parsed_input

            valid_move, _ = check_all_moves(game_grid, row, column, value)

            raw_row, raw_column, raw_value = raw_input(user_input)
            
            if not valid_move:
                print(f"Jogada ({raw_column},{raw_row}:{raw_value}) Invalida, tente novamente.")
                continue
            
            game_grid[row][column]["value"] = value

        elif len(parsed_input) == 2:

            row, column = parsed_input

            if is_cell_hint(game_grid, row, column):
                print("Voce nao pode deletar uma dica, tente novamente.")
                continue

            game_grid[row][column]["value"] = " "

        game_finished = check_grid_completed(game_grid)
    
    print("Parabens, voce venceu!")