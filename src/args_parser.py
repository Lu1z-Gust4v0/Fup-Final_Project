import re


# Search for a valid column in TEMPLATE_STRING, if do not exist return False
def parse_column(column):
    TEMPLATE_STRING = "ABCDEFGHI"
    column = column.upper().strip()

    if column in TEMPLATE_STRING:
        return TEMPLATE_STRING.index(column)

    return False


# Search for a row in [1,9], if not found return False
def parse_row(row):
    row = int(row.strip())
    # Return row -1 for a better usage in grid variable that starts on index 0
    if row >= 1 and row <= 9:
        return row - 1

    return False


# Search for a value in [1,9], if not found return False
def parse_value(value):
    value = int(value.strip())
    if value >= 1 and value <= 9:
        return value

    return False


# Receive a line and transform that line, if valid, in a parsed_input
def parse_input(input):
    splited_line = input.split(":")

    column, row = (splited_line[0]).split(",")
    value = splited_line[1]

    parsed_row = parse_row(row)
    parsed_column = parse_column(column)
    parsed_value = parse_value(value)

    return parsed_row, parsed_column, parsed_value


def raw_input(input):
    no_whitespaces = re.compile(r"\s*")
    input_pattern = re.compile(r"(.*),(.*):(.*)", flags=re.IGNORECASE)

    new_input = no_whitespaces.sub(input, "")

    input_grouped = input_pattern.search(new_input)

    if input_grouped is None:
        return False, ['no "," or ";"'], False

    column, row, value = input_grouped.groups()  # pyright: ignore

    return row, column, value


# Search for a delete pattern, if not found return none
def search_for_delete_cmd(input):
    no_whitespaces = re.compile(r"\s*")
    input_pattern = re.compile(r"(d)([a-i]),([1-9])", flags=re.IGNORECASE)

    # Remove all whitespaces in the string
    new_input = no_whitespaces.sub(input, "")
    # Try to search for a valid delete pattern, I.E., D<COL>,<LIN>
    is_matched = input_pattern.search(new_input)

    # If not found, the regex return None
    if is_matched is not None:
        # We destructure the groups tuple in a string with "D", that is discarted
        # column and row value
        _, column, row = is_matched.groups()  # pyright: ignore
        return _, column, row

    return None
