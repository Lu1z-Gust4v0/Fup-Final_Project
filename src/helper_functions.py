def grid_generator(lines, columns):
    return [[" "] * columns for _ in range(lines)]
    

# Prints a line that follows the pattern passed as argument.
def print_line(line_pattern):

    for i in range(9):
        if i == 0:
            print(" ", end="")

        if i % 3 == 0:
            print(f"+", end="")

        print(f"+{line_pattern}", end="")

    print(f"++")


# Prints the grid's columns and puts each
# cell's value in the correct order.

# count determines the line's number (from 1 to 9).
def print_columns(list, count):
    for i in range(9):
        if i == 0:
            print(f"{count + 1}", end="")

        if i % 3 == 0:
            print("|", end="")

        print(f"| {list[i]} ", end="")

    print(f"||{count + 1}")


# Prints the grid's X cordinates (from A to I).
def print_coordinates():
    for i in range(9):
        if i == 0:
            print(" ", end="")

        if i % 3 == 0:
            print(f" ", end="")

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
