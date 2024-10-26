"""
Longest Increasing Path in Matrix
You are given a 2-D grid of integers matrix, where each integer is greater
than or equal to 0.

Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or
vertically. You may not move diagonally.

Example 1:

Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]

Output: 4
Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

Example 2:



Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]

Output: 7
Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].

Constraints:

1 <= matrix.length, matrix[i].length <= 100
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r,c) -> LIP starting at (r,c)

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:  # memoization, no need to recompute
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(dp.values())
