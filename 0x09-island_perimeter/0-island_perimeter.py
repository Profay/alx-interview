#!/usr/bin/env python3
""" This module contain te function that
calculate the perimeter of the island
"""

def island_perimeter(grid):
    """ Calculate the perimeter of the island
    """
    perimeter = 0
    grid_length = len(grid)
    for row in range(grid_length):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if grid[row - 1][col] == 0 or row - 1 < 0:
                    perimeter += 1
                if grid[row + 1][col] == 0 or row + 1 >= grid_length:
                    perimeter += 1
                if grid[row][col + 1] == 0 or col + 1 >= len(grid[row]):
                    perimeter += 1
                if grid[row][col - 1] == 0 or col - 1 < 0:
                    perimeter += 1
    return perimeter
