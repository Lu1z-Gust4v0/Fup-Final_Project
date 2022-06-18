from .populate import populate_moves
from .checkers import check_grid_completed

def batch_mode(moves_file, initial_grid):
    final_grid = populate_moves(moves_file, initial_grid)

    if check_grid_completed(final_grid):
        print("A grade foi preenchida com sucesso!")
        
    else: 
        print("A grade nao foi preenchida!")