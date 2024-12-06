class Dir:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}

class File:
    def __init__(self, name, size, dir):
        self.name = name
        self.dir = dir
        self.size = size


with open('data/test.txt') as f:
    data = f.read().splitlines()

root = Dir('/', parent=None)

for line in data[1:]:
    
    line = line.split()
    
    if line[0] == '$':
        if line[1] == 'ls':
    
        # Check if line[0] is a number
        # If it is, it's a file
    elif line[0].isdigit():
        size = int(line[0])
        name = line[1]
        file = File(name, size, root)
        root.size += size


