def get_marker(data: str, n: int) -> int:
    """Get the first marker of n consecutive digits in data."""
    return [i+n for i, _ in enumerate(data[n-1:]) if len(set(data[i:i+n])) == n][0]

with open('data/06-Dec.txt', 'r') as f:
    data = f.read().strip()
print(f'Part 1: {get_marker(data, 4)}')
print(f'Part 2: {get_marker(data, 14)}')