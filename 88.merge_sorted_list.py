"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # get rid of the trailing zeros, but keep the length of nums1 to m
        while nums1 and nums1[-1] == 0 and len(nums1) > m:
            nums1.pop(-1)
        while nums2 and nums2[-1] == 0 and len(nums2) > n:
            nums2.pop(-1)

        # print(nums1, nums2)

        # merge and sort the two lists
        nums1.extend(nums2)
        # print(nums1)

        # TODO: sort is getting rid of the zeros, need to fix this
        nums1.sort()

        # remove the extra leading zeros
        # while nums1[0] == 0:
        #     nums1.pop(0)


if __name__ == "__main__":
    # nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    # m = 6
    # nums2 = [1, 2, 2]
    # n = 3
    # sol = Solution()
    # sol.merge(nums1, m, nums2, n)
    # print(nums1)

    # nums1 = [-1, -1, 0, 0, 0, 0]
    # m = 4
    # nums2 = [-1, 0]
    # n = 2
    # sol = Solution()
    # sol.merge(nums1, m, nums2, n)
    # print(nums1)

    nums1 = [0, 1, 1, 2, 2, 0, 0, 0]
    m = 5
    nums2 = [0, 3, 3]
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
