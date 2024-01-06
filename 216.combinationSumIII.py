# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
#
#
#  Only numbers 1 through 9 are used.
#  Each number is used at most once.
#
#
#  Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any order.
#
#
#  Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
#
#  Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
#
#
#  Example 3:
#
#
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1
# +2+3+4 = 10 and since 10 > 1, there are no valid combination.
#
#
#
#  Constraints:
#
#
#  2 <= k <= 9
#  1 <= n <= 60
#
#
#  Related Topics Array Backtracking 👍 5709 👎 103
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # path = []  # 1d, collect 1 path result
        result = []  # 2d
        self.backtracking(n,k, 0, 1, [], result)
        return result

    def backtracking(self, target_sum, k, current_sum, start_idx, path, result):

        # purnue tree, no need to further try
        if current_sum > target_sum:
            return

        # track each path of the tree
        if len(path) == k:  # if one route depth ==k, can check sum
            if target_sum == current_sum:
                result.append(path[:])  # deep copy
            return  # no need to go deeper since we need only k numbers sum
        # single layer search
        # 9: total 9 numbers, which means 9 options
        # 9- (k-(len(path))) numbers left, also include the last number , so add 1 again
        for i in range(start_idx, 9-(k-(len(path)))+1+1):
            current_sum += i
            path.append(i)  # add path

            self.backtracking(target_sum, k, current_sum, i + 1, path, result)

            # backtrack
            current_sum-=i
            path.pop(-1)


# leetcode submit region end(Prohibit modification and deletion)
