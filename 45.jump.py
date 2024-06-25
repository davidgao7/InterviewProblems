# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
#  Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i + j]
# where:
#
#
#  0 <= j <= nums[i] and
#  i + j < n
#
#
#  Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 1000
#  It's guaranteed that you can reach nums[n - 1].
#
#
#  Related Topics Array Dynamic Programming Greedy 👍 13973 👎 519
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0  # start pt is end pt
        cur_distance = 0  # record the current max distance index
        next_distance = 0  # record the next max distance index
        result = 0  # record the number of jumps

        for i in range(len(nums) - 1):  # we don't need to consider the last index
            next_distance = max(next_distance, i + nums[i])  # take the step or not

            if i == cur_distance:
                # if curr is not the last index, we need to go 1 step further
                result += 1   # 1 more step jump after chosen the optimal step
                cur_distance = next_distance

        return result


# leetcode submit region end(Prohibit modification and deletion)
