# Given a circular integer array nums (i.e., the next element of nums[nums.
# length - 1] is nums[0]), return the next greater number for every element in nums.
#
#  The next greater number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly to find
# its next greater number. If it doesn't exist, return -1 for this number.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also 2
# .
#
#
#  Example 2:
#
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁹ <= nums[i] <= 10⁹
#
#
#  Related Topics Array Stack Monotonic Stack 👍 7681 👎 188
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums) * 2):  # circular loop, so we need to loop twice
            # everytime we find a greater number, we pop the index from the stack and update the result
            while stack and nums[i % len(nums)] > nums[stack[-1]]:  # i % len(nums) to get the index in the original list
                result[stack.pop()] = nums[i % len(nums)]
            stack.append(i % len(nums))
        return result

# leetcode submit region end(Prohibit modification and deletion)
