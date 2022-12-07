lines: str = open('./input.txt').read()

elves: list = lines.split('\n\n')

calorie_sums: list = []

for i, elve in enumerate(elves):
    items: list = elve.splitlines()
    calorie_sums.append(0)

    for item in items:
        calorie_sums[i] += int(item)

calorie_sums.sort()
print(calorie_sums[-1])

top_three = 0
for calories in calorie_sums[-3:]:
    top_three += calories
print(top_three)