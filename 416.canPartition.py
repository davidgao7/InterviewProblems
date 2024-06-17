"""
Partition Equal Subset Sum
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # backtracking with memoization
        if sum(nums) % 2 != 0:
            return False

        db = set()
        db.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            new_db = set()
            for j in db:
                new_db.add(j + nums[i])
                new_db.add(j)
            db = new_db

        return  target in db

