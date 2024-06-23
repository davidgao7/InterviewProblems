"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""

from typing import List
# use min heap to track the smallest interval
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # NOTE: for every inerval question, we can always sort the intervals for effeciency
        intervals.sort()

        min_heap = []
        res, i = {}, 0

        for q in sorted(queries):

            # interate through the intervals, keep adding to min heap while the interval is within the query
            while i < len(intervals) and intervals[i][0] <=q:
                l, r = intervals[i]
                # find a smallest intervals which this value belongs to
                heapq.heappush(min_heap, (r-l+1, r))  # adding the (size of interval, right boundary)
                i += 1

            # poping the intervals that are to far to the left
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # adding the result to the result list if there is a valid interval in the min heap
            res[q] = min_heap[0][0] if min_heap else -1

        # return the result list
        return [res[q] for q in queries]

# Time complexity: O(nlogn + qlogq + n + q) = O((n+q)log(n+q))
# explaination: sorting the intervals and queries takes O(nlogn + qlogq), iterating through the intervals and queries takes O(n+q), and the min heap operations take O(n+q) as well


