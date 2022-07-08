from .parsers import parse_input
from .checkers import check_all_moves, is_cell_hint, check_grid_completed
from .display import display_grid, change_color


def interactive_mode(game_grid):

    game_finished = False

    while not game_finished:

        display_grid(game_grid)

        user_input = input(change_color("Faca uma jogada: ", "green"))
        print()

        parsed_input = parse_input(user_input)

        # check for invalid move format
        if not parsed_input:
            print(
                change_color(
                    f"Jogada ({user_input}) invalida, tente novamente.\n", "red"
                )
            )
            continue
        
        # Normal move
        if len(parsed_input) == 3:

            row, column, value = parsed_input
            valid_move, motive = check_all_moves(game_grid, row, column, value)

            if not valid_move:
                print(
                    change_color(
                        f"Jogada ({user_input}) invalida, tente novamente.", "red"
                    )
                )
                print(change_color(f"Motivo: {motive}\n", "yellow"))
                continue

            game_grid[row][column]["value"] = value

        # Delete move
        elif len(parsed_input) == 2:

            row, column = parsed_input

            # Check if the user is trying to delete a hint
            if is_cell_hint(game_grid, row, column):
                print(
                    change_color(
                        "Voce nao pode deletar uma dica, tente novamente.\n", "red"
                    )
                )
                continue

            game_grid[row][column]["value"] = " "

        # Check if all the cells are fullfiled  
        game_finished = check_grid_completed(game_grid)

    print(change_color("Parabens, voce venceu!", "green"))
