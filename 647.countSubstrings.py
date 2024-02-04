# Given a string s, return the number of palindromic substrings in it.
#
#  A string is a palindrome when it reads the same backward as forward.
#
#  A substring is a contiguous sequence of characters within the string.
#
#
#  Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#  Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 1000
#  s consists of lowercase English letters.
#
#
#  Related Topics String Dynamic Programming 👍 9937 👎 209

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        # loop bottom up
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        result += 1
                        dp[i][j] = True

                self.print_matrix_table(dp)
                print("=====")
                # print( f'sfasdfasfafds' # one line comment
                # f'sdfssdfssdfads')

        return result

    def countSubstrings_correct(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1):  # 注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:  # 情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:  # 情况三
                        result += 1
                        dp[i][j] = True
        return result

    def print_matrix_table(self, matrix):
        for row in matrix:
            print(row)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("abc"))  # 3
