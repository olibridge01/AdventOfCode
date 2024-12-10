import numpy as np

def get_score(data: np.ndarray, i: int, j: int, curr_num: int, cache: set, p1: bool) -> int:
    if i < 0 or i >= data.shape[0] or j < 0 or j >= data.shape[1] or data[i,j] != curr_num:
        return 0
    if curr_num == 9:
        if p1 and (i,j) not in cache:
            cache.add((i,j))
            return 1
        elif not p1:
            return 1
    return get_score(data, i+1, j, curr_num+1, cache, p1) + get_score(data, i-1, j, curr_num+1, cache, p1) + get_score(data, i, j+1, curr_num+1, cache, p1) + get_score(data, i, j-1, curr_num+1, cache, p1)

with open('data/10-Dec.txt') as f:
    data = np.array([[int(x) for x in list(line.strip())] for line in f])

print(f'Part 1: {sum([get_score(data, i, j, 0, set(), p1=True) for i in range(data.shape[0]) for j in range(data.shape[1])])}')
print(f'Part 2: {sum([get_score(data, i, j, 0, set(), p1=False) for i in range(data.shape[0]) for j in range(data.shape[1])])}')