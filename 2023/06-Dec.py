import numpy as np

data = np.loadtxt('data/06-Dec.txt', dtype=object)[:,1:] # Load data
data1 = data.astype(int).T # Part 1
data2 = np.array([''.join(line) for line in data]).astype(int).T[None,:] # Part 2

def get_win_ways(data: np.ndarray) -> int:
    """Get number of winning ways for boat race data"""
    win_product = 1
    for race in data:
        roots = np.roots([1, -race[0], race[1]])[::-1]

        # Get number of integers that lie between the range of floats upper and lower
        lower = np.ceil(roots[0]) if roots[0] % 1 else roots[0] + 1
        upper = np.floor(roots[1]) if roots[1] % 1 else roots[1] - 1
        win_product *= len(np.arange(lower, upper + 1))
    return win_product

print(f'Part 1: {get_win_ways(data1)}')
print(f'Part 2: {get_win_ways(data2)}')