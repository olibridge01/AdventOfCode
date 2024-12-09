from typing import List

def get_disk(data: str) -> List:
    disk = []
    for i, n in enumerate(data):
        if i % 2 == 0:
            disk.extend([i // 2] * int(n))
        else:
            disk.extend(['.'] * int(n))
    return disk

def part1(disk: List) -> int:
    # Two-pointer method
    p1 = 0
    p2 = len(disk) - 1

    while p1 < p2:
        if disk[p2] != '.' and disk[p1] == '.':
            disk[p1], disk[p2] = disk[p2], disk[p1]
            p1 += 1
            p2 -= 1
        elif disk[p1] != '.':
            p1 += 1
        elif disk[p2] == '.':
            p2 -= 1
    return sum([i * int(n) for i, n in enumerate(disk) if n != '.'])

def part2(data: str) -> int:
    # Get blocks including file sizes for brute force :(
    blocks = [(i//2+1 if i%2 else 0, int(d)) for i,d in enumerate(data, 1)]
    flatten = lambda x: [x for x in x for x in x]

    for i in range(len(blocks))[::-1]:
        for j in range(i):
            i_data, i_size = blocks[i]
            j_data, j_size = blocks[j]

            if i_data and not j_data and i_size <= j_size:
                blocks[i] = (0, i_size)
                blocks[j] = (0, j_size - i_size)
                blocks.insert(j, (i_data, i_size))

    return sum(i * (c-1) for i,c in enumerate(flatten([b] * s for b,s in blocks)) if c)
        
with open('data/09-Dec.txt') as f:
    data = f.read().replace('\n', '')

disk = get_disk(data)
print(f'Part 1: {part1(disk)}')
print(f'Part 2: {part2(data)}')