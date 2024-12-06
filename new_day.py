import argparse
import requests
from pathlib import Path

AOC_SESSION = 'SESSION GOES HERE'
TEMPLATE = """
with open('data/{day:02d}-Dec.txt') as f:
    data = f.read().splitlines()
"""

def get_puzzle_input(year, day):
    """Fetch puzzle input for a given day."""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": AOC_SESSION}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()  # Raise error for bad responses
    return response.text.strip()

def generate_files(year, day):
    """Generate input.txt and solution.py for the given day."""
    # Create directory for the puzzle input
    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)
    
    # Fetch and save puzzle input
    input_path = data_dir / f"{day:02d}-Dec.txt"
    if not input_path.exists():
        print(f"Fetching input for Day {day}...")
        puzzle_input = get_puzzle_input(year, day)
        input_path.write_text(puzzle_input)
        print(f"Saved input to {input_path}")
    else:
        print(f"Input for Day {day} already exists.")

    # Generate solution template
    solution_path = BASE_DIR / f"{day:02d}-Dec.py"
    if not solution_path.exists():
        print(f"Generating solution template for Day {day}...")
        solution_path.write_text(TEMPLATE.format(day=day))
        print(f"Saved template to {solution_path}")
    else:
        print(f"Solution template for Day {day} already exists.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Setup files for a new day of Advent of Code.")
    parser.add_argument("day", type=int, help="Day")
    parser.add_argument("year", type=int, help="Year")
    args = parser.parse_args()

    BASE_DIR = Path(f'{args.year}')
    BASE_DIR.mkdir(exist_ok=True)
    generate_files(args.year, args.day)