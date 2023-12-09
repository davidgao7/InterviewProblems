# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
#  0 <= a, b, c, d < n
#  a, b, c, and d are distinct.
#  nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
#  You may return the answer in any order.
#
#
#  Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
#  Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 200
#  -10⁹ <= nums[i] <= 10⁹
#  -10⁹ <= target <= 10⁹
#
#
#  Related Topics Array Two Pointers Sorting 👍 10742 👎 1287

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            # all positive number couldn't have sum 0
            if nums[i] > target and nums[i] > 0 and target > 0:  # 剪枝（可省）
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 去重
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and target > 0:  # 剪枝（可省）
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:  # 去重
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = s.fourSum(nums, target)
    print(result)  # Expected:[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
