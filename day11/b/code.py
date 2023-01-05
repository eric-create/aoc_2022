import math

def get_monkeys():
    # Get the actual counts.
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

    return monkeys


def get_expected_counts():
    # Get the expected counts.
    expected_counts_list: list = []
    expected_raw: list = open('expected.txt').read().split('\n\n')

    for expected_block in expected_raw:
        expected_counts: list = []
        for i in range(1, 5):
            expected_counts.append(int(expected_block.splitlines()[i][25:-7]))
        expected_counts_list.append(expected_counts)

    return expected_counts_list



def get_inspection_counts(monkeys: list, reduce_op: str):
    insp_c: list = []

    for index in range(0, 10000):
        for monkey in monkeys:
            while monkey['items']:
                old: int = monkey['items'].pop(0)
                # Monkey inspects
                old = eval(monkey['operation'])
                # Inspection count increases
                monkey['inspection_count'] += 1
                # Monkey did no damage -> reduces stress level
                old = eval(reduce_op)
                # Monkey decides
                target_monkey: int = monkey['true'] if old % monkey['divisor'] == 0 else monkey['false']
                # Monkey passes
                monkeys[target_monkey]['items'].append(old)

        if index % 1000 == 0:
            insp_c.append([monkey['inspection_count'] for monkey in monkeys])

    return insp_c


def main():
    expected_counts_list: list = get_expected_counts()

    # Test reduction operations
    for stress_divisor in range(2, 100, 1):
        reduce_op: str = f"int(math.log(old, {stress_divisor}))"
        inspection_counts_list: list = get_inspection_counts(get_monkeys(), reduce_op)
        diff: int = 0
        sum_a: int = 0
        sum_b: int = 0

        for _j in range(0, len(inspection_counts_list)):
            for _k in range(0, len(inspection_counts_list[_j])):
                sum_a += expected_counts_list[_j][_k]
                sum_b +=inspection_counts_list[_j][_k]
                diff += expected_counts_list[_j][_k] - inspection_counts_list[_j][_k]
    
        print(reduce_op, diff)


if __name__ == '__main__': # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        pass