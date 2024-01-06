# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers
# sum to target. You may return the combinations in any order.
#
#  The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
#
#  The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.
#
#
#  Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
#
#  Example 2:
#
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#
#  Example 3:
#
#
# Input: candidates = [2], target = 1
# Output: []
#
#
#
#  Constraints:
#
#
#  1 <= candidates.length <= 30
#  2 <= candidates[i] <= 40
#  All elements of candidates are distinct.
#  1 <= target <= 40
#
#
#  Related Topics Array Backtracking 👍 18097 👎 375
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        self.backtrack(candidates, target, 0, result, 0, path)
        return result

    def backtrack(self, candidates: List[int], target: int, sum:int,result:List, start_index:int,path:List):

        if sum>target: return  # no need to keep searching
        if sum==target:
            result.append(path[:])
            return # no need to keep searching

        for i in range(start_index,len(candidates)):
            # if sum > target, can return and find another path
            if sum + candidates[i] > target:
                continue # continue to the next branch for next number

            # add 1 candidate
            path.append(candidates[i])
            sum+=candidates[i]

            # backtracking
            self.backtrack(candidates, target, sum, result, i, path)

            # pop and subtrack this path
            sum-=candidates[i]
            path.pop(-1)
# leetcode submit region end(Prohibit modification and deletion)
