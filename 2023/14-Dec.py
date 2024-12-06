import numpy as np

def shift_rocks(data: np.ndarray) -> np.ndarray:
    """Shift movable rocks North."""
    for i, row in enumerate(data.T):
        l = []
        for j, col in enumerate(row):
            if col in ['.', 'O']:
                l.append(col)
                if j == len(row) - 1:
                    data.T[i, j - len(l) + 1:] = sorted(l, key=lambda x: x == '.')
            else:
                data.T[i, j - len(l):j] = sorted(l, key=lambda x: x == '.')
                l = []
    return data

def total_load(data: np.ndarray) -> int:
    """Compute total load."""
    tot = 0
    for i, row in enumerate(data):
        for col in row:
            if col == 'O':
                tot += len(data) - i
    return tot

def cycle(data: np.ndarray) -> np.ndarray:
    """Compute shifts for one cycle (4 rotations)."""
    for i in range(4):
        data = shift_rocks(data)
        data = np.rot90(data, k=3)
    return data

def cycle_load(data: np.ndarray, n: int) -> int:
    """Compute total load after n cycles."""
    tots = [] # Total loads for each cycle
    pattern = False # Whether pattern has been found

    while not pattern:
        data = cycle(data)
        tots.append(total_load(data))
        if tots.count(tots[-1]) == 3:
            p = np.argwhere(np.array(tots) == tots[-1]).flatten()
            l = (p[1] - p[0]) == (p[2] - p[1]) # Whether gaps between recurring loads are equal
            r1 = tots[p[0] + 1:p[1]] # Loads between recurring loads 1 and 2
            r2 = tots[p[1] + 1:p[2]] # Loads between recurring loads 2 and 3
            if l and r1 == r2 and r1:
                pattern = True

    return tots[p[0] + (n - p[0]) % (p[1] - p[0]) - 1]

with open('data/14-Dec.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

print('Part 1:', total_load(shift_rocks(data)))
print('Part 2:', cycle_load(data, 1000000000))