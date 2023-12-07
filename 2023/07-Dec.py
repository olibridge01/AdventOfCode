def get_rank(hand: str, part1: bool = True) -> list:
    """Get rank of a hand as list of various priority values."""
    # Get unique cards and number of occurrences of each card
    cards = set(hand) 
    n_occur = sorted([hand.count(card) for card in cards], reverse=True)
    
    # Compute the rank list for part 1 or part 2
    if part1:
        card_ranks = dict(zip('23456789TJQKA', range(1, 14))) # Card ranks
        rank_list = [5 - len(cards), max(n_occur)]
        rank_list.extend([card_ranks[card] for card in hand])
    else:
        card_ranks = dict(zip('J23456789TQKA', range(1, 14))) # Modified card ranks
        if 'J' in cards:
            if hand.count('J') == max(n_occur):
                rank_list = [5 - len(cards) + 1, sum(n_occur[:2])] if len(cards) > 1 else [4,5]
            else:
                rank_list = [5 - len(cards) + 1, max(n_occur) + hand.count('J')] if len(cards) > 1 else [4,5]
        else:
            rank_list = [5 - len(cards), max(n_occur)]

        rank_list.extend([card_ranks[card] for card in hand])
    return rank_list

def get_winnings(hands: list, part1: bool = True) -> int:
    """Get winnings for a given hand."""
    # Sort the hands by the rank list given by get_rank()
    hands = sorted(hands, key=lambda x: get_rank(x[0], part1))

    # Compute total winnings
    total_winnings = sum([(i + 1) * hand[1] for i, hand in enumerate(hands)])
    return total_winnings

with open('data/07-Dec.txt', 'r') as f:
    data = f.read().splitlines()
    hands = [(line.split()[0], int(line.split()[1])) for line in data]

print(f'Part 1: {get_winnings(hands)}')
print(f'Part 2: {get_winnings(hands, part1=False)}')