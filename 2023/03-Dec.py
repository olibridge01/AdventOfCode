import numpy as np
import re

def add_border(data: list) -> list:
    """Add border of '.'s to data"""
    for i, line in enumerate(data):
        data[i] = '.' + line + '.'
    data.insert(0, '.' * len(data[0]))
    data.append('.' * len(data[0]))
    return data

def get_numbers(data: list) -> list:
    """Get indices of all numbers present in data"""
    numbers = []
    for i, line in enumerate(data):
        seen_number = False
        for j, char in enumerate(line):
            # Check for digits and update number list accordingly
            if char.isdigit() and not seen_number:
                current_number = char
                current_number_i = i
                current_number_j = j
                seen_number = True
            elif char.isdigit() and seen_number:
                current_number += char
                if j == len(line) - 1:
                    numbers.append((current_number, current_number_i, current_number_j))
            elif not char.isdigit() and seen_number:
                seen_number = False
                numbers.append((current_number, current_number_i, current_number_j))
    return numbers

def get_sum_part_numbers(data: list) -> tuple:
    """Get sum of all part numbers"""

    # Get positions of all numbers in data
    numbers = get_numbers(data)
    sum_part_numbers = 0
    sum_gear_numbers = 0
    gears = {}

    # Get set of symbols in data
    data_chars = set()
    for line in data:
        for char in line:
            if not char.isdigit() and char != '.':
                data_chars.add(char)

    # Get sum of all part numbers
    for number in numbers:
        for i in range(number[1] - 1, number[1] + 2):
            for j in range(number[2] - 1, number[2] + len(number[0]) + 1):
                if data[i][j] in data_chars:
                    sum_part_numbers += int(number[0])
                    if data[i][j] == '*':
                        if (i, j) in gears:
                            gears[(i, j)].append(int(number[0]))
                        else:
                            gears[(i, j)] = [int(number[0])]
                    break
                    
    # Get sum of all gear numbers
    for gear in gears:
        if len(gears[gear]) == 2:
            sum_gear_numbers += np.prod(gears[gear])
    
    return sum_part_numbers, sum_gear_numbers


with open ('data/03-Dec.txt', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

data = add_border(data)
sum, gears = get_sum_part_numbers(data)

print(f'Part 1: {sum}')
print(f'Part 2: {gears}')                