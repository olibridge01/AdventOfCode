import numpy as np
from typing import Tuple, List
from itertools import combinations
from collections import defaultdict

def antinodes(pos1: np.ndarray, pos2: np.ndarray, shape: Tuple[int], p1: bool = True) -> List[np.ndarray]:
    diff = pos2 - pos1
    ans = []
    
    while in_bounds(pos1 - diff, shape):
        ans.append(pos1 - diff)
        if p1:
            break
        diff += pos2 - pos1
    diff = pos2 - pos1

    while in_bounds(pos2 + diff, shape):
        ans.append(pos2 + diff)
        if p1:
            break
        diff += pos2 - pos1

    if not p1:
        ans.extend([pos1, pos2])
    return ans

def in_bounds(pos: np.ndarray, shape: Tuple[int]) -> bool:
    return 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]

def get_antennae(data: np.ndarray) -> defaultdict:
    antennae = defaultdict(list)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] != '.':
                antennae[data[i, j]].append(np.array([i, j]))
    return antennae

def get_antinodes(data: np.ndarray, p1: bool = True) -> set:
    antinode_set = set()
    antennae = get_antennae(data)
    for ant, positions in antennae.items():
        for pos1, pos2 in combinations(positions, 2):
            ans = antinodes(pos1, pos2, shape=data.shape, p1=p1)
            for a in ans:
                antinode_set.add(tuple(a))
    return antinode_set

with open('data/08-Dec.txt') as f:
    data = np.array([list(line) for line in f.read().splitlines()])

antennae = get_antennae(data)

print(f'Part 1: {len(get_antinodes(data, p1=True))}')
print(f'Part 2: {len(get_antinodes(data, p1=False))}')