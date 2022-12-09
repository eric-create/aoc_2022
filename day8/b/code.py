

lines: list = open('input.txt').read().splitlines()

tree_map: list = []

for line in lines:
    tree_map.append([int(char) for char in line])



def get_dir(tree_map, x_start, y_start, x_slope, y_slope):
    x_len = len(tree_map[0])
    y_len = len(tree_map)

    scenic_factor: int = 0

    if x_slope == 0:
        if y_start == 0 or y_start == y_len - 1:
            return 0

        y_lim = -1 if y_slope < 0 else y_len
        for y in range(y_start + y_slope, y_lim, y_slope):
            scenic_factor += 1
            if tree_map[y][x_start] >= tree_map[y_start][x_start]:
                return scenic_factor
        return scenic_factor

    if y_slope == 0:
        if x_start == 0 or x_start == x_len - 1:
            return 0

        x_lim = -1 if x_slope < 0 else x_len
        for x in range(x_start + x_slope, x_lim, x_slope):
            scenic_factor += 1
            if tree_map[y_start][x] >= tree_map[y_start][x_start]:
                return scenic_factor
        return scenic_factor



x_len = len(tree_map[0])
y_len = len(tree_map)

spots: list = []

for y in range(0, y_len):
    for x in range(0, x_len):
        up      = get_dir(tree_map, x_start=x, y_start=y, x_slope=0, y_slope=-1)
        down    = get_dir(tree_map, x_start=x, y_start=y, x_slope=0, y_slope=1)
        right   = get_dir(tree_map, x_start=x, y_start=y, x_slope=1, y_slope=0)
        left     = get_dir(tree_map, x_start=x, y_start=y, x_slope=-1, y_slope=0)
        spots.append(up * left * right * down)

spots.sort()
print(spots[-1])