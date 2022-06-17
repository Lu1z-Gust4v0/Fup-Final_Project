# Generate a grid `lines` X `columns`, each grid_cell
# is a dictionary containing `value` and `is_hint`.
def grid_generator(lines, columns):
    return [
        [
            {"value": " ", "is_hint": False} for _ in range(columns)
        ] for _ in range(lines)
    ]