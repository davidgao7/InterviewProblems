# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
#
#  You are given two distinct 0-indexed integer arrays nums1 and nums2, where
# nums1 is a subset of nums2.
#
#  For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[
# j] and determine the next greater element of nums2[j] in nums2. If there is no
# next greater element, then the answer for this query is -1.
#
#  Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.
#
#
#  Example 1:
#
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
#
#
#  Example 2:
#
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so
# the answer is -1.
#
#
#
#  Constraints:
#
#
#  1 <= nums1.length <= nums2.length <= 1000
#  0 <= nums1[i], nums2[i] <= 10⁴
#  All integers in nums1 and nums2 are unique.
#  All the integers of nums1 also appear in nums2.
#
#
#
# Follow up: Could you find an
# O(nums1.length + nums2.length) solution?
#
#  Related Topics Array Hash Table Stack Monotonic Stack 👍 7575 👎 637
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums1)
        hashmap = {}  # key: value in nums1, value: index in nums1

        if not nums1:
            return result

        for i, num in enumerate(nums1):
            hashmap[num] = i

        stack.append(0)  # store the element which has iterated in nums1
        for i in range(1, len(nums2)):
            if nums2[i] < nums2[stack[-1]]:
                stack.append(i)
            elif nums2[i] == nums2[stack[-1]]:
                stack.append(i)
            else:
                # keep comparing until the loop element is less than the top of the stack
                while stack and nums2[i] > nums2[stack[-1]]:
                    # if top of the stack is in nums1, update the result array
                    if nums2[stack[-1]] in hashmap.keys():
                        index = hashmap[nums2[stack[-1]]]
                        result[index] = nums2[i-1]
                    # pop the stack after record the number in result array
                    stack.pop(-1)
                stack.append(i)
        return result


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    so = Solution()
    print(so.nextGreaterElement([2,4], [1,2, 3, 4])) # [3, -1]