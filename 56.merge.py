# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals that
# cover all the intervals in the input.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#
#  Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
#  Constraints:
#
#
#  1 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁴
#
#
#  Related Topics Array Sorting 👍 21516 👎 745
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        # sort by left bound
        intervals.sort(key=lambda x: x[0])
        merged = []
        # for each interval, if there is no overlap, add it to merged
        # if there is overlap, merge the current and previous interval
        # will have at least 1 interval in merged
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            # if curr left bound is less than prev right bound, there is overlap
            if curr[0] <= prev[1]:
                # last interval's left is always less than curr interval's left, use prev[0],so not change
                # merge, get the max of prev right bound and curr right bound
                prev[1] = max(prev[1], curr[1])
            else:
                # no overlap, add curr interval to merged
                merged.append(curr)

        return merged

# leetcode submit region end(Prohibit modification and deletion)
