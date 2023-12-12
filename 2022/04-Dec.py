import re
import numpy as np

def get_counts(filename: str) -> tuple(int, int):
    """Get counts of duplicate jobs and overlapping jobs"""
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        duplicates, overlaps = 0, 0

        for line in data:
            line = list(map(int, re.split('-|,', line)))
            a1, a2 = np.arange(line[0], line[1]+1), np.arange(line[2], line[3]+1)
            
            duplicates += np.intersect1d(a1, a2).size == np.min([a1.size, a2.size])
            overlaps += np.intersect1d(a1, a2).size > 0

    return duplicates, overlaps

duplicates, overlaps = get_counts('data/04-Dec.txt')
print(f'Part 1: {duplicates}')
print(f'Part 2: {overlaps}')