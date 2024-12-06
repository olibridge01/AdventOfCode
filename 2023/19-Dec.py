import re

def check_condition(c: tuple, input: dict) -> str:
    """Check if condition is met, and return destination if so."""
    if c[0] != 'True':
        vals = re.split('<|>', c[0])
        if c[0][1] == '>':
            return c[1] if input[vals[0]] > int(vals[1]) else False
        else:
            return c[1] if input[vals[0]] < int(vals[1]) else False
    else:
        return c[1]
        
def accepted_sum(workflows: dict, input: dict) -> int:
    """Calculate sum of accepted values."""
    tot = 0
    complete = False
    workflow = workflows['in']
    while not complete:
        for c in workflow:
            i = check_condition(c, input)
            if not i:
                continue
            elif i == 'R':
                complete = True
                break
            elif i == 'A':
                tot += sum(input.values())
                complete = True
                break
            else:
                workflow = workflows[i]
                break
    return tot

def get_subtotal(criteria: list) -> int:
    """Get subtotal from set of valid values."""
    vals = {'x': [0] + [1] * 4000, 
            'm': [0] + [1] * 4000, 
            'a': [0] + [1] * 4000, 
            's': [0] + [1] * 4000
    }
    for c in criteria:
        if c != 'True':
            if c[0] == '!':
                c = c[1:]
                cat, c, lim = c[0], c[1], int(c[2:])
                if c == '<':
                    for i in range(1, lim):
                        vals[cat][i] = 0
                else:
                    for i in range(lim + 1, 4001):
                        vals[cat][i] = 0
            else:
                cat, c, lim = c[0], c[1], int(c[2:])
                if c == '<':
                    for i in range(lim, 4001):
                        vals[cat][i] = 0
                else:
                    for i in range(1, lim + 1):
                        vals[cat][i] = 0
    subtotal = 1
    for cat, valid in vals.items():
        subtotal *= sum(valid)
    return subtotal

def get_total(name: str, previous_crit: list, previous_dest: list) -> int:
    """Get total number of valid values."""
    total = 0
    inverted_criteria = []
    for criteria, dest in workflows[name]:
        if dest == 'A':
            total += get_subtotal(previous_crit + inverted_criteria + [criteria])
            inverted_criteria += ['!' + criteria]
        else:
            if dest != 'R':
                total += get_total(dest, previous_crit + inverted_criteria + [criteria], previous_dest + [name])
            inverted_criteria += ['!' + criteria]
    return total

workflows = {}
inputs = []

with open('data/19-Dec.txt') as f:
    d1, d2 = f.read().split('\n\n')
    d1 = d1.splitlines()
    d2 = d2.splitlines()

    for l in d1:
        a, b = l[:-1].split('{')
        workflows[a] = []
        for element in b.split(','):
            parts = element.split(':')
            if len(parts) == 2:
                workflows[a].append((parts[0], parts[1]))
            else:
                workflows[a].append(('True', parts[0]))
        
    for l in d2:
        l = l[1:-1].split(',')
        input = {}
        for i in l:
            vals = i.split('=')
            input[vals[0]] = int(vals[1])
        inputs.append(input)

print(f'Part 1: {sum([accepted_sum(workflows, input) for input in inputs])}')
print(f'Part 2: {get_total("in", [], [])}')