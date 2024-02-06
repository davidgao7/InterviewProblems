# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the
# histogram.
#
#
#  Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
#
#  Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
#  Constraints:
#
#
#  1 <= heights.length <= 10⁵
#  0 <= heights[i] <= 10⁴
#
#
#  Related Topics Array Stack Monotonic Stack 👍 16555 👎 250
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force, O(n^2) time, O(1) space
        # result = 0
        #
        # for i in range(len(heights)):
        #     min_height = float('inf')
        #     for j in range(i, len(heights)):
        #         min_height = min(min_height, heights[j])
        #         result = max(result, min_height * (j - i + 1))
        #
        # return result

        # O(n) time, O(n) space
        stack = []
        result = 0
        heights = [0] + heights + [0]  # add 0 to the beginning and the end of the list to avoid index out of range

        for i in range(len(heights)):
            # if heights[i] > stack[-1], we append the index to the stack
            # if heights[i] == stack[-1], we pop the index from the stack, then append the index to the stack
            # if heights[i] < stack[-1], we pop the index from the stack and calculate the area,
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                result = max(result, height * width)  # calculate the area, update the result
            stack.append(i)

        return result
# leetcode submit region end(Prohibit modification and deletion)

