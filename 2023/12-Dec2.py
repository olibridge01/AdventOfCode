from functools import cache

@cache
def check_line(seq: str, groups: tuple, n_hash: int = 0) -> int:
    # Base case
    if not seq:
        return 1 if (not groups and not n_hash) else 0
    
    # Recursive case
    n = 0
    if seq[0] in ('#', '?'):
        n += check_line(seq[1:], groups, n_hash + 1)
    if seq[0] in ('.', '?'):
        if (groups and n_hash == groups[0]) or not n_hash:
            if not n_hash:
                n += check_line(seq[1:], groups, 0)
            else:
                n += check_line(seq[1:], groups[1:], 0)
    return n

with open('data/12-Dec.txt', 'r') as f:
    data = [line.split() for line in f.read().splitlines()]
    data = [(seq, tuple(int(a) for a in groups.split(','))) for seq, groups in data]

unfolded_data = [('?'.join([seq] * 5), groups * 5) for seq, groups in data]

print(f'Part 1: {sum([check_line(seq + ".", groups, 0) for seq, groups in data])}')
print(f'Part 2: {sum([check_line(seq + ".", groups, 0) for seq, groups in unfolded_data])}')