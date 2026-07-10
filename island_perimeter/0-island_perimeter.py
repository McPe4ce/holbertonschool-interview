#!/usr/bin/python3

def island_perimeter(grid):

    peri_counter = 0

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row] == 1 and grid[row][col] == 1:
                if grid[row + 1][col] == 0:
                    peri_counter += 1
                if grid[row - 1][col] == 0:
                    peri_counter += 1
                if grid[row][col - 1] == 0:
                    peri_counter += 1
                if grid[row][col + 1] == 0:
                    peri_counter += 1

            elif grid[row][col] == 1:
                if grid[row + 1][col] == 0:
                    peri_counter += 1
                if grid[row][col - 1] == 0:
                    peri_counter += 1
                if grid[row][col + 1] == 0:
                    peri_counter += 1
                if grid[row - 1][col] == 0:
                    peri_counter += 1
    return peri_counter
