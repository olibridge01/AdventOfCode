def get_score(round: str, part1: bool = False) -> int:
    """Get score for one round of rock-paper-scissors"""
    opp_move = 'ABC'.index(round.split(' ')[0]) # Get opponent's move
    my_move = 'XYZ'.index(round.split(' ')[1]) # Get my move

    # Get score for this round, for part 1 or part 2
    move_score = my_move if part1 else (my_move + opp_move + 2) % 3
    outcome = (my_move - opp_move + 1) % 3 if part1 else my_move
    return (move_score + 1) + (3 * outcome)

with open('data/02-Dec.txt', 'r') as f:
    data = f.read().splitlines()
    scores1 = [get_score(round, part1=True) for round in data]
    scores2 = [get_score(round, part1=False) for round in data]

print(f"Part 1: {sum(scores1)}")
print(f"Part 2: {sum(scores2)}")