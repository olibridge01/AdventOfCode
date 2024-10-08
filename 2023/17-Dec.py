import numpy as np
import heapq

def min_heat(data: np.ndarray, start: tuple, end: tuple, min_move: int, max_move: int) -> int:
    """Get path of minimum heat from start to end, with min/max move constraints."""
    queue = [(0, *start, 0, 0)] # Initialise queue
    visited = set() # Initialise set of visited nodes
    while queue:
        heat, x, y, px, py = heapq.heappop(queue) # Pop node with lowest heat
        if (x, y) == end:
            return heat
        if (x, y, px, py) in visited:
            continue
        visited.add((x, y, px, py))
        for dx, dy in {(0, 1), (0, -1), (1, 0), (-1, 0)} - {(px, py), (-px, -py)}:
            new_x, new_y, new_heat = x, y, heat
            for i in range(1, max_move + 1):
                new_x, new_y = new_x + dx, new_y + dy
                if (0 <= new_x < len(data) and 0 <= new_y < len(data[0])):
                    new_heat += data[new_x,new_y]
                    if i >= min_move:
                        heapq.heappush(queue, (new_heat, new_x, new_y, dx, dy))

with open('data/17-Dec.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()], dtype=int)

print(f'Part 1: {min_heat(data, (0, 0), (len(data) - 1, len(data[0]) - 1), 1, 3)}')
print(f'Part 2: {min_heat(data, (0, 0), (len(data) - 1, len(data[0]) - 1), 4, 10)}')