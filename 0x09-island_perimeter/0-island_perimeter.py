#!/usr/bin/python3
"""interview question island_perimeter
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid
    Args:
        grid: list of list of integers
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if we find land
            if grid[i][j] == 1:
                # check top side
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom side
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # check left side
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check right side
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
