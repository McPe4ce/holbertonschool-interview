#!/usr/bin/python3
"""Module that determines the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Args:
        grid (list): List of lists of integers, where 0 represents
            water and 1 represents land, describing a grid-shaped
            island (there is exactly one island, with no lakes).

    Returns:
        int: The perimeter of the island.
    """
    peri_counter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    peri_counter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    peri_counter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    peri_counter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    peri_counter += 1
    return peri_counter
