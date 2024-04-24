# # You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
# Accepted
# 851.3K
# Submissions
# 1.2M
# Acceptance Rate
# 72.0%
#
#
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # overall approach: using dfs to try every point in the grid, and find the maximum area of an island
        # 1. if the grid is empty, return 0
        if not grid:
            return 0

        # 2. perform dfs on the grid
        rows, cols = len(grid), len(grid[0])

        # mark visited cells
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # initialze the expansion for islands stack
        max_area = 0

        # dfs to visit a island, get the area
        def dfs(r, c):
            # if we reach end of the world, or the cell is water, or invalid cell, or visited,
            # return 0
            if (
                (r < 0 or c < 0)
                or (r >= rows or c >= cols)
                or (grid[r][c] == 0)
                or visited[r][c]
            ):
                # so we didn't find the island, return 0
                return 0

            # else it's a valid island cell, we visit it, mark it, then try to explore its
            # neighbors
            visited[r][c] = True
            # calculate the area of the island
            # so the current position we just visited, its area is 1
            # we add this island to our big island, then consider the next neighbor unit island
            # we can go 4 directions: up, right, down, left
            # current island area = 1
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        # iterate over the grid, see if can form island when take each cell as starting point
        # find the max area of the island
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r, c))

        return max_area
