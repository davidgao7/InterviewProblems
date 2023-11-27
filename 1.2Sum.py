# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
#  You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
#  You can return the answer in any order.
#
#
#  Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
#  Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
#  Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 10⁴
#  -10⁹ <= nums[i] <= 10⁹
#  -10⁹ <= target <= 10⁹
#  Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than
# O(n²)
#  time complexity?
#
#  Related Topics Array Hash Table 👍 53269 👎 1760
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for i, v in enumerate(nums):
            # if the supplemental value exists in the records, return records idx and current i
            if target - v in records.keys():
                return [records[target - v], i]
            # else store the value and index
            records[v] = i
        # return [] if no pairs found
        return []


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
