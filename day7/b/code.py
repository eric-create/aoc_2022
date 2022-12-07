lines: list = open('input.txt').read().splitlines()

operations: list = []

while lines:
    line = lines.pop(0)
    operation: dict = {}

    if line.startswith('$ cd'):
        operation['type'] = 'cd'
        operation['input'] = line[5:]

    if line.startswith('$ ls'):
        operation['type'] = 'ls'
        operation['input'] = line[5:]
        operation['output'] = []

        while lines and not lines[0].startswith('$'):
            outputLine: str = lines.pop(0)
            operation['output'].append((outputLine.split(' ')[0], outputLine.split(' ')[1]))

    operations.append(operation)

TREE: dict = {'files': [], 'size': 0}

current: dict = TREE

for operation in operations:
    if operation['type'] == 'cd':
        destination: str = operation['input']
        if destination == '/':
            current = TREE
        elif destination == '..':
            current = current['parent']
        else:
            if destination in current:
                current = current[destination]
            else:
                current[destination] = {'parent': current, 'files': [], 'size': 0}

    if operation['type'] == 'ls':
        for element in operation['output']:
            if element[0] == 'dir':
                if element[1] not in current:
                    current[element[1]] = {'parent': current, 'files': [], 'size': 0}
            else:
                current['files'].append(element)
                current['size'] += int(element[0])

def get_directories(current: dict) -> list:
    keys: list = list(current)
    if 'parent' in keys: keys.remove('parent')
    if 'files' in keys: keys.remove('files')
    keys.remove('size')
    return keys


def update_parent_size(size: int, current: dict) -> None:
    if 'parent' in current:
        current['parent']['size'] += current['size']


def traverse(current: dict, func) -> None:
    for directory in get_directories(current):
        traverse(current[directory], func)
    func(current['size'], current)


traverse(TREE, update_parent_size)
sizes: list = []
traverse(TREE, lambda size, _: sizes.append(size if size <= 100000 else 0))
print(sum(sizes))