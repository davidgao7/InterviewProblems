# Given an integer array nums, return all the different possible non-decreasing
# subsequences of the given array with at least two elements. You may return the
# answer in any order.
#
#
#  Example 1:
#
#
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
#  Example 2:
#
#
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 15
#  -100 <= nums[i] <= 100
#
#
#  Related Topics Array Hash Table Backtracking Bit Manipulation 👍 3566 👎 226
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    class Solution:
        def findSubsequences(self, nums: List[int]) -> List[List[int]]:
            path = []
            result = []
            self.backtracking(nums, path, 0, result)
            return result

        def backtracking(
            self,
            nums: List[int],
            path: List[int],
            start_index: int,
            result: List[List[int]],
        ):

            if len(path) > 1:
                result.append(path[:])

            # set to record if number has been chosen
            used = set()

            # for each branch
            for i in range(start_index, len(nums)):

                # if the current path we chose less than the last path in the result,
                # 1. since we need increasing order, this can't be done,
                # 2. also we cannot use the element we chose before
                if len(path) > 0 and nums[i] < path[-1] or nums[i] in used:
                    # cut the route
                    continue

                # record the used num
                used.add(nums[i])
                # add path to subset
                path.append(nums[i])
                # go to next node
                self.backtracking(nums, path, i + 1, result)
                path.pop()
                # only record current recursive level if use a element twice


# leetcode submit region end(Prohibit modification and deletion)
