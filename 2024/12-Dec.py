from typing import List, Tuple, Set

def dfs(grid: List[str], row: int, col: int, plot_type: str, visited: Set[Tuple[int, int]]) -> None:
    visited.add((row, col))

    if (row, col - 1) not in visited and grid[row][col - 1] == plot_type:
        dfs(grid, row, col - 1, plot_type, visited)
    if (row, col + 1) not in visited and grid[row][col + 1] == plot_type:
        dfs(grid, row, col + 1, plot_type, visited)
    if (row - 1, col) not in visited and grid[row - 1][col] == plot_type:
        dfs(grid, row - 1, col, plot_type, visited)
    if (row + 1, col) not in visited and grid[row + 1][col] == plot_type:
        dfs(grid, row + 1, col, plot_type, visited)

def fence_cost(grid: List[str], region: Set[Tuple[int, int]], plant: str) -> Tuple[int, int]:
    perimeter, shared_borders = 0, 0

    for row, col in region:

        if grid[row - 1][col] != plant:
            perimeter += 1
      
            if grid[row][col - 1] == plant and grid[row - 1][col - 1] != plant:
                shared_borders += 1
      
        if grid[row + 1][col] != plant:
            perimeter += 1
           
            if grid[row][col - 1] == plant and grid[row + 1][col - 1] != plant:
                shared_borders += 1
      
        if grid[row][col - 1] != plant:
            perimeter += 1
  
            if grid[row - 1][col] == plant and grid[row - 1][col - 1] != plant:
                shared_borders += 1

        if grid[row][col + 1] != plant:
            perimeter += 1
            
            if grid[row - 1][col] == plant and grid[row - 1][col + 1] != plant:
                shared_borders += 1

    return len(region) * perimeter, len(region) * (perimeter - shared_borders)

with open('data/12-Dec.txt', "rt") as f:
    grid = [line.strip() + "." for line in f]
    grid.append("." * len(grid[0]))

pos = {(row, col) for row in range(len(grid) - 1) for col in range(len(grid[0]) - 1)}
tot_p1, tot_p2 = 0, 0

while pos:
    start = pos.pop()
    plant_type = grid[start[0]][start[1]]
    region = set()
    dfs(grid, start[0], start[1], plant_type, region)
    p1, p2 = fence_cost(grid, region, plant_type)
    tot_p1 += p1
    tot_p2 += p2
    pos -= region

print(f"Part 1: {tot_p1}")
print(f"Part 2: {tot_p2}")