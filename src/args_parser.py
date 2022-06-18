import re


# Search for a valid column in TEMPLATE_STRING, if do not exist return False
def parse_column(column):
    TEMPLATE_STRING = "ABCDEFGHI"
    column = column.upper().strip()

    if column in TEMPLATE_STRING:
        return TEMPLATE_STRING.index(column)

    return None


# Search for a row in [1,9], if not found return False
def parse_row(row):
    row = int(row.strip())
    # Return row -1 for a better usage in grid variable that starts on index 0
    if row >= 1 and row <= 9:
        return row - 1

    return None


# Search for a value in [1,9], if not found return False
def parse_value(value):
    value = int(value.strip())
    if value >= 1 and value <= 9:
        return value

    return None


def raw_input(input):
    no_whitespaces = re.compile(r"\s*")
    input_pattern = re.compile(r"(.*),(.*):(.*)", flags=re.IGNORECASE)

    new_input = no_whitespaces.sub(input, "")

    input_grouped = input_pattern.search(new_input)

    # If the input does not match it returns a None list
    if not input_grouped:
        return False
    # if input_grouped is None:
    #     return False, ['no "," or ";"'], False

    raw_column, raw_row, raw_value = input_grouped.groups()  # pyright: ignore
    
    return [raw_row, raw_column, raw_value]


# Search for a delete pattern, if not found return none
def search_for_delete_cmd(input):
    no_whitespaces = re.compile(r"\s*")
    input_pattern = re.compile(r"(d)([a-i]),([1-9])", flags=re.IGNORECASE)

    # Remove all whitespaces in the string
    new_input = no_whitespaces.sub(input, "")
    # Try to search for a valid delete pattern, I.E., D<COL>,<LIN>
    is_matched = input_pattern.search(new_input)

    # If not found, the regex return None
    if not is_matched:
        return False
        
    # We destructure the groups tuple in a string with "D", that is discarted
    # column and row value
    _, column, row = is_matched.groups()  # pyright: ignore
    return [column, row]


# This function receives an input and check if it is a valid input / command. 
def parse_input(input):

    raw_move_input = raw_input(input)
    raw_del_input = search_for_delete_cmd(input) 

    # Debug
    # print(raw_move_input)
    # print(raw_del_input)

    if raw_move_input:

        row, column, value = raw_move_input

        parsed_row = parse_row(row)
        parsed_column = parse_column(column)
        parsed_value = parse_value(value)

        # Debug
        # print(parsed_row)
        # print(parsed_column)
        # print(parsed_value)

        # Check each parsed value, if at least one of them is None, return False.
        if not all(not i == None for i in [parsed_row, parsed_column, parsed_value]):
            return False

        return [parsed_row, parsed_column, parsed_value]

    elif raw_del_input:

        column, row = raw_del_input

        parsed_row = parse_row(row)
        parsed_column = parse_column(column)

        # Check each parsed value, if at least one of them is None, return False.        
        if not all(not i == None for i in [parsed_row, parsed_column]):
            return False

        return [parsed_row, parsed_column]
    
    else: 
        return False
