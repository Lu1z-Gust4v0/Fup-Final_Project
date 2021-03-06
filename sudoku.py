import sys
from src.batch_mode import batch_mode
from src.populate import populate_grid
from src.interactive_mode import interactive_mode
from src.display import change_color


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print(
            change_color(
                f"""
A quantidade de "{len(sys.argv) - 1}" argumentos não é esperada pelo Sudoku
Por favor, insira ou apenas o arquivo de "cfg" ou o de "cfg" E o de "play"
            """,
                "red",
            )
        )
        exit()

    (grid, hint_counter, invalid_hint) = populate_grid(sys.argv[1])

    if invalid_hint:
        print(
            change_color(
                f"""
Arquivo de dicas invalido.
Dica invalida: {invalid_hint}
            """,
                "red",
            )
        )
        exit()

    if hint_counter < 1 or hint_counter > 80:
        print(
            change_color(
                f"""
A quantidade minima de dicas é 1 e a máxima é 80.
Você inseriu {hint_counter} dicas.
            """,
                "red",
            )
        )
        exit()

    if len(sys.argv) == 2:
        interactive_mode(grid)

    if len(sys.argv) == 3:
        batch_mode(sys.argv[2], grid)


if __name__ == "__main__":
    main()
