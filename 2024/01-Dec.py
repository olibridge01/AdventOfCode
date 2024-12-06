from collections import Counter

def dists(l1: list, l2: list) -> int:
    return sum([abs(l1[i] - l2[i]) for i in range(len(l1))])

def sim(l1: list, l2: list) -> int:
    c2 = Counter(l2)
    return sum([i * c2[i] for i in l1 if i in c2])

with open('data/01-Dec.txt') as f:
    # Get list of numbers for each column
    lines = f.readlines()
    l1 = [int(l.split()[0]) for l in lines]
    l2 = [int(l.split()[1]) for l in lines]

l1.sort()
l2.sort()

print(f'Part 1: {dists(l1, l2)}')
print(f'Part 2: {sim(l1, l2)}')