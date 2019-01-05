"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""


# -2 is the obstacle
# -1 is the target
def robot_in_a_grid(grid, row, col, row_len, col_len, count):
    if grid[row][col] != -2:
        if grid[row][col] != -1:
            grid[row][col] = count
            if row + 1 < row_len:
                robot_in_a_grid(grid.copy(), row + 1, col, row_len, col_len, count+1)
            if col + 1 < col_len:
                robot_in_a_grid(grid.copy(), row, col + 1, row_len, col_len, count+1)
        else:
            return True


_grid = []
r = 9
c = 6
for i in range(r):
    _grid.append([0]*c)
_grid[4][4] = -1

_grid[0][2] = -2
_grid[1][2] = -2
_grid[3][2] = -2
_grid[3][3] = -2
_grid[5][2] = -2
_grid[6][2] = -2

robot_in_a_grid(_grid, 0, 1, r, c, 0)

for i in range(r):
    for j in range(c):
        print(str(_grid[i][j]), end='\t\t')
    print()