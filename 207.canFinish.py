"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # map each course to prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # all courses along the curr DFS path
        visit = [False for _ in range(numCourses)]

        def dfs(i):
            if visit[i]:
                return False

            if preMap[i] == []:
                return True

            visit[i] = True
            for pre in preMap[i]:
                if not dfs(pre):
                    return False

            visit[i] = False
            preMap[i] = []  # no need to revisit again
            return True

        # if graph is not fully connected, return False
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
