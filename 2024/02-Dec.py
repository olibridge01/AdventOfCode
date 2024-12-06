def generate_diff(r: list) -> list:
    return [s - f for f, s in zip(r, r[1:])]

def check_report(r: list) -> int:
    d = generate_diff(r)
    return 1 if (all([-3 <= x < 0 for x in d]) or all([0 < x <= 3 for x in d])) else 0

def check_with_removal(r: list) -> int:
    if check_report(r):
        return 1

    for i, level in enumerate(r):
        chopped_r = r[:i] + r[i+1:]
        if check_report(chopped_r):
            return 1
    return 0

with open('data/02-Dec.txt', 'r') as f:
    reports = [[int(x) for x in line.split()] for line in f]

print(f'Part 1: {sum([check_report(r) for r in reports])}')
print(f'Part 2: {sum([check_with_removal(r) for r in reports])}')