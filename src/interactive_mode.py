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

        if not parsed_input:
            print(f"{change_color(f'Jogada ({user_input}) invalida, tente novamente.', 'red')}\n")
            continue

        if len(parsed_input) == 3:

            row, column, value = parsed_input
            valid_move = check_all_moves(game_grid, row, column, value)
            
            if not valid_move:
                print(f"{change_color(f'Jogada ({user_input}) invalida, tente novamente.', 'red')}\n")
                continue
            
            game_grid[row][column]["value"] = value

        elif len(parsed_input) == 2:

            row, column = parsed_input

            if is_cell_hint(game_grid, row, column):
                print(f"{change_color('Voce nao pode deletar uma dica, tente novamente.', 'red')}\n")
                continue

            game_grid[row][column]["value"] = " "

        game_finished = check_grid_completed(game_grid)
    
    print(change_color("Parabens, voce venceu!", "green"))