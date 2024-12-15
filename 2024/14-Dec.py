import re
from typing import List

GRID_SIZE = (101,103)
mid_1, mid_2 = GRID_SIZE[0] // 2, GRID_SIZE[1] // 2

def step(p: List[int], v: List[int]) -> List[int]:
    p[0] = (p[0] + v[0]) % GRID_SIZE[0]
    p[1] = (p[1] + v[1]) % GRID_SIZE[1]
    return p

with open('data/14-Dec.txt') as f:
    data = [[int(x) for x in re.findall(r'-?\d+', line)] for line in f]
    p = [d[:2] for d in data]
    v = [d[2:] for d in data]

# Part 1
for _ in range(100):
    for i in range(len(p)):
        p[i] = step(p[i], v[i])
    
quadrants = [0, 0, 0, 0]
for i in range(len(p)):
    if p[i][0] < mid_1:
        if p[i][1] < mid_2:
            quadrants[0] += 1
        elif p[i][1] > mid_2:
            quadrants[1] += 1
    elif p[i][0] > mid_1:
        if p[i][1] < mid_2:
            quadrants[2] += 1
        elif p[i][1] > mid_2:
            quadrants[3] += 1

print(f'Part 1: {quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]}')

# Part 2
for i in range(110000):
    for j in range(GRID_SIZE[1]):
        row, n = sorted({d[0] for d in data if d[1] == j}), 0
        for k in range(len(row) - 1):
            n = n + 1 if row[k + 1] == row[k] + 1 else 0
            if n > 10:
                print(f'Part 2: {i}')
                quit()
    for d in data: d[0], d[1] = (d[0] + d[2]) % 101, (d[1] + d[3]) % 103