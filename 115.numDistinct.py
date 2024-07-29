# Given two strings s and t, return the number of distinct subsequences of s which equals t.
#
#  The test cases are generated so that the answer fits on a 32-bit signed
# integer.
#
#
#  Example 1:
#
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
#
#
#  Example 2:
#
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
#  Constraints:
#
#
#  1 <= s.length, t.length <= 1000
#  s and t consist of English letters.
#
#
#  Related Topics String Dynamic Programming 👍 6425 👎 282


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        # time complexity: O(m * n)

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                # if s[i] == t[j], we can either skip s[i] or match s[i] with t[j]
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # if s[i] != t[j], we can only skip s[i]
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    result = s.numDistinct("rabbit", "rabbbit")
    print(result)
