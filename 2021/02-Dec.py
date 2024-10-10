def move(pos: tuple, direction: str, steps: int, aim: int = None) -> tuple:
    """Move submarine."""
    if aim is None:
        return (pos[0] + DIRECTIONS[direction][0] * steps, pos[1] - DIRECTIONS[direction][1] * steps)
    else:
        if direction == 'down':
            aim += steps
        elif direction == 'up':
            aim -= steps
        else:
            pos = (pos[0] + steps, pos[1] + steps * aim)
        return pos, aim

with open('data/02-Dec.txt', 'r') as file:
    data = file.read().splitlines()
    data = [i.split(' ') for i in data]

pos1 = pos2 = (0,0)
aim = 0
DIRECTIONS = {'forward': (1,0), 'up': (0,1), 'down': (0,-1)}

for l in data:
    direction = l[0]
    steps = int(l[1])
    pos1 = move(pos1, direction, steps)
    pos2, aim = move(pos2, direction, steps, aim)

print(f'Part 1: {pos1[0] * pos1[1]}')
print(f'Part 2: {pos2[0] * pos2[1]}')