"""
Meeting Schedule II
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 100
0 <= intervals[i].start < intervals[i].end <= 1000

"""

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res, count = 0, 0
        s,e = 0,0
        # print(res)

        while s < len(starts):
            if starts[s] < end[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res



if __name__ == '__main__':
    intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
    # print(intervals)
    print(Solution().minMeetingRooms(intervals))
