from typing import List

"""
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # initialize the left pointer and the current total sum
        left, total_sum = 0, 0
        # initialize the minimum length to infinity
        res = float("inf")

        for right in range(len(nums)):
            # update the total
            total_sum += nums[right]
            # in order to find the minimum array, we can keep shriking the left pointer
            # while this condition holds
            while total_sum >= target:
                # update the minimum length
                res = min(res, right - left + 1)
                left += 1
                total_sum -= nums[left - 1]

        # if result is still infinity, then we couldn't find arry that is greater than or equal to target
        # return 0 as the question said
        return 0 if res == float("inf") else res


# time complexity: O(n) since we are iterating through the array only once
# space complexity: O(1) since we are not using any additional
