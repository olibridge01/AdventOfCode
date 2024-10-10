with open('data/01-Dec.txt', 'r') as file:
    data = file.read().splitlines()
    data = [int(i) for i in data]

count1 = count2 = 0
for i, num in enumerate(data):
    if i > 0 and data[i] > data[i-1]:
        count1 += 1
    if i > 2 and sum(data[i-2:i+1]) > sum(data[i-3:i]):
        count2 += 1

print(f'Part 1: {count1}')
print(f'Part 2: {count2}')