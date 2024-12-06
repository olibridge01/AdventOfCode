from collections import defaultdict
from typing import List, Dict

def split_updates(rules: Dict[str, List[str]], updates: List[List[str]]) -> List[List[str]]:
    valid = []
    invalid = []
    for u in updates:
        is_valid = True
        for i, n in enumerate(u):
            history = u[:i]
            if any([h in rules[n] for h in history]):
                is_valid = False
                invalid.append(u)
                break
        if is_valid:
            valid.append(u)
    return valid, invalid

def reorder_invalid(rules: Dict[str, List[str]], invalid: List[List[str]]) -> List[List[str]]:
    invalid_modified = []
    for u in invalid:
        for i, n in enumerate(u):
            history = u[:i]
            indices = [i for i, h in enumerate(history) if h in rules[n]]
            if indices:
                earliest = min(indices)
                u = u[:earliest] + [n] + u[earliest:i] + u[i+1:] # Put n before earliest violation of rules

        invalid_modified.append(u)
    return invalid_modified

with open('data/05-Dec.txt') as f:
    data = f.read().split('\n\n')
    rule_list = data[0].splitlines()
    updates = [n.split(',') for n in data[1].splitlines()]

# Create dict of rules
rules = defaultdict(list)
for r in rule_list:
    r = r.split('|')
    rules[r[0]].append(r[1])

valid, invalid = split_updates(rules, updates)
invalid_modified = reorder_invalid(rules, invalid)

print(f'Part 1: {sum([int(v[len(v)//2]) for v in valid])}')
print(f'Part 2: {sum([int(v[len(v)//2]) for v in invalid_modified])}')