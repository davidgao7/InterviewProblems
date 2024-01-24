# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the
# intervals non-overlapping.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-
# overlapping.
#
#
#  Example 2:
#
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
#
#
#  Example 3:
#
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
#  Constraints:
#
#
#  1 <= intervals.length <= 10⁵
#  intervals[i].length == 2
#  -5 * 10⁴ <= starti < endi <= 5 * 10⁴
#
#
#  Related Topics Array Dynamic Programming Greedy Sorting 👍 7814 👎 212
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        # sort points according to 1st e
        intervals.sort(key=lambda x: (x[0], x[1]))
        count = 0


        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i][1] = min( intervals[i-1][1], intervals[i][1])
                count += 1

        return count

# leetcode submit region end(Prohibit modification and deletion)
