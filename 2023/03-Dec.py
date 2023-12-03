import numpy as np
import re

def get_numbers(data):
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

def get_search_ranges(number, data):
    """Get range of indices to search over for each number"""
    # i_range - vertical
    if number[1] == 0:
        i_range = np.arange(0, 2)
    elif number[1] + 1 == len(data):
        i_range = np.arange(number[1] - 1, number[1] + 1)
    else:
        i_range = np.arange(number[1] - 1, number[1] + 2)

    # j_range - horizontal
    if number[2] == 0:
        j_range = np.arange(0, len(number[0]) + 1)
    elif number[2] + len(number[0]) == len(data[0]):
        j_range = np.arange(number[2] - 1, number[2] + len(number[0]))
    else:
        j_range = np.arange(number[2] - 1, number[2] + len(number[0]) + 1)

    return i_range, j_range

def get_sum_part_numbers(data):
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
        i_range, j_range = get_search_ranges(number, data)
        ij_range = [(i,j) for i in i_range for j in j_range]
        for i, j in ij_range:
            if data[i][j] in data_chars:
                sum_part_numbers += int(number[0])
                if data[i][j] == '*':
                    if (i, j) in gears:
                        gears[(i, j)].append(int(number[0]))
                    else:
                        gears[(i, j)] = [int(number[0])]
                break
    
    for gear in gears:
        if len(gears[gear]) == 2:
            sum_gear_numbers += np.prod(gears[gear])
    
    return sum_part_numbers, sum_gear_numbers

data = np.loadtxt('data/03-Dec.txt', dtype=str, comments=None)
sum, gears = get_sum_part_numbers(data)

print(f'Part 1: {sum}')
print(f'Part 2: {gears}')                