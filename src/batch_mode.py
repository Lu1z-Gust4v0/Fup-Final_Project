from .populate import populate_moves
from .checkers import check_grid_completed
from .display import change_color


def batch_mode(moves_file, initial_grid):
    # Pass all the moves in the 'moves_file' to the grid, and throw error 
    # messages when an invalid move is found. 
    final_grid = populate_moves(moves_file, initial_grid)

    if check_grid_completed(final_grid):
        print(change_color("A grade foi preenchida com sucesso!", "green"))

    else:
        print(change_color("A grade nao foi preenchida!", "red"))
