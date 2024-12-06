import re

def get_data(filename: str) -> tuple(list, list):
    """Get initial state of crates from file"""
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        header = data[:data.index('')] # Initial crate configuration
        moves_data = data[data.index('')+1:] # Sequence of moves
        moves = [[int(i) for i in re.findall(r'\d+', line)] for line in moves_data]

        # Initialise crates list of lists
        crates = [[int(i)] for i in header[-1].split()]
        for line in header[-2::-1]:
            for i, val in enumerate(range(1, len(line), 4)):
                if line[val] != ' ':
                    crates[i].append(line[val])
            
    return crates, moves

def move_crates(crates: list, move: list, part1: bool = True) -> list:
    """Move crate from one stack to another"""
    n = move[0]
    from_stack, to_stack = move[1] - 1, move[2] - 1

    # Modify crate stacks by applying move
    if part1:
        crates[to_stack].extend(crates[from_stack][:-(n + 1):-1])
    else:
        crates[to_stack].extend(crates[from_stack][-n:])
    crates[from_stack] = crates[from_stack][:-n]

    return crates

def get_message(filename: str, part1: bool = True) -> str:
    """Get message from crates"""
    crates, moves = get_data(filename)

    # Apply moves to crates
    for move in moves:
        crates = move_crates(crates, move, part1)

    return ''.join(crate[-1] for crate in crates)

print(f'Part 1: {get_message("data/05-Dec.txt")}')
print(f'Part 2: {get_message("data/05-Dec.txt", part1=False)}')