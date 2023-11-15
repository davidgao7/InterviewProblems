# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can only
# see the k numbers in the window. Each time the sliding window moves right by one
# position.
#
#  Return the max sliding window.
#
#
#  Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#  Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  1 <= k <= nums.length
#
#
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic
# Queue 👍 17339 👎 604
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    class MyHeap(object):
        def __init__(self, ):

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq  # creating priority queue

        #  building the max heap
        # time complexity: O(number of elements)
        for i in range(0, len(nums)):
            if i==0:
                heapq.heapify(nums[i])
            else:
                heapq.heappush(nums[i])

        pass


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = s.maxSlidingWindow(nums, k)
    print(result)
