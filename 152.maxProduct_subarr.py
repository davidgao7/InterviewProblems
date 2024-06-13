"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initailize the variables
        res = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            temp = curr_max * n
           
            # update the curr_max and curr_min
            curr_max = max(n, curr_max * n, curr_min * n)  # negative * negative = positive, result might greater than curr_max
            curr_min = min(n, temp, curr_min * n)

            res = max(res, curr_max)
        return res
