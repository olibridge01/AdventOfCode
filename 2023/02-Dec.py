import numpy as np
import re

# Set maximum ball numbers for Part 1
max_red = 12
max_green = 13
max_blue = 14

def get_min_ball_colors(filename: str) -> list:
    """Get minimum possible ball numbers for each game"""
    min_balls = []

    with open(filename, 'r') as f:
        for line in f:
            # Edit the line 
            line = re.split(': |; |, | ', line.strip())[2:]
            
            # Get lists of red, green, blue draw numbers
            reds = [int(line[i-1]) for i, element in enumerate(line) if element == 'red']
            greens = [int(line[i-1]) for i, element in enumerate(line) if element == 'green']
            blues = [int(line[i-1]) for i, element in enumerate(line) if element == 'blue']

            # Minimum possible ball numbers are the maximum of each color observed
            min_balls.append((max(reds), max(greens), max(blues)))
    
    return min_balls

def get_id_sum(min_balls: list, max_red: int, max_green: int, max_blue: int) -> int:
    """Get sum of IDs of possible games given maximum ball numbers"""
    id_sum = 0

    for i, ball in enumerate(min_balls):
        if ball[0] <= max_red and ball[1] <= max_green and ball[2] <= max_blue:
            # print(i+1, ball)
            id_sum += i + 1

    return id_sum

def get_prod_sum(min_balls: list) -> int:
        """Get sum of products of minimum possible ball numbers for each game"""
        prod_sum = 0
    
        for i, ball in enumerate(min_balls):
            prod_sum += np.prod(ball)
    
        return prod_sum

# Compute solutions
min_balls = get_min_ball_colors('data/02-Dec.txt')
id_sum = get_id_sum(min_balls, max_red, max_green, max_blue) # Part 1
prod_sum = get_prod_sum(min_balls) # Part 2

print(f'Part 1: {id_sum}')
print(f'Part 2: {prod_sum}')