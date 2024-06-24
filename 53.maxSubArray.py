"""
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:

Input: nums = [-1]

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
14151613121117181097861920212223
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        # use dynamic programming to continue update the answer
        res = nums[0] # subarray is non-empty so at least take 1st value
        cur_sum = 0

        for i in range(0, len(nums)):

…
        return res 

--NORMAL--
Accepted

Passed test cases: 19 / 19
You have successfully completed this problem!
"""
# English description is not available for the problem. Please switch to Chinese
# . Related Topics 数组 分治 动态规划
#  👍 322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
# 提示：
#
# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100
# 注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        # use dynamic programming to continue update the answer
        res = nums[0] # subarray is non-empty so at least take 1st value
        cur_sum = 0

        for i in range(0, len(nums)):

            # only keep the positive result         
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
        

            # dp only record max for each sub array end position
            # need overall max
            res = max(res, cur_sum)

        return res



# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
input_array = [2, -1, 1, 1]
maximum = s.maxSubArray(input_array)
print('maximum sum of sub array %s: %d' % ([2, -1, 1, 1], maximum))
