# Given an array of n integers, find the minimum element in each sliding window of size k. Return the list containing the minimum elements of each sliding window of size k.
#
# For example given array = {3, 4, 2, 5, 1} and k = 3. Here we have 3 possible windows of size 3. For first window {3, 4, 2, 5, 1}, min = 2.
# For second window {3, 4, 2, 5, 1}, min = 2.
# For third window {3, 4, 2, 5, 1}, min = 1.
# Hence return the list {2, 2, 1}.
# Sample 0
# Input
#
# nums: [3, 4, 2, 5, 1]
#
# k: 3
# Output
#
# [2, 2, 1]
# Sample 1
# Input
#
# num: [1, 2, 3, 4]
#
# k: 2
# Output
#
# [1, 2, 3]
from __future__ import annotations


class SlidingWindowMinimum:
    # DO NOT read from stdin or write to stdout.
    # Input is given as the function arguments.
    # Output is taken as the function return value.
    def getMinimums(self, nums: list[int], k: int) -> list[int]:
        import collections
        nums = [-1*a for a in nums]

        output = []
        q = collections.deque()  # index
        l = r = 0  # window

        while r < len(nums):
            # make sure no smaller in the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()  # pop the elem smaller than current e

            # add new value
            q.append(r)

            # if left index out of bound, remove left val from window
            if l > q[0]:
                q.popleft()  # shift the window to right

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output
