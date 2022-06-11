import sys
from args_parser import populate_grid
from helper_functions import display_grid


def main():
    if len(sys.argv) > 3:
        print(
            f""" 
A quantidade de "{len(sys.argv) -1}" argumentos é maior que a necessária
Por favor, insira ou apenas o arquivo de "cfg" ou ele e o de "play"
            """
        )
        exit()

    (grid, hint_counter) = populate_grid(sys.argv[1])
    display_grid(grid)


if __name__ == "__main__":
    main()
