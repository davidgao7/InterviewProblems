# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum
# to target.
#
#  Each number in candidates may only be used once in the combination.
#
#  Note: The solution set must not contain duplicate combinations.
#
#
#  Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
#  Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
#  Constraints:
#
#
#  1 <= candidates.length <= 100
#  1 <= candidates[i] <= 50
#  1 <= target <= 30
#
#
#  Related Topics Array Backtracking 👍 10005 👎 265
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        used = [False] * (len(candidates) + 1)
        candidates.sort() # need sort to purnue
        self.backtrack(candidates, target, 0, 0, path, used, result)
        return result

    def backtrack(self, nums, targetSum, sum, start_index, path, used, result):
        """
        :param nums:
        :param targetSum:
        :param sum: current sum
        :param start_index: track which branch, prevent overlap
        :param path: current path
        :param used: current level path used
        :param result: final result paths
        :return:
        """

        if sum == targetSum:
            # find the target combination
            result.append(path[:])
            return

        for i in range(start_index, len(nums)):
            if sum + nums[i] > targetSum:
                break
            if (
                i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False
            ):  # since nums[i] == nums[i - 1], two numbers # are equal, and this value hasn't been used, which is a overlapped value
                continue
            path.append(nums[i])
            sum += nums[i]
            used[i] = True  # check if used or not
            self.backtrack(nums, targetSum, sum, i + 1, path, used, result)
            # backtrack
            path.pop(-1)
            sum -= nums[i]
            used[i] = False


# leetcode submit region end(Prohibit modification and deletion)
