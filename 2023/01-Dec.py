import numpy as np
import re

# Load data
data = np.loadtxt('data/01-Dec.txt', dtype=str)

letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_calibration_val(element: str, letter_digits: list = None) -> int:
    """Get calibration value for an element in data"""

    # Get all numbers from element
    numbers = []
    for idx, char in enumerate(element):
        if char.isdigit():
            numbers.append((idx, char))
    
    # Find indices of all occurrences of word numbers
    if letter_digits is not None:
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

# Compute total calibration for Parts 1 and 2
total_calibration_part1 = 0
total_calibration_part2 = 0

for element in data:
    total_calibration_part1 += get_calibration_val(element)
    total_calibration_part2 += get_calibration_val(element, letter_digits)

print(f'Part 1: {total_calibration_part1}')
print(f'Part 2: {total_calibration_part2}')