import re


lines: str = open('input.txt').read().splitlines()
directives = [line for line in lines if line.startswith('move')]

stackLines: list = []
stackLinesLen: list = []
for line in lines:
    if '[' in line:
        stackLinesLen.append(line.count('['))
        stackLines.append(line)
    else:
        break

stackLinesLen.sort()
stackLinesLen: int = stackLinesLen[-1]
stackLinesHig: int = len(stackLines)

stacks: list = [[] for _ in range(0, stackLinesLen)]

for x in range(0, stackLinesLen):
    for y in range(stackLinesHig - 1, -1, -1):
        crate: str = stackLines[y][1 + x*4].strip()
        if crate:
            stacks[x].append(crate)

for directive in directives:
    count: int = int(re.search(r'move (\d+)', directive).groups(1)[0])
    source: int = stacks[int(re.search(r'from (\d+)', directive).groups(1)[0]) - 1]
    target: int = stacks[int(re.search(r'to (\d+)', directive).groups(1)[0]) - 1]

    for operation in range(0, count):
        if source:
            target.append(source.pop())

for stack in stacks:
    print(stack[-1], end='')
print()