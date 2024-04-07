# Given an integer array nums of unique elements, return all possible subsets (
# the power set).
#
#  The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#  Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#  All the numbers of nums are unique.
#
#
#  Related Topics Array Backtracking Bit Manipulation 👍 16353 👎 248
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        self.backtracking(nums, 0, path, result)
        return result

    # brute force yet most sufficient method
    def backtracking(
        self, nums: List[int], start_index: int, path, result
    ) -> List[List[int]]:
        # store the current path in current recursive
        result.append(path[:])

        if start_index >= len(
            nums
        ):  # the loop won't execute if this satisfies anyway , no need to add
            return

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # use dfs to find the path, backtrack to choose another path
        result = []  # 2d array to store all the subsets
        subset = []  # 1d array to track the current subset

        def dfs(current_index):
            # stop case: if we've reached all the elements in nums, we can stop this dfs,
            # append this path
            if current_index >= len(nums):
                result.append(subset[:])
                return  # exit the current path dfs

            # add the current subset to the result
            subset.append(nums[current_index])
            # choose another path
            dfs(current_index + 1)

            # backtrack, not choose this path
            subset.pop()
            dfs(current_index + 1)

        # start the dfs from the first element
        dfs(0)
        return result


# leetcode submit region end(Prohibit modification and deletion)

#         []
#     1/    \[]
#     [1]    []
#     2/\3       \1
# [1,2]  [1,3]         [1]
# 3/      \2
# [1,3,2]   [1,2]         [1,2]
