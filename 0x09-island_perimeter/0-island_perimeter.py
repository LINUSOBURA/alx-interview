#!/usr/bin/python3
"""Perimeter Island
Returns the perimeter of an island described in grid"""


def island_perimeter(grid):
    """Returns the perimeter of an island described in grid"""
    # Initialize the perimeter counter
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land
            if grid[r][c] == 1:
                """Check the four possible sides (up, down,
                left, right) Add to perimeter if the neighboring
                cell is water or out of bounds"""
                if r == 0 or grid[r - 1][c] == 0:  # Check above
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Check below
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Check left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
