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

# Small test
# X_MAX: int = 5
# Y_MAX: int = 4

X_MAX: int = 25
Y_MAX: int = 20

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


def normalize(i: int):
    if i < 0: return -1
    if i > 0: return 1
    return 0


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


def move(rope: list, direction: tuple, distance: int) -> None:

    rope[0] = _move(rope[0], direction) 

    for i in range(0, len(rope) - 1):
        if not (abs(rope[i][X] - rope[i+1][X]) < 2 and abs(rope[i][Y] - rope[i+1][Y]) < 2):
            rope[i+1] = _move(rope[i+1], (normalize(rope[i][X] - rope[i+1][X]), normalize(rope[i][Y] - rope[i+1][Y])))


    # # Debug
    # screen: list = get_screen()
    # for i, knot in enumerate(rope):
    #     screen[knot[Y]][knot[X]] = i
    # print_screen(screen)

    HISTORY.append(rope)

    distance -= 1
    if distance > 0:
        move(rope.copy(), direction, distance)

# Small test
# HISTORY.append([(0,0) for _ in range(0,10)])

HISTORY.append([(11,5) for _ in range(0,10)])

for direction, distance in commands:
    move(HISTORY[-1].copy(), direction, distance)


tails: list = []
for position in HISTORY:
    tails.append(position[-1])

print(len(set(tails)))