import re

def solve(data: str, p1: bool = True) -> int:
    pattern1 = 'mul\((\d+),(\d+)\)'
    pattern2 = 'do\(\)|don\'t\(\)'

    if p1:
        nums = re.findall(pattern1, data)
    else:
        matches = re.finditer(re.compile(pattern1 + '|' + pattern2), data)

        do, nums = True, []
        for m in matches:
            if m.group() == 'do()':
                do = True
            elif m.group() == 'don\'t()':
                do = False
            elif do:
                nums.append(m.groups())
    
    return sum(int(a) * int(b) for a, b in nums)

with open('data/03-Dec.txt') as f:
    data = ''.join(f.read().splitlines())

print(solve(data, p1=True)) 
print(solve(data, p1=False))  