from helper_functions import matrix_generator


def column_parser(col):
    col = col.lower()
    templateString = "abcdefghi"
    resultCol = templateString.index(col) if col in templateString else False
    return resultCol


def row_parser(row):
    row = int(row)
    if row < 1 or row > 9:
        return False
    else:
        return row - 1


def value_parser(value):
    value = int(value)
    if value < 1 or value > 9:
        return False
    else:
        return value


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


def config_parser(configFile, playFile=False):
    with open(configFile) as file:
        configMatrix = matrix_generator(9, 9)
        quantityOfHints = 0

        for line in file:
            quantityOfHints += 1
            line = "".join(line.split())
            (col, _, row, _, value) = (line)[:5]

            resultCol = column_parser(col)
            resultRow = row_parser(row)
            resultValue = value_parser(value)

            if resultRow is False:
                print(f"False o {resultRow}")
                exit()
            if resultCol is False:
                print(f"False o {resultCol}")
                exit()
            if resultValue is False:
                print(f"False o {resultValue}")
                exit()

            configMatrix[resultRow][resultCol] = resultValue

        return configMatrix, quantityOfHints


config_parser("teste.txt")
