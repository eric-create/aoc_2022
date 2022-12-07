lines: str = open('./input.txt').read()

matches: list = [(line.split(' ')[0], line.split(' ')[1]) for line in lines.splitlines()]

def normalize(match: tuple):
    me = match[1]

    if me == 'X': me = 'A'
    if me == 'Y': me = 'B'
    if me == 'Z': me = 'C'

    return (match[0], me)


normalized_matches: list = [normalize(match) for match in matches]

scissors = [None, 'C', None]
paper = [scissors, 'B', None]
rock = [paper, 'A', scissors]

scissors[0] = rock
scissors[2] = paper
paper[2] = rock


def get_item(char):
    if char == 'A': return rock
    if char == 'B': return paper
    if char == 'C': return scissors


def get_win_points(match: tuple):
    op = get_item(match[0])
    me = get_item(match[1])

    if op is me: return 3
    if op is me[2]: return 6
    if op is me[0]: return 0


def get_choice_points(match: tuple):
    if match[1] == 'A': return 1
    if match[1] == 'B': return 2
    if match[1] == 'C': return 3


def get_points(match: tuple):
    return get_win_points(match) + get_choice_points(match)


points = 0
for match_points in [get_points(match) for match in normalized_matches]:
    points += match_points

print(points)