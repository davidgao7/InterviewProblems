"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
Accepted: 3761  |  Submitted: 10945  |  Acceptance Rate: 34%
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # method: union find (https://www.youtube.com/watch?v=ayW5B2W9hfo)
        #
        # each node is a parent of itself
        parent = [i for i in range(n)]
        # rank of each node is 1
        rank = [1] * n

        def find(x):
            """
            find the parent of the node
            """
            res = x

            while res != parent[res]:
                # optimize the tree
                # make the parent of x to be the parent of the parent of x
                # path compression, if doesn't have parent, it will do nothing
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res

        def union(x, y):
            parent_1, parent_2 = find(x), find(y)
            if parent_1 == parent_2:
                return 0  # already in the same group

            # union by rank
            if rank[parent_1] > rank[parent_2]:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]

            return 1  # union successfully

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
