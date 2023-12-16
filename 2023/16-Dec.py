import numpy as np

def fill_path(data: np.ndarray, x: int, y: int, dx: int, dy: int, filled: bool = None) -> int:
    """Get number of visited cells in data grid."""
    filled = {} if not filled else filled
    while 0 <= x < len(data) and 0 <= y < len(data[0]):
        dir = filled.setdefault((x, y), [])
        if (dx, dy) in dir:
            break
        dir.append((dx, dy))
        if data[x][y] == '/':
            dx, dy = (-dy, -dx)
        elif data[x][y] == '\\':
            dx, dy = (dy, dx)
        elif data[x][y] == '-' and dx:
            fill_path(data, x, y + 1, 0, 1, filled)    
            dx, dy = (0, -1)        
        elif data[x][y] == '|' and dy:
            fill_path(data, x + 1, y, 1, 0, filled)
            dx, dy = (-1, 0)
        x += dx
        y += dy
    return len(filled)

with open('data/16-Dec.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

energies = []
for i, row in enumerate(data):
    energies.append(fill_path(data, i, 0, 0, 1))
    energies.append(fill_path(data, i, len(data.T) - 1, 0, -1))

for j, col in enumerate(data.T):
    energies.append(fill_path(data, 0, j, 1, 0))
    energies.append(fill_path(data, len(data) - 1, j, -1, 0))

print(f'Part 1: {fill_path(data, 0, 0, 0, 1)}')
print(f'Part 2: {max(energies)}')