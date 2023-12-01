import numpy as np
import re

# Load data
data = np.loadtxt('01-Dec.txt', dtype=str)

# ----------------------Part 1----------------------------

def get_calibration_val(element):
    """Get calibration value from element in data"""

    # Get all the numbers from element
    numbers = []
    for char in element:
        if char.isdigit():
            numbers.append(char)

    # Get first and last element in numbers
    calibration_val = ''
    for i in [0, -1]:
        calibration_val += numbers[i]
    
    # Return calibration value as int
    return int(calibration_val)

# Compute total calibration
total_calibration = 0
for element in data:
    total_calibration += get_calibration_val(element)

print(total_calibration)

# ----------------------Part 2----------------------------

letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_new_calibration_val(element, letter_digits):
    """Get calibration value taking into account numbers as words"""

    # Get all numbers from element
    numbers = []
    for idx, char in enumerate(element):
        if char.isdigit():
            numbers.append((idx, char))
    
    # Find indices of all occurrences of word numbers
    for number in letter_digits:
        for m in re.finditer(number, element):
            numbers.append((m.start(), str(letter_digits.index(number)+1)))

    # Sort found numbers
    numbers = sorted(numbers, key=lambda x: x[0])

    # Get first and last found number
    calibration_val = ''
    for i in [0, -1]:
        calibration_val += numbers[i][1]
    
    # Return calibration value as int
    return int(calibration_val)

# Compute total calibration
total_calibration_2 = 0
for element in data:
    total_calibration_2 += get_new_calibration_val(element, letter_digits)

print(total_calibration_2)