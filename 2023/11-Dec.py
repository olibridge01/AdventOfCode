import numpy as np

arry = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arry)
print(np.insert(arry,1,[[10,11,12]],axis=1))

with open('data/test.txt', 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

print(data)

added_rows = 0
for i, row in enumerate(data):
    if np.all(row == '.'):
        added_rows += 1
        data = np.insert(data, i + added_rows, [np.full(len(row), '.')], axis=0)

added_cols = 0
for i, col in enumerate(data.T):
    if np.all(col == '.'):
        added_cols += 1
        data = np.insert(data, i + added_cols, [np.full(len(col), '.')], axis=1)

print(data)
gals = []
for i, row in enumerate(data):
    for j, _ in enumerate(row):
        if data[i,j] == '#':
            gals.append([i,j])

print(gals)

dists = []
for i, gal in enumerate(gals):
    for j, gal2 in enumerate(gals[i+1:]):
        dists.append(np.abs(gal[0] - gal2[0]) + np.abs(gal[1] - gal2[1]))

print(sum(dists))