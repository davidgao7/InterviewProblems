# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
#  You must write an algorithm that runs in O(n) time.
#
#
#  Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#  Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
#  Constraints:
#
#
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#
#
#  Related Topics Array Hash Table Union Find 👍 19258 👎 922


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for n in nums:
            # check if n has left neighbor
            # check if it is the start of a sequence
            if n - 1 not in num_set:
                # n is the start of a sequence
                length = 0
                while (
                    n + length in num_set
                ):  # <critical step>  continue to check if n+1, n+2, n+3... exists
                    length += 1  # checking consetive numbers
                longest_streak = max(length, longest_streak)

        return longest_streak


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
