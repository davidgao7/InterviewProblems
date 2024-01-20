# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum jump
# length at that position.
#
#  Return true if you can reach the last index, or false otherwise.
#
#
#  Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
#  Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 10⁵
#
#
#  Related Topics Array Dynamic Programming Greedy 👍 18571 👎 1126
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True  # already at the last index

        cover = 0
        for i in range(len(nums)):
            # only care for how far we can reach
            # 2. greedy get the current max cover
            if i<=cover:
                cover = max(cover, i+nums[i])
                # 3. if we can reach the final index, return True, no matter where we are currently
                if cover>=len(nums)-1: return True

        # 4. if we cannot reach the current index, return False
        return False
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4])==True)