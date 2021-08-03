from typing import List


# 在一个 n * m 的二维数组中，【每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。】请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。
#
#
#
#  示例:
#
#  现有矩阵 matrix 如下：
#
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#
#
#
#  限制：
#
#  0 <= n <= 1000
#
#  0 <= m <= 1000
#
#
#
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
#  Related Topics 数组 二分查找 分治 矩阵
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flatten(matrix):
        flatten = []
        if matrix == [[]]:
            return []
        else:
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    flatten.append(matrix[i][j])

            return flatten

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        # base case
        if len(Solution.flatten(matrix)) == 0:  # 没元素
            return False

        # the most right most up number is the mid
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:  # 限制 j
            mid = matrix[i][j]
            if mid == target:
                return True
            if mid < target:
                i += 1
            if mid > target:
                j -= 1
            # print(i)
            # print(j)
            # print(" ")
        return False


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
array = [[-5]]
# [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target_1 = -10
print(solution.findNumberIn2DArray(array, target_1))
