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
        # base case
        if len(nums) == 0:
            return 0

        # dp[i]: 以 nums[i] 结尾的sublist sum
        dp = [0] * len(nums)
        max_sum = nums[0]
        for i in range(0, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 计算是否还有更大的最大值
            max_sum = max(max_sum, dp[i])  # update 到更大的最大值

        return max_sum


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
input_array = [2, -1, 1, 1]
maximum = s.maxSubArray(input_array)
print('maximum sum of sub array %s: %d' % ([2, -1, 1, 1], maximum))
