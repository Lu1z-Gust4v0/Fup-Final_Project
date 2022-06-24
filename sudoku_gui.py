import sys
from src.batch_mode import batch_mode
from src.populate import populate_grid
from src.gui_functions import pop_up, game_screen, game_screen_batch


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        message = f'''
        A quantidade de "{len(sys.argv) - 1}" argumentos não é esperada pelo Sudoku
        Por favor, insira ou apenas o arquivo de "cfg" ou o de "cfg" E o de "play"'''
        pop_up(message, 'IndianRed')
        exit()

    (grid, hint_counter, invalid_hint) = populate_grid(sys.argv[1])
 
    if invalid_hint:
        message = f'''
        Arquivo de dicas invalido.
        Dica invalida: {invalid_hint}'''
        pop_up(message, 'IndianRed')
        exit()

    if hint_counter < 1 or hint_counter > 80:
        message = f'''
        A quantidade minima de dicas é 1 e a máxima é 80.
        Você inseriu {hint_counter} dicas.'''
        pop_up(message,'IndianRed')
        exit()

    if len(sys.argv) == 2:
        game_screen(grid)

    if len(sys.argv) == 3:
        game_screen_batch(sys.argv[2], grid)
        

if __name__ == "__main__":
    main()
