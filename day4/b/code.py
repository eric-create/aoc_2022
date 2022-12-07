lines: list = open('input.txt').read().splitlines()

pairs: list = [(line.split(',')[0], line.split(',')[1]) for line in lines]

pairs = [(
    (pair[0].split('-')[0], pair[0].split('-')[1]),
    (pair[1].split('-')[0], pair[1].split('-')[1])
    ) for pair in pairs]

def overlaps(a_lo: int, a_hi: int, b_lo: int, b_hi: int) -> bool:
    if (a_lo >= b_lo and a_hi <= b_hi) or (b_lo >= a_lo and b_hi <= a_hi) or (a_hi >= b_lo and a_hi <= b_hi) or (a_lo >= b_lo and a_lo <= b_hi):
        return True
    return False

results: list = [overlaps(int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])) for pair in pairs]

print(len([result for result in results if result is True]))