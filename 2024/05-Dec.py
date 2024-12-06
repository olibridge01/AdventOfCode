from collections import defaultdict

with open('data/05-Dec.txt') as f:
    # Split into two variables by the linebreak
    data = f.read().split('\n\n')
    rule_list = data[0].splitlines()
    updates = [n.split(',') for n in data[1].splitlines()]

rules = defaultdict(list)
for r in rule_list:
    r = r.split('|')
    rules[r[0]].append(r[1])

# Loop to print rules
for k, v in rules.items():
    print(k, v)

for u in updates:
    print(u)

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

# Print sum of middle characters of valid
print(sum([int(v[len(v)//2]) for v in valid]))

print(valid)
print(invalid)

invalid_modified = []
# For each invalid update, reorder the numbers to satisfy the rules
for u in invalid:
    for i, n in enumerate(u):
        history = u[:i]
        # Find indices of all of h in the rules
        indices = [i for i, h in enumerate(history) if h in rules[n]]
        if indices:
            # Find indices of earliest occurence of h in the rules
            earliest = min(indices)
            # Put n in the earliest position and shift the rest forward
            u = u[:earliest] + [n] + u[earliest:i] + u[i+1:]

    invalid_modified.append(u)

print(invalid_modified)
print(sum([int(v[len(v)//2]) for v in invalid_modified]))