# Code
# Testcase
# Test Result
# Test Result
# 1235. Maximum Profit in Job Scheduling
# Hard
# Topics
# Companies
# Hint
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
#
# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
#
#
#
# Example 1:
#
#
#
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# Example 2:
#
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
# Example 3:
#
#
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
#
# Constraints:
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 104
# 1 <= startTime[i] < endTime[i] <= 109
# 1 <= profit[i] <= 104
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # greedy approach

        # 1. sort the jobs according to their end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  # O(nlogn)
        # print("start time, end time, profit")
        # print("sort by end time")
        # print(jobs)

        # loop through the jobs, and keep track of the maximum profit
        # that can be made at the end of each job
        # 2. for each job, we have two options:
        #   a. pick the job
        #   b. not pick the job
        #   c. find the first job that ends before this job starts
        #   d. find the maximum profit that can be made at the end of this job
        #   e. update the maximum profit that can be made at the end of this job
        #   f. return the maximum profit that can be made at the end of the last job

        dp = [[0, 0]]  # [end_time, profit]
        for s, e, p in jobs:

            # find the first job that ends before this job starts
            # the best way is to binary search, log time is less than linear time
            i = self.binary_search(dp, s)  # O(logn)

            # find the maximum profit that can be made at the end of this job
            # record the endtime, and the maximum profit that can be made at the end of this job
            # if the profit of this job is greater than the maximum profit that can be made at the end of this job
            # we update the maximum profit that can be made at the end of this job
            dp.append([e, max(dp[i][1] + p, dp[-1][1])])  # O(1)

        return dp[-1][1]

    def binary_search(self, dp, s):
        l, r = 0, len(dp) - 1
        while l < r:
            m = (l + r + 1) // 2
            # find the job that start time is ahead of the current job
            if dp[m][0] <= s:
                l = m
            else:
                r = m - 1
        return l


if __name__ == "__main__":
    s = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]

    result = s.jobScheduling(startTime, endTime, profit)
    print(result)
