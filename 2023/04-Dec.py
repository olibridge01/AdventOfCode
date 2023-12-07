import numpy as np
import re

def get_points(filename: str) -> tuple:
    """Get total points and sum of cards won from file"""
    with open (filename, 'r') as f:
        total_points = 0
        # Get number of lines in file
        n_lines = len(f.readlines())
        cards_won = np.ones(n_lines)

        # Reset file pointer
        f.seek(0)

        for i, card in enumerate(f):
            card = card.strip()
            card = re.split(r'\s+', card)

            divider = card.index('|')
            winning_numbers = card[2:divider]
            my_numbers = card[divider + 1:]
            
            card_score, n_winners = 0, 0 # Reset card score and no. winners

            for number in my_numbers:
                if number in winning_numbers:
                    n_winners += 1
                    if card_score == 0:
                        card_score += 1
                    else:
                        card_score *= 2
            cards_won[i + 1:i + n_winners + 1] += cards_won[i]
            total_points += card_score
    
    total_cards_won = np.sum(cards_won).astype(int)
    return total_points, total_cards_won

total_points, total_cards_won = get_points('data/04-Dec.txt')

print(f'Part 1: {total_points}')
print(f'Part 2: {total_cards_won}')