# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
#  A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not).
#
#
#  Example 1:
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#
#  Example 2:
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
#  Constraints:
#
#
#  0 <= s.length <= 100
#  0 <= t.length <= 10⁴
#  s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming
# s, say
# s1, s2, ..., sk where
# k >= 10⁹, and you want to check one by one to see if
# t has its subsequence. In this scenario, how would you change your code?
#
#  Related Topics Two Pointers String Dynamic Programming 👍 9262 👎 499


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 1. create a dp array
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        # 2. fill the dp array
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # 3. if the characters are equal, then add 1 to the previous diagonal element
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 4. if the characters are not equal, then take the maximum of the previous row and previous column
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 5. if the last element of the dp array is equal to the length of the string s, then return True
        return dp[-1][-1] == len(s)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc") == True
    assert Solution().isSubsequence("axc", "ahbg") == False
