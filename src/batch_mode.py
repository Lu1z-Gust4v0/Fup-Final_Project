from .populate import populate_moves
from .checkers import check_grid_completed
from .display import change_color


def batch_mode(moves_file, initial_grid):
    final_grid = populate_moves(moves_file, initial_grid)

    if check_grid_completed(final_grid):
        print(change_color("A grade foi preenchida com sucesso!", "green"))

    else:
        print(change_color("A grade nao foi preenchida!", "red"))
