# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # mark visited cells
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # initialze the expansion for islands queue
        queue = deque([])
        # count number of islands
        n_islands = 0

        def bfs(r, c):
            visited[r][c] = True
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                # all the direction to move
                directions = [
                    (0, 1),  # try explore right
                    (0, -1),  # try explore left
                    (1, 0),  # try explore down
                    (-1, 0),  # try explore up
                ]
                for dr, dc in directions:
                    # check the new position is island and not visited
                    # while updated row and col is within the grid
                    if (
                        0 <= row + dr < rows
                        and 0 <= col + dc < cols
                        and grid[row + dr][col + dc] == "1"
                        and not visited[row + dr][col + dc]
                    ):
                        # mark visited and add to queue
                        visited[row + dr][col + dc] = True
                        queue.append((row + dr, col + dc))

        # iterate over the grid, see if can form island when take each cell as starting point
        for r in range(rows):
            for c in range(cols):
                # start point has to be island and not visited
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    n_islands += 1

        return n_islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().numIslands(grid))  # 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))  # 3
