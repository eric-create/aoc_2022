lines = open('input.txt').read().splitlines()

groups: list = []

for i in range(0, len(lines)):
    if i % 3 == 0:
        groups.append([])

    groups[int(i/3)].append(lines[i])

badges: list = []

for group in groups:
    badges.append(list(set(group[0]) & set(group[1]) & set(group[2]))[0])


def get_priority(char: str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

_sum = 0
for badge in badges:
    _sum += get_priority(badge)

print(_sum)