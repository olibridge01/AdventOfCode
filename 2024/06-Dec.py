import numpy as np
from itertools import cycle

def simulate(pos: np.ndarray, data: np.ndarray):
    dirs = cycle([np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])])
    dir = next(dirs)
    
    visited = {tuple(pos)}
    dir_cache = {(pos[0], pos[1], dir[0], dir[1])}

    while True:
        new_pos = tuple(pos + dir) # Get next position
    
        if new_pos[0] < 0 or new_pos[0] >= data.shape[0] or new_pos[1] < 0 or new_pos[1] >= data.shape[1]:
            return visited, False
        
        elif data[new_pos] == '#':
            dir = next(dirs)

        else:
            pos = np.array(new_pos)
            visited.add(tuple(pos))

            # Check if np array dirs[dir_i] is in visited
            c = (pos[0], pos[1], dir[0], dir[1])
            if c in dir_cache:
                return visited, True
            else:
                dir_cache.add(c)

with open('data/06-Dec.txt') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])
    
pos = np.array(np.where(data == '^')).T[0]
visited, loop = simulate(pos, data) # Part 1, simulate on the original data

count = 0
candidates = visited - set([tuple(pos)]) # Part 2, check for infinite loops after adding obstacle to each visited position except the starting one

for i in range(data.shape[0]):
    for j in range(data.shape[1]):

        if (i, j) in candidates:
            old_char = data[i, j]
            data[i, j] = '#'

            _, loop = simulate(pos, data)
            if loop:
                count += 1

            data[i, j] = old_char
    
print(f'Part 1: {len(visited)}')
print(f'Part 2: {count}')