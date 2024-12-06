import re
import numpy as np

def path_length(start: str, connectivity: dict, moves: list, part1: bool = True) -> int:
    """Get length of path from starting node to ZZZ or --Z."""
    current_pos = start
    steps, move_idx = 0, 0
    if part1:
        end_cond = lambda x: x != 'ZZZ'
    else:
        end_cond = lambda x: x[-1] != 'Z'
    while end_cond(current_pos):
        steps += 1
        current_pos = connectivity[current_pos][moves[move_idx]]
        move_idx = move_idx + 1 if move_idx < len(moves) - 1 else 0
    return steps

with open('data/08-Dec.txt', 'r') as f:
    moves = [int(char == 'R') for char in f.readline().strip()]
    connectivity = dict()
    f.readline()
    for line in f:
        nodes = re.findall('[A-Z0-9]+', line)
        connectivity[nodes[0]] = (nodes[1], nodes[2])

starts = [key for key in connectivity.keys() if key[-1] == 'A']
paths = [path_length(start, connectivity, moves, part1=False) for start in starts]

print(f'Part 1: {path_length("AAA", connectivity, moves)}')
print(f'Part 2: {np.lcm.reduce(paths)}')