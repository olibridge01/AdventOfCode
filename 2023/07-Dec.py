def get_rank(hand: str, part1: bool = True) -> list:
    """Get rank of a hand as list of various priority values."""
    # Get unique cards and number of occurrences of each card
    cards = set(hand)
    card_ranks = '23456789TJQKA' if part1 else 'J23456789TQKA'
    n_occur = [hand.count(char) for char in card_ranks]
    
    # Compute the rank list for part 1 or part 2
    if part1:
        rank_list = [5 - len(cards), max(n_occur)]
        rank_list.extend([card_ranks.index(card) for card in hand])
    else:
        if 'J' in cards and len(cards) > 1:
            cards.remove('J')
        jokers = n_occur.pop(0)
        rank_list = [5 - len(cards), max(n_occur) + jokers]

        rank_list.extend([card_ranks.index(card) for card in hand])
    return rank_list

def get_winnings(hands: list, part1: bool = True) -> int:
    """Get winnings for a given hand."""
    # Sort the hands by the rank list given by get_rank()
    hands = sorted(hands, key=lambda x: get_rank(x[0], part1))

    # Compute total winnings
    total_winnings = sum([rank * bid for rank, (_, bid) in enumerate(hands, start=1)])
    return total_winnings

with open('data/07-Dec.txt', 'r') as f:
    data = f.read().splitlines()
    hands = [(line.split()[0], int(line.split()[1])) for line in data]

import time as t
start = t.time()
print(f'Part 1: {get_winnings(hands)}')
print(f'Part 2: {get_winnings(hands, part1=False)}')
end = t.time()
print(f'Runtime: {end - start}')