"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # bfs
        # as always, we use deque for bfs
        q = deque()
        # track the number of fresh oranges
        fresh = 0
        # track the number of minutes passed
        t = 0

        # iterate through the grid
        # get current state of the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))  # mark the rotten oranges

        # perform bfs
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # while there are fresh oranges and the queue is not empty
        # we can keep bfs update the fresh oranges
        while q and fresh > 0:
            for _ in range(len(q)):
                # get the current rotten orange
                r, c = q.popleft()

                # check the 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # if the next cell is out of bound or the cell is empty or the cell is already rotten
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= len(grid)
                        or nc >= len(grid[0])
                        or grid[nr][nc] != 1
                    ):
                        continue

                    # mark the cell as rotteCOLS
                    grid[nr][nc] = 2

                    fresh -= 1
                    # add the cell to the queue, so we can check the next cell
                    q.append((nr, nc))

            # go to next time t
            t += 1

        # if there are still fresh oranges, return -1
        # otherwise, return the number of minutes passed
        return t if fresh == 0 else -1
