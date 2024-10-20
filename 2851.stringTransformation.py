"""
You are given two strings s and t of equal length n. You can perform the following operation on the string s:

    Remove a suffix of s of length l where 0 < l < n and append it at the start of s.
    For example, let s = 'abcd' then in one operation you can remove the suffix 'cd' and append it in front of s making s = 'cdab'.

You are also given an integer k. Return the number of ways in which s can be transformed into t in exactly k operations.

Since the answer can be large, return it modulo 109 + 7.



Example 1:

Input: s = "abcd", t = "cdab", k = 2
Output: 2
Explanation:
First way:
In first operation, choose suffix from index = 3, so resulting s = "dabc".
In second operation, choose suffix from index = 3, so resulting s = "cdab".

Second way:
In first operation, choose suffix from index = 1, so resulting s = "bcda".
In second operation, choose suffix from index = 1, so resulting s = "cdab".

Example 2:

Input: s = "ababab", t = "ababab", k = 1
Output: 2
Explanation:
First way:
Choose suffix from index = 2, so resulting s = "ababab".

Second way:
Choose suffix from index = 4, so resulting s = "ababab".



Constraints:

    2 <= s.length <= 5 * 105
    1 <= k <= 1015
    s.length == t.length
    s and t consist of only lowercase English alphabets.

Math
String
Dynamic Programming
String Matching
"""

from typing import List


class Solution:
    M: int = 1000000007

    def add(self, x: int, y: int) -> int:
        x += y
        if x >= self.M:
            x -= self.M
        return x

    def mul(self, x: int, y: int) -> int:
        return int(x * y % self.M)

    def getZ(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        left = right = 0
        for i in range(1, n):
            if i <= right and z[i - left] <= right - i:
                z[i] = z[i - left]
            else:
                z_i = max(0, right - i + 1)
                while i + z_i < n and s[i + z_i] == s[z_i]:
                    z_i += 1
                z[i] = z_i
            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1
        return z

    def matrixMultiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        m = len(a)
        n = len(a[0])
        p = len(b[0])
        r = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    r[i][j] = self.add(r[i][j], self.mul(a[i][k], b[k][j]))
        return r

    def matrixPower(self, a: List[List[int]], y: int) -> List[List[int]]:
        n = len(a)
        r = [[0] * n for _ in range(n)]
        for i in range(n):
            r[i][i] = 1
        x = [a[i][:] for i in range(n)]
        while y > 0:
            if y & 1:
                r = self.matrixMultiply(r, x)
            x = self.matrixMultiply(x, x)
            y >>= 1
        return r

    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        dp = self.matrixPower([[0, 1], [n - 1, n - 2]], k)[0]
        s += t + t
        z = self.getZ(s)
        m = n + n
        result = 0
        for i in range(n, m):
            if z[i] >= n:
                result = self.add(result, dp[0] if i - n == 0 else dp[1])
        return result


if __name__ == "__main__":
    s = "abcd"
    t = "cdab"
    k = 2
    so = Solution()
    print(so.numberOfWays(s, t, k))
