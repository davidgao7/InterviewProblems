# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
#  Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#
#  Related Topics Array Backtracking 👍 8291 👎 138
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtracking(nums, used, [], result)
        return result

    def backtracking(
        self, nums: List[int], used: List[int], path: List[int], result: List[List[int]]
    ):

        # reach the leaf
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(0, len(nums)):

            # NOTE: the reason use used[i-1]=False is more efficient
            # is because
            # used[i-1] == True is checking when same level, different branch
            # used[i-1] == False is checking when check parent level this number is chosen or not, same branch
            # while same branch seach is more efficient (dfs), when backtracking goes to different branches, it will
            # have more choices, which cost more time
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False :
                # level check if number is used
                continue  # go to another branch

            if used[i]:
                # cannot choose this number
                continue

            # we can choose this number
            used[i] = True
            # collect element to from path
            path.append(nums[i])
            # choose another element
            self.backtracking(nums, used, path, result)
            used[i] = False
            path.pop(-1)


# leetcode submit region end(Prohibit modification and deletion)
