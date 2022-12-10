lines: list = open('input.txt').read().splitlines()

commands: list = []

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
X=0
Y=1

for line in lines:
    direction = line[0]
    distance: int = int(line[2:])

    if direction == 'U': direction = UP
    if direction == 'D': direction = DOWN
    if direction == 'L': direction = LEFT
    if direction == 'R': direction = RIGHT

    commands.append((direction, distance))

HISTORY: list = []
X_MAX: int = 0
Y_MAX: int = 0

def get_screen():
    screen: list = []
    for y in range(0, Y_MAX + 1):
        screen.append([])
        for _ in range(0, X_MAX + 1):
            screen[y].append('.')

    return screen


def print_screen(screen: list):
    for y in range(0, Y_MAX + 1):
        for x in range(0, X_MAX + 1):
            print(screen[Y_MAX - y][x], end='')
        print()
    print()


def _move(knot: tuple, direction: tuple) -> tuple:
    """
    """
    global X_MAX
    global Y_MAX

    new_x : int = knot[X] + direction[X]
    new_y: int = knot[Y] + direction[Y]

    if new_x > X_MAX: X_MAX = new_x
    if new_y > Y_MAX: Y_MAX = new_y

    return (new_x, new_y)


def move(tail: tuple, head: tuple, direction: tuple, distance: int) -> tuple:
    """
    :return: new position of the passed part of the rope
    """
    head = _move(head, direction)

    if direction in [LEFT, RIGHT]:
        if abs(head[X] - tail[X]) > 1:
            tail = _move(tail, direction)
            tail = _move(tail, (0, head[Y] - tail[Y]))

    if direction in [UP, DOWN]:
        if abs(head[Y] - tail[Y]) > 1:
            tail = _move(tail, direction)
            tail = _move(tail, (head[X] - tail[X], 0))

    # # Debug
    # screen: list = get_screen()
    # screen[head[Y]][head[X]] = 'H'
    # screen[tail[Y]][tail[X]] = 'T'
    # print_screen(screen)

    HISTORY.append((tail, head))
    distance -= 1
    if distance > 0:
        move(tail, head, direction, distance)


# screen: list = get_screen()

HISTORY.append(((0,0), (0,0)))

for direction, distance in commands:
    move(HISTORY[-1][0], HISTORY[-1][1], direction, distance)

print('Y_MAX', Y_MAX)
print('X_MAX', X_MAX)
print()

screen: list = get_screen()

# # WARNINIG this fails for the personalized input for whatever reason
# for tail_position, _ in HISTORY:
#     screen[tail_position[1]][tail_position[0]] = 'T'

_sum = 0

tails: list = []
for position in HISTORY:
    tails.append(position[0])

print_screen(screen)
print()
print(len(set(tails)))