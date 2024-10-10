G = {(i, j): c for i, r in enumerate(open('data/21-Dec.txt'))
                   for j, c in enumerate(r) if c in ['.', 'S']}

done = []
pos = {x for x in G if G[x] == 'S'}
cmod = lambda x: (x[0] % 131, x[1] % 131) # Get relative grid position on current 'tile'

for s in range(3 * 131):
    if s == 64: 
        print(f'Part 1: {len(pos)}')
    if s % 131 == 65: 
        done.append(len(pos))

    pos = {(p[0] + d[0], p[1] + d[1]) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                                      for p in pos 
                                      if cmod((p[0] + d[0], p[1] + d[1])) in G}

f = lambda n, a, b, c: a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
print(f'Part 2: {f(26501365 // 131, *done)}')