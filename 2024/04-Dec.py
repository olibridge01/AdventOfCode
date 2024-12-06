import numpy as np

def search_mas(x: int, y: int) -> int:
    count = 0
    for i in range(max(0, x-1),min(x+2, data.shape[0])):
        for j in range(max(0, y-1),min(y+2, data.shape[1])):
            if data[i,j] == 'M':
                count += check_remainder(i,j,i-x,j-y)
    return count

def check_remainder(x: int, y: int, dx: int, dy: int) -> int:
    rem = 'AS'
    while rem:
        x += dx
        y += dy
        if x < 0 or x >= data.shape[0] or y < 0 or y >= data.shape[1] or data[x,y] != rem[0]:
            return 0
        rem = rem[1:]
    return 1
        
def search_cross(x: int, y: int) -> int:
    poss_corners = ['MMSS','SSMM','MSMS','SMSM']
    corners = ''.join([data[x+i,y+j] for i in [-1,1] for j in [-1,1]])
    if corners in poss_corners:
        return 1
    return 0

with open('data/04-Dec.txt') as f:
    data = np.array([list(line) for line in f.read().splitlines()])

p1 = sum([search_mas(i,j) for i in range(data.shape[0]) for j in range(data.shape[1]) if data[i,j] == 'X'])
p2 = sum([search_cross(i,j) for i in range(1,data.shape[0]-1) for j in range(1,data.shape[1]-1) if data[i,j] == 'A'])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')