"""
Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
Accepted: 2757  |  Submitted: 9350  |  Acceptance Rate: 29%
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        I think we can use dfs to search if each edges makes a valid tree
        the valid tree is a tree with no cycle and all nodes are connected
        """
        # if there is no node, return False
        if not n:
            return False

        # if there is only one node and no edges, return True
        if n == 1 and not edges:
            return True

        visited = set()
        neighbor_edges_map = {}

        # create a map of neighbors
        for edge in edges:
            if edge[0] not in neighbor_edges_map:
                neighbor_edges_map[edge[0]] = []
            if edge[1] not in neighbor_edges_map:
                neighbor_edges_map[edge[1]] = []
            neighbor_edges_map[edge[0]].append(edge[1])
            neighbor_edges_map[edge[1]].append(edge[0])

        # print("========================")
        # print("routes:")
        # print(neighbor_edges_map)
        # print("========================")
        #
        def dfs(edge, parent):
            if edge in visited:
                return False

            print(f"visit edge {edge}")
            visited.add(edge)
            for neighbor in neighbor_edges_map[edge]:
                if neighbor != parent and not dfs(neighbor, edge):
                    return False

            return True  # if all neighbors are visited

        # check if all nodes are visited
        return dfs(0, -1) and len(visited) == n


if __name__ == "__main__":
    s = Solution()
    # n = 5
    # edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    n = 1
    edges = []
    print(s.validTree(n, edges))  # expected : True
