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
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        :param matrix: 2d array/list
        :param target: number to find
        :return: can find number or not

        I'm going to try the two ptr method similar to find median in 2 array, binary search but now theres one 2d list
        idea: binary search array[i][0] to find possible row, then binary search this row
        time complexity: O(logn)+O(logn) = O(logn)
        """
        flatten_list = [e for row in matrix for e in row]
        if len(flatten_list) == 0:
            return False
        if len(flatten_list) == 1:
            if flatten_list[0] == target:
                return True
            else:
                return False

        first_elements = [arr[0] for arr in matrix]
        pivot = len(first_elements) // 2
        vertical_mid = first_elements[pivot]

        if vertical_mid == target:
            return True

        # if beginning of row < target, search this row
        if vertical_mid < target:
            # edge case, one element in  sub array
            if len(matrix[pivot]) == 1:
                return self.findNumberIn2DArray(matrix[pivot:], target)

            in_row = self.binary_search_1D(matrix[pivot], target)

            if in_row:
                return True
            else:
                return self.findNumberIn2DArray(matrix[:pivot], target) or self.findNumberIn2DArray(matrix[pivot:],
                                                                                                    target)
        # if beginning of row > target or target not in current row, need search sub 2d array above this row
        else:
            return self.findNumberIn2DArray(matrix[0:pivot], target)

    def binary_search_1D(self, arr: List[int], target: int) -> bool:

        if not arr:
            return False
        if len(arr) == 1 and arr[0] != target:
            return False

        pivot = len(arr) // 2

        if arr[pivot] == target:
            return True
        if arr[pivot] < target:
            return self.binary_search_1D(arr[pivot:], target)
        else:
            return self.binary_search_1D(arr[:pivot], target)


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
array = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target_1 = 20
print(solution.findNumberIn2DArray(array, target_1))
