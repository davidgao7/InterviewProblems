# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
#
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
#
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
#
#
#
#  示例 1：
#
#
# 输入：A = [[0,1],[1,0]]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#
#
#  示例 3：
#
#
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
#
#
#
#  提示：
#
#
#  2 <= A.length == A[0].length <= 100
#  A[i][j] == 0 或 A[i][j] == 1
#
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 185 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
"""
多起點，多終點
起點：用DFS找
終點：用BFS找
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(grid: List[List[int]], x: int, y: int, queue: List):
            # 如果没有visit，标记为visit，接着想四周阔
            if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[x]) - 1 and grid[x][y] != 2:
                grid[x][y] = 2  # 2: visited
                queue.append([x, y]) # add visited island to queue

                # 向四个方向延伸找终点
                dfs(grid, x - 1, y, queue)  # up
                dfs(grid, x, y - 1, queue)  # left
                dfs(grid, x + 1, y, queue)  # down
                dfs(grid, x, y + 1, queue)  # right

        # 1. 找到这两座岛(dfs)
        # 2. 选择一座，将它不断向外扩展一圈(bfs)已知领域，直到发现了另一座岛
        # 深度优先搜索grid 中的 1，再从source中的所有位置开始进行深度优先搜索
        # 在向外延伸时，用广度优先搜索
        queue = []
        # 找到其中一个小岛
        found = False
        for x, row in len(grid), grid:
            for y, space in len(row), row:
                if space:  # 找到一个小岛就退出
                    dfs(grid, x, y, queue)
                    found = True

        steps = 0
        directions = [0,1,0,-1,0]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
A = [
    [0, 1],
    [1, 0]
]
minimum_zero_flipped = s.shortestBridge(A)
print(minimum_zero_flipped)
