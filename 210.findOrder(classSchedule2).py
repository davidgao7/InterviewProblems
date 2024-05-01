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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # NOTE: topological sort

        # build adjacency list of prereqs
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)

        # a couse has 3 possible states
        # visited : course has been added to output
        # visiting: course not added to output , but added to cycle
        # unvisited: course not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in visit:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                # cycle detected
                return []

        return output
