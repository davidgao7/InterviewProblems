# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否
# 则返回 -1。
#
#
# 示例 1:
#
#  输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
#
#  示例 2:
#
#  输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#
#
#
#  提示：
#
#
#  你可以假设 nums 中的所有元素是不重复的。
#  n 将在 [1, 10000]之间。
#  nums 的每个元素都将在 [-9999, 9999]之间。
#
#  Related Topics 数组 二分查找
#  👍 277 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # base case 0,1,2 elements
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and not (nums[0] == target):
            return -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            else:
                return -1
        if target < nums[0]:
            return -1
        pivot = (len(nums) - 1) // 2
        # ordered list
        val = nums[pivot]

        if target == val:
            return pivot
        if target < val:
            return self.search(nums[0:pivot], target)
        elif pivot + 1 <= len(nums) - 1:  # <= for getting the last element in list
            k = self.search(nums[pivot + 1:len(nums)], target) # not find element need to end quick
            if k != -1:
                return pivot + 1 + k
            else:
                pass

        return -1


# leetcode submit region end(Prohibit modification and deletion)
nums = [-1, 0, 5]
target = 2
s = Solution()
index = s.search(nums, target)
print('index of %d is %d in %s' % (target, index, nums))
