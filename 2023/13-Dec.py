import numpy as np

def mirror_index(p: np.ndarray, part1: bool = True) -> list:
    """Check for mirror line in rows."""
    indices = []
    for i, _ in enumerate(p[1:], start=1):
        r = np.min([p.shape[0] - i, i]) # Range of rows to check for mirror image

        if part1:
            if np.all(p[i - r:i] == np.flip(p[i:i + r], axis=0)):
                indices.append(i)
        else:
            if np.sum(p[i - r:i] != np.flip(p[i:i + r], axis=0)) == 1:
                indices.append(i)
    return indices

def get_summary(data: list, part1: bool = True) -> list:
    """Get summary of data."""
    return sum([100 * sum(mirror_index(p, part1)) + sum(mirror_index(p.T, part1)) for p in data])

with open('data/13-Dec.txt', 'r') as f:
    data = f.read().split('\n\n')
    data = [np.array([list(line.strip()) for line in l.split('\n')]) for l in data]

print('Part 1:', get_summary(data))
print('Part 2:', get_summary(data, part1=False))