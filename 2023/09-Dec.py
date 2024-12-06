import numpy as np

data = np.loadtxt('data/09-Dec.txt', dtype=int) # Load data

def next_num(seq, forward=True):
    """Extrapolate forward or backward from a sequence."""
    diffs = [seq] if forward else [seq[::-1]]
    
    while np.any(np.diff(diffs[-1])):
        diffs.append(np.diff(diffs[-1]))

    next = sum([d[-1] for d in diffs])
    return next

print(f'Part 1: {np.sum([next_num(seq) for seq in data])}')
print(f'Part 2: {np.sum([next_num(seq, forward=False) for seq in data])}')