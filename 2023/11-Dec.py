import numpy as np

def empty_indices(data: np.ndarray) -> list:
    """Get indices of empty rows in 2D array."""
    return [i for i, row in enumerate(data) if np.all(row == '.')]

def galaxy_dists(data: np.ndarray, n: int) -> int:
    """Get sum of distances between galaxies given space expansion multiplier."""
    empty_rows = empty_indices(data)
    empty_cols = empty_indices(data.T)
    gals = [[i,j] for i, j in np.ndindex(data.shape) if data[i,j] == '#']

    dists = []
    for i, gal1 in enumerate(gals):
        for gal2 in gals[i+1:]:
            xlims = sorted([gal1[0], gal2[0]])
            ylims = sorted([gal1[1], gal2[1]])

            n_empty_rows = len([k for k in empty_rows if xlims[0] < k < xlims[1]])
            n_empty_cols = len([k for k in empty_cols if ylims[0] < k < ylims[1]])

            dists.append(xlims[1] - xlims[0] + ylims[1] - ylims[0] + (n - 1) * (n_empty_rows + n_empty_cols))

    return sum(dists)

with open('data/11-Dec.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

print(f'Part 1: {galaxy_dists(data, 2)}')
print(f'Part 2: {galaxy_dists(data, 1000000)}')