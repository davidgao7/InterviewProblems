# Given a string s, find the longest palindromic subsequence's length in s.
#
#  A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining elements.
#
#
#  Example 1:
#
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#
#
#  Example 2:
#
#
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 1000
#  s consists only of lowercase English letters.
#
#
#  Related Topics String Dynamic Programming 👍 9289 👎 317


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1

        # 1. construct a dp array
        dp = [[0] * len(s) for _ in range(len(s))]

        # 2. fill the dp array from the bottom up
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1  # Base case: single character is a palindrome of length 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:  # if the two characters are the same
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:  # if the two characters are different, then the length of the palindrome is the maximum of the two subproblems
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("aaa")) # 3