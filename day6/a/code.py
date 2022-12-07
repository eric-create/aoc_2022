lines: list = open('input.txt').read().splitlines()

print(lines)

for line in lines:
    linelen: int = len(line)
    for i in range(0, linelen - 4):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            break