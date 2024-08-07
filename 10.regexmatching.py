"""
10. Regular Expression Matching
Hard
Topics
Companies
Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a
previous valid character to match.
Accepted
993.8K
Submissions
3.5M
Acceptance Rate
28.3%
Topics
String
Dynamic Programming
Recursion
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        s: input string
        p: pattern
        """

        # memoization
        cache = {}

        # top down memoization
        def dfs(i, j):
            # check if i and j are in cache
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # handeling the case of *
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:
        """
        s: input string
        p: pattern
        """

        # bottom up dp
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(2, n + 1):
            dp[0][i] = dp[0][i - 2] and p[i - 1] == "*"
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = (
                        dp[i][j - 2]
                        or (s[i - 1] == p[j - 2] or p[j - 2] == ".")
                        and dp[i - 1][j]
                    )
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (
                        s[i - 1] == p[j - 1] or p[j - 1] == "."
                    )
        return dp[m][n]
