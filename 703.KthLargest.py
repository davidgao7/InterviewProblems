# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
#
#
# Example 1:
#
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#
#
# Constraints:
#
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.
# Seen this question in a real interview before?
# 1/5
# Yes
# No

from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # declear a min heap
        self.min_heap = nums
        self.k = k  # trackcurrent kth learget
        heapq.heapify(self.min_heap)  # O(nlogn)

        # we can only obtain k number of elements, we don't care about k+1th largest
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  # O(logn)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # O(logn)
        # if length is > k we pop until k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # O(logn)

        # return the minimum of the minheap, which is always be the root
        # min_heap list has been changed by heapq
        # the root will always be the 1st one
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
