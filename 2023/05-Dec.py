import numpy as np

def get_input(filename: str) -> tuple:
    """Get seeds to check and maps to apply from file"""
    with open(filename) as f:
        # Get seeds to be checked
        seeds = [int(a) for a in f.readline().strip().split(' ')[1:]]
        lines = f.readlines()[1:]

        # Convert input to list of maps
        maps = []
        for line in lines:
            if not line[0].isdigit() and line != '\n':    
                current_map = []
            if line[0].isdigit():
                current_map.append([int(a) for a in line.strip().split(' ')])
            if line == '\n' or line == lines[-1]:
                maps.append(current_map)

    return seeds, maps
    
def pointwise_output(seed: int, input: list) -> int:
    """Get output of a seed after applying all maps"""
    for map in input:
        for mapping in map:
            if mapping[1] <= seed <= mapping[1] + mapping[2]:
                seed = mapping[0] + (seed - mapping[1])
                break
    return seed

def splitrange_output(seeds: list, input: list) -> list:
    """Get output ranges of seeds after applying all maps"""
    # Compute seed ranges for Part 2
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    for map in input:
        mapped_ranges = []

        while seed_ranges:
            seed_start, seed_end = seed_ranges.pop()
            mapped = False

            # Apply range splitting logic for each map
            for destination, source, span in map:
                overlap_start = max(seed_start, source)
                overlap_end = min(seed_end, source + span)

                if overlap_start < overlap_end:
                    mapped_ranges.append((destination + overlap_start - source, destination + overlap_end - source))
                    mapped = True

                    # Add remaining parts of seed range back to seed_ranges
                    if seed_start < overlap_start:
                        seed_ranges.append((seed_start, overlap_start))
                    if overlap_end < seed_end:
                        seed_ranges.append((overlap_end, seed_end))
                    break
            
            # If no mapping found, add current seed range to mapped ranges (i.e. it maps to itself)
            if not mapped:
                mapped_ranges.append((seed_start, seed_end))
        
        seed_ranges = mapped_ranges
    
    return seed_ranges

# Compute minimum locations for Parts 1 and 2
seeds, input = get_input('data/05-Dec.txt')

min_loc1 = min([pointwise_output(seed, input) for seed in seeds])
min_loc2 = min(splitrange_output(seeds, input), key=lambda x: x[0])[0]

print(f'Part 1: {min_loc1}')
print(f'Part 2: {min_loc2}')