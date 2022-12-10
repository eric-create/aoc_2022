lines: list = open('input.txt').read().splitlines()


history: list = []
register: int = 1

for line in lines:
    if line.startswith('addx'):
        history.extend([register, register])
        register += int(line[5:])
    if line.startswith('noop'):
        history.append(register)
history.append(register)

_sum = 0

for i in range(0, 6):
    index: int = i*40+20
    _sum += history[index-1]*index
    print(history[index-1]*index)

print()
print(_sum)