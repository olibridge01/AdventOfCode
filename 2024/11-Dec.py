def solve(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    elif (stone, blinks) in cache:
        return cache[(stone, blinks)]
    elif stone == 0:
        num = solve(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        split = len(str(stone)) // 2
        num = solve(int(str(stone)[:split]), blinks - 1) + solve(int(str(stone)[split:]), blinks - 1)
    else:
        num = solve(stone * 2024, blinks - 1)
    cache[(stone, blinks)] = num
    return num

with open('data/11-Dec.txt') as f:
    stones = [int(x) for x in f.read().split()]

cache = {}

print(f'Part 1: {sum(solve(stone, 25) for stone in stones)}')
print(f'Part 2: {sum(solve(stone, 75) for stone in stones)}')