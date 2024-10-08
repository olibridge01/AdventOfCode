def get_area(points: list) -> int:
    """Get area with shoelace formula."""
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i+1][1]
        area -= points[i][1] * points[i+1][0]
    return abs(area) // 2

def get_points(data: list, part1: bool = True) -> tuple:
    """Get points and perimeter of dig hole."""
    perimeter = 0
    points = [(0,0)]

    if part1:
        directions = {'R': (1,0), 'D': (0,-1), 'L': (-1,0), 'U': (0,1)}
    else:
        directions = {'0': (1,0), '1': (0,-1), '2': (-1,0), '3': (0,1)}

    for l in data:
        if part1:
            dir = directions[l[0]]
            d = int(l[1])
        else:
            dir = directions[l[2][7]]
            d = int(l[2][2:7], 16)
        perimeter += d
        points.append((points[-1][0] + dir[0] * d, points[-1][1] + dir[1] * d))
    return points, perimeter

with open('data/18-Dec.txt', 'r') as f:
    data = f.read().splitlines()
    for i, l in enumerate(data):
        a, b, c = l.split(' ')
        data[i] = [a, int(b), c]

points1, perimeter1 = get_points(data)
points2, perimeter2 = get_points(data, part1=False)

print(f'Part1: {get_area(points1) + perimeter1 // 2 + 1}')
print(f'Part2: {get_area(points2) + perimeter2 // 2 + 1}')