from collections import defaultdict
import re

def drop(bricks: list) -> tuple:
    """Drop all bricks and return the number of falls and the new bricks."""
    highest = defaultdict(int)
    new_bricks = []
    falls = 0
    for br in bricks:
        new_br = drop_brick(highest, br)
        if new_br[2] != br[2]:
            falls += 1
        new_bricks.append(new_br)
        for x in range(br[0], br[3] + 1):
            for y in range(br[1], br[4] + 1):
                highest[(x, y)] = new_br[5]
    return falls, new_bricks

def drop_brick(highest: dict, br: tuple) -> tuple:
    """Drop a single brick and return the new brick."""
    peak = max(highest[(x, y)] for x in range(br[0], br[3] + 1) for y in range(br[1], br[4] + 1))
    dz = max(br[2] - peak - 1, 0) # Drop height
    return (br[0], br[1], br[2] - dz, br[3], br[4], br[5] - dz)

def solve(data: list) -> tuple:
    """Solve Part 1 and Part 2 given a snapshot of bricks."""
    bricks = sorted(data, key=lambda x: x[2])
    _, fallen = drop(bricks)
    p1 = p2 = 0
    for i in range(len(fallen)):
        removed = fallen[:i] + fallen[i + 1:] # Remove the i-th brick
        falls, _ = drop(removed) # Count number of falls
        if not falls:
            p1 += 1 # Increment part 1 counter
        else:
            p2 += falls # Increment part 2 counter
    return p1, p2

with open('data/22-Dec.txt', 'r') as f:
    data = f.read().splitlines()
    data = [tuple(map(int, re.findall(r'-?\d+', x))) for x in data] # Split by , or ~ and convert to int

solution = solve(data)
print(f'Part 1: {solution[0]}')
print(f'Part 2: {solution[1]}')