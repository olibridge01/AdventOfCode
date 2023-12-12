import numpy as np
import re
import itertools

data = []
with open('data/12-Dec.txt', 'r') as f:
    for line in f:
        line_dat = []
        line_dat.append(line.strip().split(' ')[0])
        line_dat.append([int(a) for a in line.strip().split(' ')[1].split(',')])
        data.append(line_dat)

# print(data)

def get_unknowns(line):
    unknowns = []
    hashcount = 0
    for i, char in enumerate(line):
        if char == '?':
            unknowns.append(i)
        elif char == '#':
            hashcount += 1
    return unknowns, hashcount

def get_combos(unknowns, k):
    return list(itertools.combinations(unknowns, k))

def check_combo(combo, line, groups):
    filled_line = line
    for i, char in enumerate(filled_line):
        if char == '?':
            if i in combo:
                filled_line = filled_line[:i] + '#' + filled_line[i+1:]
            else:
                filled_line = filled_line[:i] + '.' + filled_line[i+1:]
    
    # Count the size of the groups of #
    group_sizes = []
    group_size = 0
    for i, char in enumerate(filled_line):
        if char == '#':
            group_size += 1
        else:
            if group_size > 0:
                group_sizes.append(group_size)
                group_size = 0
        if i == len(filled_line) - 1 and group_size > 0:
            group_sizes.append(group_size)
            
    # print(group_sizes)
    return 1 if group_sizes == groups else 0
s = 0
for line in data:
    unknowns, hashcount = get_unknowns(line[0])
    combos = get_combos(unknowns, sum(line[1]) - hashcount)
    # print(combos)
    
    for combo in combos:
        s += check_combo(combo, line[0], line[1])
    
print(s)
    





