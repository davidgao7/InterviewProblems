from typing import List


# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
#
#
#  示例：
#
#  输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#
#
#
#
#  提示：
#
#
#  1 <= len(A), len(B) <= 1000
#  0 <= A[i], B[i] < 100
#
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希
#  👍 503 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2) + 1)  # 用来放结果
        result = 0
        for i in range(1, len(nums1) + 1):  # 前窗口
            for j in range(len(nums2), 0, -1):
                if nums1[i - 1] == nums2[j - 1]:  # 前 VS 后
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0  # 不相同就从头开始
                result = max(result, dp[j])
        return result


# from: leetcode-master

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
A = [57,85,85,5,28]
B = [82,85,85,32,50]
print(solution.findLength(A, B))
# find longest common subarray
