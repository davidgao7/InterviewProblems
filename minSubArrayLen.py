# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
#
#
#  Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
#  Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
#  Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
#  Constraints:
#
#
#  1 <= target <= 10⁹
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁴
#
#
#
# Follow up: If you have figured out the
# O(n) solution, try coding another solution of which the time complexity is
# O(n log(n)).
#
#  Related Topics Array Binary Search Sliding Window Prefix Sum 👍 11908 👎 366
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # sliding window start position
        right = 0  # window end position
        min_len = float("inf")
        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]

            while current_sum >= target:
                # when the right is the current sum is greater than the target,
                # update minimum len if the len is smaller
                min_len = min(min_len, right - left + 1)
                # start to move left ptr to right to decrease sum
                current_sum -= nums[left]
                left += 1

            right += 1

        return (
            min_len if min_len != float("inf") else 0
        )  # If there is no such subarray, return 0 instead.


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    target = 4
    nums = [1,4,4]
    s = Solution()
    print(s.minSubArrayLen(target, nums))
