from helper_functions import matrix_generator


def column_parser(col):
    templateString = "abcdefghi"
    resultCol = templateString.index(col) if col in templateString else False
    return resultCol


def row_parser(row):
    if row < 1 or row > 9:
        return False
    else:
        return row - 1


def value_parser(value):
    if value < 1 or value > 9:
        return False
    else:
        return value


def config_parser(configFile, playFile=False):
    with open(configFile) as file:
        configMatrix = matrix_generator(9, 9)
        quantityOfHints = 0
        for line in file:
            quantityOfHints += 1
            line = "".join(line.split())
            (col, _, row, _, value) = (line)[:5]

            resultCol = column_parser(col.lower())
            resultRow = row_parser(int(row))
            resultValue = value_parser(int(value))

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

        print(configMatrix[0])

        return configMatrix, quantityOfHints


config_parser("teste.txt")
