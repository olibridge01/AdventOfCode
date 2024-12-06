import numpy as np

def rev(move: list) -> list:
    return [-i for i in move]
    
def first_move(data: np.ndarray) -> tuple:
    """Get first move from initial position S."""
    init_pos = np.concatenate(np.where(data == 'S'))
    for i in [[1,0],[-1,0],[0,1],[0,-1]]:
        pos = [init_pos[j] + i[j] for j, _ in enumerate(init_pos)]
        
        if all([0 <= pos[j] < data.shape[j] for j, _ in enumerate(pos)]):
            char = data[tuple(pos)]
            if char != '.' and rev(i) in moves[char]:
                return pos, i
            
def farthest_point(data: np.ndarray, pos: list, i: list) -> tuple:
    """Get farthest point from S."""
    loop_pos = [pos]
    path_length = 0
    while data[tuple(pos)] != 'S':
        char = data[tuple(pos)]
        i = moves[char][0] if np.any(moves[char][0] != rev(i)) else moves[char][1]
        pos = [pos[j] + i[j] for j, _ in enumerate(pos)]
        path_length += 1
        loop_pos.append(pos)
    
    return np.ceil(path_length / 2).astype(int), loop_pos

def enclosed_area(data: np.ndarray, loop_pos: list) -> int:
    """Get enclosed area by loop containing S."""
    n_points = 0
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            n = len([k for l, k in enumerate(row[:j]) if k in ['|', 'F', '7'] and [i,l] in loop_pos])
            if [i,j] not in loop_pos:
                n_points += n % 2
    print(len(loop_pos))
    return n_points

moves = {
    '|': [[1,0],[-1,0]],
    '-': [[0,1],[0,-1]],
    'L': [[-1,0],[0,1]],
    'J': [[-1,0],[0,-1]],
    '7': [[1,0],[0,-1]],
    'F': [[1,0],[0,1]],
}

with open('data/10-Dec.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

pos, i = first_move(data)
max_dist, loop_pos = farthest_point(data, pos, i)

print(f'Part 1: {max_dist}')
print(f'Part 2: {enclosed_area(data, loop_pos)}')