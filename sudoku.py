import sys
from src.read_files import populate_grid
from src.frontend import display_grid


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(
            f"""
A quantidade de "{len(sys.argv) -1}" argumentos não é esperada pelo Sudoku
Por favor, insira ou apenas o arquivo de "cfg" ou o de "cfg" E o de "play"
            """
        )
        exit()

    (grid, hint_counter, wrong_hints) = populate_grid(sys.argv[1])
    display_grid(grid)

    if hint_counter < 1 or hint_counter > 80:
        print(
            f"""
A quantidade de entradas {hint_counter} não está no intervalo [1,80]
Por favor, insira entradas válidas
                """
        )
        exit()

    if len(wrong_hints) > 0:
        print(
            """
Encontramos algumas entradas erradas no arquivo de configuração
Por favor, conserte as seguintes entradas:
                """
        )
        for hint in wrong_hints:
            print(f"Linha: {hint[4]}, Motivo: {hint[0]}")
        exit()


if __name__ == "__main__":
    main()
