# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#  Example 2:
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
#  Example 3:
#  Input: nums = [1]
# Output: [[1]]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  All the integers of nums are unique.
#
#
#  Related Topics Array Backtracking 👍 18447 👎 300
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # similar to previous find subsequences, permutation allow same elements
        used = [False] * len(nums)  # track which element has been chosen
        result = []
        self.backtracking(used,[], nums,  result)
        return result

    def backtracking(self, used: List, path: List, nums:List[int], result: List[List[int]]):

        # stop condition
        if len(path) == len(nums):
            result.append(path[:])
            return  # get one path, return to another backtracking

        for i in range(0, len(nums)):  # NOTE: only difference is this loop:
            # since we are getting permutation, order matters, no need to check if choose previous number,
            # only need to check if this number has already chosen in this path
            if used[i]: continue  # choose another option
            used[i] = True
            # collect element to from path
            path.append(nums[i])
            # choose another element
            self.backtracking(used, path, nums, result)
            used[i] = False
            path.pop(-1)

# leetcode submit region end(Prohibit modification and deletion)
