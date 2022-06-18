COLOR = {
    "gray": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"    
}

def change_color(text, color):
    return COLOR[color] + f"{text}" + COLOR["reset"]


# Generate a grid `lines` X `columns`, each grid_cell
# is a dictionary containing `value` and `is_hint`.
def grid_generator(lines, columns):
    return [
        [
            {"value": " ", "is_hint": False} for _ in range(columns)
        ] for _ in range(lines)
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
    

    print(f'||{count + 1}')


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