"""
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time
it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all the n nodes to receive the signal. If it is impossible for all the
n nodes to receive the signal, return -1.


Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # shortest path problem (dijsktra)
        # min heap
        # O(ElogV)
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))  # u -> v(edge), w(weight)

        min_heap = [(0, k)]  # (time, node)
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue

            # don't visit again
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                # for all neighbors of n1 hasn't been visited, push to min heap
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        # if all nodes are visited, return time
        return t if len(visited) == n else -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(Solution().networkDelayTime(times, n, k))  # 2
