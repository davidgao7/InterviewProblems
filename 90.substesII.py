# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
#  The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
#  Example 1:
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#  Example 2:
#  Input: nums = [0]
# Output: [[],[0]]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#
#
#  Related Topics Array Backtracking Bit Manipulation 👍 9338 👎 278
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = [False] * len(nums)
        # need sort the array before removing duplicates
        nums.sort()
        self.backtracking(nums, 0, path, used, result)
        return result

    def backtracking(
        self, nums: List[int], start_index: int, path, used, result
    ) -> List[List[int]]:
        """
        :param nums: original set
        :param start_index: track which first possible choice of the current subset is
        :param path: track current subset
        :param used: track which number is used, prevent overlapping
        :param result: collection of paths
        :return:
        """
        # store the current path in current recursive
        result.append(path[:])

        if start_index >= len(nums):
            # the loop won't execute if this satisfies anyway , no need to add
            return

        for i in range(start_index, len(nums)):
            # purning for same level

            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i + 1, path, used, result)
            used[i] = False
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)
