import copy


def grid_generator(lines, columns, is_hint=True):
    grid_cell = {"value": " ", "is_hint": is_hint}
    return [[copy.deepcopy(grid_cell) for _ in range(columns)] for _ in range(lines)]
