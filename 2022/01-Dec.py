import numpy as np

def get_totals(filename: str) -> np.ndarray:
    """Get list of total calories for each elf"""
    with open(filename) as f:
        lines = f.read().split('\n\n')

        # Compute calorie totals for each elf
        calories = [[int(a) for a in line.splitlines()] for line in lines]
        totals = [np.sum(calorie) for calorie in calories]

    return np.sort(totals)[::-1] # Return totals sorted in descending order

filename = 'data/01-Dec.txt'
print(f'Part 1: {np.amax(get_totals(filename))}')
print(f'Part 2: {np.sum(get_totals(filename)[:3])}')