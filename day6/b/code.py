lines: list = open('input.txt').read().splitlines()

for line in lines:
    linelen: int = len(line)
    for i in range(0, linelen - 14):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            break