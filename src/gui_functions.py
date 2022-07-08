import PySimpleGUI as sg
from .parsers import parse_input
from .populate import populate_moves
from .checkers import check_all_moves, is_cell_hint, check_grid_completed
from .display import get_grid


sg.theme('Dark')


# Pops up a message
def pop_up(message, color):
    layout = [
            [sg.Text(message, text_color=color)],
            [sg.Button('Ok', bind_return_key=True)]
    ]
    
    window = sg.Window('Mensagem do Sistema', layout)

    while True:
        event, values = window.read()
        
        if event == 'Ok' or event == sg.WIN_CLOSED:
            break
    
    window.close()


def game_screen(game_grid):
    
    layout = [
            [sg.Text(get_grid(game_grid), key='-GRID-', font='Courier')],
            [
                sg.Text('Faça uma jogada:', text_color='PaleGreen'),
                sg.InputText(do_not_clear=False),
                sg.Button('Ok', bind_return_key=True)
            ]
    ]

    window = sg.Window('Sudoku', layout)
    
    while True:
        
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        user_input = values[0]
        parsed_input = parse_input(user_input)

        if not parsed_input:
            pop_up(f"Jogada ({user_input}) invalida, tente novamente.", 'IndianRed')
            continue

        if len(parsed_input) == 3:

            row, column, value = parsed_input
            valid_move, motive = check_all_moves(game_grid, row, column, value)

            if not valid_move:
                pop_up(f"Jogada ({user_input}) invalida, tente novamente.\nMotivo: {motive}.", 'IndianRed')
                continue
    
            game_grid[row][column]["value"] = value
            
            window['-GRID-'].update(get_grid(game_grid))

        elif len(parsed_input) == 2:

            row, column = parsed_input

            if is_cell_hint(game_grid, row, column):
                pop_up("Voce nao pode deletar uma dica, tente novamente.", 'IndianRed')
                continue

            game_grid[row][column]["value"] = " "

        if check_grid_completed(game_grid):
            pop_up("Parabens, voce venceu!", 'PaleGreen')
    
    window.close()


def game_screen_batch(moves_file, initial_grid):
    final_grid = populate_moves(moves_file, initial_grid)

    if check_grid_completed(final_grid):
        pop_up('A grade foi preechida com sucesso!', 'PaleGreen')
    else:
        pop_up('A grade não foi preenchida!', 'IndianRed')
