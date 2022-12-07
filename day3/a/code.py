lines = open('input.txt').read().splitlines()

backpacks: list = [(line[:int(len(line)/2)], line[int(len(line)/2):]) for line in lines]

duplicates: list = []

for backpack in backpacks:
    cur_d: list = []
    for item in backpack[0]:
        if item in backpack[1]:
            cur_d.append(item)
    duplicates.append(list(set(cur_d))[0])


def get_priority(char: str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

_sum = 0

for duplicate in duplicates:
    _sum += get_priority(duplicate)

# print(duplicates)
print(_sum)