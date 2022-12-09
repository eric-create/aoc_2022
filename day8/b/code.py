width: int = len(lines[0])
height: int = len(lines)

def get_bigger_tree(matrix: list, x_start, y_start, x_slope, y_slope):
    x_lim: int = len(lines[0])
    y_lim: int = len(lines)
    tree_string: list = []

    edge_value: int = int(matrix[y_start][x_start])

    for y in range(y_start + y_slope, len(matrix), y_slope):
        for x in range(x_start + x_slope, len(matrix[0]), x_slope):
            tree_string.append[int(matrix[y][x])]

    tree_string.sort()

    if tree_string[-1] > edge_value:
        return True

    return tree_string[-1]


print(get_bigger_tree(lines, 2, 0, 0, 1))