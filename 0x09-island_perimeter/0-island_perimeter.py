#!/usr/bin/python3


""" This module contain te function that
calculate the perimeter of the island
"""


def island_perimeter(grid):
    """this function returns the perimeter of the only island described by grid"""
    perimeter = 0
    grid_len = len(grid)

    # Find the location of the only island
    island_row = None
    island_col = None
    for row in range(grid_len):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                island_row = row
                island_col = col
                break
        if island_row is not None:
            break

    # Traverse the island and count the perimeter
    stack = [(island_row, island_col)]
    visited = set()
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if row == 0 or grid[row-1][col] == 0:
            perimeter += 1
        if col == 0 or grid[row][col-1] == 0:
            perimeter += 1
        if row == grid_len-1 or grid[row+1][col] == 0:
            perimeter += 1
        if col == len(grid[row])-1 or grid[row][col+1] == 0:
            perimeter += 1
        if row > 0 and grid[row-1][col] == 1:
            stack.append((row-1, col))
        if col > 0 and grid[row][col-1] == 1:
            stack.append((row, col-1))
        if row < grid_len-1 and grid[row+1][col] == 1:
            stack.append((row+1, col))
        if col < len(grid[row])-1 and grid[row][col+1] == 1:
            stack.append((row, col+1))

    return perimeter
