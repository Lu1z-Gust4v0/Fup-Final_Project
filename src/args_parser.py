from helper_functions import grid_generator


def parse_column(column):
    TEMPLATE_STRING = "ABCDEFGHI"
    
    column = column.upper()

    if column in TEMPLATE_STRING: 
        return TEMPLATE_STRING.index(column)

    return False


def parse_row(row):
    row = int(row)
    if row >= 1 or row <= 9:
        return row
    
    return False


def parse_value(value):
    value = int(value)
    if value >= 1 or value <= 9:
        return value
    
    return False


def parse_input(input):
    splited_line = input.split(":")

    column, row = (splited_line[0]).split(",")
    value = splited_line[1]

    parsedRow = parse_row(row) 
    parsedColumn = parse_column(column) 
    parsedValue = parse_value(value) 

    return parsedRow, parsedColumn, parsedValue


def check_hor_ver(matrix, targetRow, targetCol, value):
    isValidMove = True
    motive = []
    for i in range(9):
        # Check horizontally
        if i != targetCol:
            if matrix[targetRow][i] == value:
                isValidMove = False
                motive = ["row", targetRow, i]
                break
        # Check vertically
        if i != targetRow:
            if matrix[i][targetCol] == value:
                isValidMove = False
                motive = ["col", i, targetCol]
                break

    return isValidMove, motive


def check_block(matrix, targetRow, targetCol, value):
    isValidMove = True
    motive = []
    rowBlock = int(targetRow / 3)
    colBlock = int(targetCol / 3)

    for i in range(rowBlock * 3, rowBlock * 3 + 3):
        for j in range(colBlock * 3, colBlock * 3 + 3):
            if matrix[i][j] == value:
                isValidMove = False
                motive = ["block", i, j]
                break

    return isValidMove, motive


def populate_grid(configFile, playFile=False):
    with open(configFile) as file:
        configMatrix = grid_generator(9, 9)
        hintCounter = 0
        for line in file:
            row, column, value = parse_input(line)
                        
            configMatrix[row][column] = value
            hintCounter += 1

        return configMatrix, hintCounter


populate_grid("teste.txt")
