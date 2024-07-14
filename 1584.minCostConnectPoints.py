"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # 1. create adjacency list
        adj = {i: [] for i in range(N)}  # i: list of [node, cost]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):  # compare other points
                x2, y2 = points[j]
                # get manhattan distance
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        # Prim's algorithm
        # O(ElogE) = O(N^2logN
        res = 0
        visit = set()
        min_heap = [(0, 0)]  # [(cost, node)]

        while len(visit) < N:
            cost, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            res += cost  # add fresh new node
            for nei, dist in adj[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (dist, nei))

        return res
