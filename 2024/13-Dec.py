import numpy as np
import re

def compute_cost(data: list, p1: bool = True):
    cost = 0
    for i in range(0, len(data), 4):
        mat = np.array([[int(x) for x in re.findall(r'\d+', data[i])] for i in range(i, i+2)]).T
        prize = np.array([int(x) for x in re.findall(r'\d+', data[i+2])])
        prize[0] = prize[0] if p1 else prize[0] + 10000000000000
        prize[1] = prize[1] if p1 else prize[1] + 10000000000000
        sol = np.linalg.solve(mat, prize)
        if np.isclose(sol - np.round(sol), 0, atol=1e-4).all():
            cost += 3 * sol[0] + sol[1]
    return int(cost)

with open('data/13-Dec.txt') as f:
    data = f.read().splitlines()

print(f'Part 1: {compute_cost(data, p1=True)}')
print(f'Part 2: {compute_cost(data, p1=False)}')