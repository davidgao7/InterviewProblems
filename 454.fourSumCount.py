# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
#
#
#  0 <= i, j, k, l < n
#  nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
#
#  Example 1:
#
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1)
#  + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1)
#  + 0 = 0
#
#
#  Example 2:
#
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
#
#  Constraints:
#
#
#  n == nums1.length
#  n == nums2.length
#  n == nums3.length
#  n == nums4.length
#  1 <= n <= 200
#  -2²⁸ <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2²⁸
#
#
#  Related Topics Array Hash Table 👍 4806 👎 138
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # record the sum of first 2 number in the map
        hashmap = dict()
        for a in nums1:
            for b in nums2:
                if a+b in hashmap:
                    hashmap[a+b] +=1
                else:
                    hashmap[a+b] = 1

        # if -(a+b) in nums3 and nums4, save to map
        count=0
        for c in nums3:
            for d in nums4:
                k = -c-d
                if k in hashmap.keys():
                    count += hashmap[k]

        return count

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]

    s=Solution()
    print(s.fourSumCount(nums1, nums2, nums3,nums4))