# Given an integer array nums and an integer k, modify the array in the
# following way:
#
#
#  choose an index i and replace nums[i] with -nums[i].
#
#
#  You should apply this process exactly k times. You may choose the same index
# i multiple times.
#
#  Return the largest possible sum of the array after modifying it in this way.
#
#
#
#  Example 1:
#
#
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].
#
#
#  Example 2:
#
#
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
#
#
#  Example 3:
#
#
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -100 <= nums[i] <= 100
#  1 <= k <= 10⁴
#
#
#  Related Topics Array Greedy Sorting 👍 1495 👎 109

from functools import cmp_to_key
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # python sort list custom comparator(according to its absolute value descending order)
        nums.sort(key=cmp_to_key(lambda x, y:-1 if abs(x) > abs(y) else 0))

        for i in range(len(nums)):
            # since we already sort according to its absolute value,
            # we can just flip the sign of the number
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # if k still > 0, we can keep flipping the sign of the smallest number
        # until k is exhausted
        if k % 2 == 1:
            nums[-1] = -nums[-1]
            k -= 1

        return sum(nums)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    nums = [4, 2, 3]
    k = 1
    print(Solution().largestSumAfterKNegations(nums, k))
