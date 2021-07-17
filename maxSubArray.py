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
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # inital need to consider negative case
        max_sum = -1 * math.inf

        # base case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(max(nums[0], nums[0] + nums[1]), max(nums[1], nums[0] + nums[1]))

        # general case 1: given list
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                # dynamic programming
                max_sum = max(max_sum, sum(nums[i:j]))  # index i to index j

        # compare with whole list sum
        max_sum = max(max_sum, sum(nums))

        # general case 2: reversed given list
        nums.reverse()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                # dynamic programming
                max_sum = max(max_sum, sum(nums[i:j]))

        return max_sum


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
input_array = [2, -1, 1, 1]
maximum = s.maxSubArray(input_array)
print('maximum sum of sub array %s: %d' % ([2, -1, 1, 1], maximum))
