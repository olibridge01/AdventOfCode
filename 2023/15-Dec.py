import numpy as np

def hash(s):
    """Run HASH algorithm on a string."""
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n = n % 256
    return n

def operation(s, boxes):
    """Perform operation on the dict of boxes."""
    if '=' in s:
        lens = s.split('=')
        pos = hash(lens[0])
        for i, entry in enumerate(boxes[pos]):
            if entry[0] == lens[0]:
                boxes[pos][i] = lens # Update focal length
                return boxes
        boxes[pos].append(lens) # Add new lens
    else:
        lens = s[:-1]
        pos = hash(lens)
        for i, entry in enumerate(boxes[pos]):
            if entry[0] == lens:
                boxes[pos].pop(i) # Remove lens
    return boxes

def foc_power(boxes):
    """Compute total focal power of lenses."""
    p = 0
    for box, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            p += (box + 1) * (i + 1) * int(lens[1]) # Formula from problem
    return p

with open('data/15-Dec.txt', 'r') as f:
    data = f.read().strip().split(',')

boxes = {i: [] for i in range(256)} # Generate dict of boxes
for s in data:
    boxes = operation(s, boxes) # Perform operations from data

print(f'Part 1: {sum(hash(s) for s in data)}')
print(f'Part 2: {foc_power(boxes)}')