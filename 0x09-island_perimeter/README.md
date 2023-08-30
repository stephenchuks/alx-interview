# Island Perimeter

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Island Perimeter**<br/>[0-island_perimeter.py](0-island_perimeter.py) contains a module with a function having the prototype `function def island_perimeter(grid):`, which returns the perimeter of the island described in `grid`, with the following requirements:
  + `grid` is a list of list of integers:
    + 0 represents water.
    + 1 represents land.
    + Each cell is square, with a side length of 1.
    + Cells are connected horizontally/vertically (not diagonally).
    + `grid` is rectangular, with its width and height not exceeding 100.
  + The grid is completely surrounded by water.
  + There is only one island (or nothing).
  + The island doesn't have "lakes' (water inside that isn't connected to the water surrounding the island).

### Hints:
let's break this problem down. 

To calculate the perimeter of the island, we need to understand that the perimeter is defined as the number of edges (the sides of the squares that make up the island) that are exposed to water. Therefore, to solve this problem, we will need to iterate over each cell in the grid, find the cells that contain land, and check if any of their adjacent cells are water. If an adjacent cell is water, then the edge between the land and water is exposed, and we can increase the perimeter count. 
