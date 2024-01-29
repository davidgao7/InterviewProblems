# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
#
#
#  Example 1:
#
#
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
#
#  Example 2:
#
#
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
#
#
#
#  Constraints:
#
#
#  1 <= nums1.length, nums2.length <= 1000
#  0 <= nums1[i], nums2[i] <= 100
#
#
#  Related Topics Array Binary Search Dynamic Programming Sliding Window
# Rolling Hash Hash Function 👍 6661 👎 162

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] = max(dp[i-1][j-1] + 1 if nums1[i] == nums2[j] else 0, dp[i-1][j], dp[i][j-1])
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] != nums2[j-1]:
                    continue
                dp[i][j] = dp[i-1][j-1] + 1  # find the common subarray, update the length
                ans = max(ans, dp[i][j])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
