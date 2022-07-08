COLOR = {
    "gray": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m",
}


def change_color(text, color):
    return COLOR[color] + f"{text}" + COLOR["reset"]


# Generate a grid `lines` X `columns`, each grid_cell
# is a dictionary containing `value` and `is_hint`.
def grid_generator(lines, columns):
    return [
        [{"value": " ", "is_hint": False} for _ in range(columns)] for _ in range(lines)
    ]


# Prints a line that follows the pattern passed as argument.
def print_line(line_pattern):

    for i in range(9):
        if i == 0:
            print(" ", end="")

        if i % 3 == 0:
            print("+", end="")

        print(f"+{line_pattern}", end="")

    print("++")


# Prints the grid's columns and puts each
# cell's value in the correct order.

# count determines the line's number (from 1 to 9).
def print_columns(list, count):
    for i in range(9):
        if i == 0:
            print(f"{count + 1}", end="")

        if i % 3 == 0:
            print("|", end="")

        if list[i]["is_hint"]:
            print(f'| {change_color(list[i]["value"], "blue")} ', end="")
        else:
            print(f'| {change_color(list[i]["value"], "green")} ', end="")

    print(f"||{count + 1}")


# Prints the grid's X cordinates (from A to I).
def print_coordinates():
    for i in range(9):
        if i == 0:
            print(" ", end="")

        if i % 3 == 0:
            print(" ", end="")

        print(f"  {chr(65 + i)} ", end="")

    print("")


# Prints the grid that is passed as argument.
def display_grid(grid):

    print_coordinates()

    for i in range(9):
        if i == 3 or i == 6:
            print_line("===")
        else:
            print_line("---")

        print_columns(grid[i], i)

    print_line("---")

    print_coordinates()
    print()


def matriz(lins, cols, val_inic):
    m = [[val_inic] * cols for _ in range(lins)]
    return m

# Display grid for GUI version
def get_grid(grid):
    m = matriz(9, 9,'   ')
    for i in range(9):
        for j in range(9):
            m[i][j] = grid[i][j]['value']
    return f'''
    A   B   C    D   E   F    G   H   I 
 ++---+---+---++---+---+---++---+---+---++
1|| {m[0][0]} | {m[0][1]} | {m[0][2]} || {m[0][3]} | {m[0][4]} | {m[0][5]} || {m[0][6]} | {m[0][7]} | {m[0][8]} ||1
 ++---+---+---++---+---+---++---+---+---++
2|| {m[1][0]} | {m[1][1]} | {m[1][2]} || {m[1][3]} | {m[1][4]} | {m[1][5]} || {m[1][6]} | {m[1][7]} | {m[1][8]} ||2
 ++---+---+---++---+---+---++---+---+---++
3|| {m[2][0]} | {m[2][1]} | {m[2][2]} || {m[2][3]} | {m[2][4]} | {m[2][5]} || {m[2][6]} | {m[2][7]} | {m[2][8]} ||3
 ++===+===+===++===+===+===++===+===+===++
4|| {m[3][0]} | {m[3][1]} | {m[3][2]} || {m[3][3]} | {m[3][4]} | {m[3][5]} || {m[3][6]} | {m[3][7]} | {m[3][8]} ||4
 ++---+---+---++---+---+---++---+---+---++
5|| {m[4][0]} | {m[4][1]} | {m[4][2]} || {m[4][3]} | {m[4][4]} | {m[4][5]} || {m[4][6]} | {m[4][7]} | {m[4][8]} ||5
 ++---+---+---++---+---+---++---+---+---++
6|| {m[5][0]} | {m[5][1]} | {m[5][2]} || {m[5][3]} | {m[5][4]} | {m[5][5]} || {m[5][6]} | {m[5][7]} | {m[5][8]} ||6
 ++===+===+===++===+===+===++===+===+===++
7|| {m[6][0]} | {m[6][1]} | {m[6][2]} || {m[6][3]} | {m[6][4]} | {m[6][5]} || {m[6][6]} | {m[6][7]} | {m[6][8]} ||7
 ++---+---+---++---+---+---++---+---+---++
8|| {m[7][0]} | {m[7][1]} | {m[7][2]} || {m[7][3]} | {m[7][4]} | {m[7][5]} || {m[7][6]} | {m[7][7]} | {m[7][8]} ||8
 ++---+---+---++---+---+---++---+---+---++
9|| {m[8][0]} | {m[8][1]} | {m[8][2]} || {m[8][3]} | {m[8][4]} | {m[8][5]} || {m[8][6]} | {m[8][7]} | {m[8][8]} ||9
 ++---+---+---++---+---+---++---+---+---++
    A   B   C    D   E   F    G   H   I 
'''
