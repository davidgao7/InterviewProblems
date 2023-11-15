# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
#  Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
#  Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an
# O(n) solution using a different approach?
#
#  Related Topics Array Two Pointers Sorting 👍 8470 👎 211

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        # nums is sorted
        # start find the largest number, then coming close to the center
        res = []
        # building in resverse order b/c we add the large result in first
        while l<=r:
            # since the absolute value of the number will be smaller when the number in the middle(list is sorted),
            # we start from the middle, then use ptr spread towards left & right
            if nums[l] ** 2 > nums[r] ** 2:
                res.append(nums[l]**2)
                l+=1
            else:
                res.append(nums[r]**2)
                r-=1
        res.reverse()
        return res
# time : O(logn)
# space: O(n)

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    s = Solution()
    print(s.sortedSquares(nums))