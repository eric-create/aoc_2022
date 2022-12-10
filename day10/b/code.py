lines: list = open('input.txt').read().splitlines()

history: list = []
register: int = 1

for line in lines:
    if line.startswith('addx'):
        history.extend([register, register])
        register += int(line[5:])
    if line.startswith('noop'):
        history.append(register)


for i, sprite_position in enumerate(history):
    position : int = i % 40
    if position == 0:
        print()
    if position >= sprite_position - 1 and position <= sprite_position + 1:
        print('#', end='')
    else:
        print('.', end='')
print()