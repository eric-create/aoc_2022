raw: list = open('input.txt').read().split('\n\n')

monkeys: list = []

for raw_block in raw:
    lines: list = raw_block.splitlines()
    monkeys.append({
        'items': [int(line) for line in lines[1][18:].replace(' ', '').split(',')],
        'inspection_count': 0,
        'operation': lines[2][19:],
        'divisor': int(lines[3][21:]),
        'true': int(lines[4][29:]),
        'false': int(lines[5][30:])})

for i in range(0, 20):
    for monkey in monkeys:
        while monkey['items']:
            old: int = monkey['items'].pop(0)
            # Monkey inspects
            old = eval(monkey['operation'])
            # Inspection count increases
            monkey['inspection_count'] += 1
            # Monkey did no damage -> reduces stress level
            old = int(old/3)
            # Monkey decides
            target_monkey: int = monkey['true'] if old % monkey['divisor'] == 0 else monkey['false']
            # Monkey passes
            monkeys[target_monkey]['items'].append(old)

inspection_counts: list = []
for monkey in monkeys:
    inspection_counts.append(monkey['inspection_count'])

inspection_counts.sort()
print(inspection_counts[-1] * inspection_counts[-2])