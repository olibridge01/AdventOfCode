def get_duplicate(rucksack: str) -> str:
    """Get duplicate item in each compartment"""
    c1, c2 = {*rucksack[:len(rucksack)//2]}, {*rucksack[len(rucksack)//2:]}
    return (c1 & c2).pop()

def get_badge(group: list) -> str:
    """Get common badge from group of rucksacks"""
    return set.intersection(*map(set, group)).pop()

def get_priority(letter: str) -> int:
    """Get priority of letter"""
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38

with open('data/03-Dec.txt', 'r') as f:
    rucksacks = f.read().splitlines()
    priorities = [get_priority(get_duplicate(rucksack)) for rucksack in rucksacks]
    groups = [[rucksacks[i], rucksacks[i+1], rucksacks[i+2]] for i in range(0, len(rucksacks), 3)]
    badges = [get_priority(get_badge(group)) for group in groups]

print(f'Part 1: {sum(priorities)}')
print(f'Part 2: {sum(badges)}')