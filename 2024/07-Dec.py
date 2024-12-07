from operator import add, mul

def concat(a: int, b: int) -> int: 
    return int(f"{a}{b}")

def solve(nums: list[int], ops: list[callable]) -> int:
    if len(nums) == 2:
        return nums[0] == nums[1] # Base case

    tot, a, b, *rest = nums
    for op in ops:
        if solve([tot, op(a, b)] + rest, ops): # Recursively try all combinations
            return tot 
    return 0

with open('data/07-Dec.txt') as f:
    data = [list(map(int, line.replace(':','').split())) for line in f.readlines()]

print(f'Part 1: {sum(solve(nums, ops=[add, mul]) for nums in data)}')
print(f'Part 2: {sum(solve(nums, ops=[add, mul, concat]) for nums in data)}')