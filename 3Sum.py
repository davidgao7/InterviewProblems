# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
#  Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
#  Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
#  Constraints:
#
#
#  3 <= nums.length <= 3000
#  -10⁵ <= nums[i] <= 10⁵
#
#
#  Related Topics Array Two Pointers Sorting 👍 29003 👎 2621
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # record result
        result = []
        # sort nums
        nums.sort()
        # if the 1st > 0, sum 0 not possible
        if nums[0] > 0:
            return []

        for i in range(0, len(nums)):

            # skip the overlapped element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # moving left right pointer towards each other
            while right > left:

                # calculate the sum of current ptr
                sum_ = nums[i] + nums[left] + nums[right]

                # if current 3 sums are < 0 , move left to greater value
                if sum_ < 0:
                    left += 1

                # if current 3 sums are > 0, move right to smaller value
                elif sum_ > 0:
                    right -= 1

                # find the correct 3 values which have sum of 0, record the value (not index) to result
                # order not matter
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # narrow down the pointer to get rid of overlapping reuslt
                    # eg. [0, -1, -1, -1, -1, 1, 1, 1]
                    #          ^              ^
                    # eg. [0, -1, -1, -1, -1, 1, 1, 1]    <=== overlapping result, no need to record
                    #              ^          ^

                    # take care of right side
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    # if it's not overlapping case, do the regular move
                    right-=1
                    left+=1

        return result



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
