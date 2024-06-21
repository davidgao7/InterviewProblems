"""
Meeting Schedule
Given an array of meeting time interval objects consisting of start and end times 

[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false

Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
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
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the start time of the intervals
        intervals.sort(key=lambda x: x.start)

        # check if the previous interval's end time is greater than the current interval's start time
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            # if start of i2 is less than end of i1, overlap course
            if i2.start < i1.end:
                return False

        return True

