# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#  示例 3：
#
#
# 输入：s = "a"
# 输出："a"
#
#
#  示例 4：
#
#
# 输入：s = "ac"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母（大写和/或小写）组成
#
#  Related Topics 字符串 动态规划 👍 4141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
                n = len(s)
                if n < 2:
                    return s

                max_len = 1
                begin = 0
                # dp[i][j] 表示 s[i..j] 是否是回文串
                dp = [[False] * n for _ in range(n)]
                for i in range(n):
                    dp[i][i] = True

                # 递推开始
                # 先枚举子串长度
                for L in range(2, n + 1):
                    # 枚举左边界，左边界的上限设置可以宽松一些
                    for i in range(n):
                        # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                        j = L + i - 1
                        # 如果右边界越界，就可以退出当前循环
                        if j >= n:
                            break

                        if s[i] != s[j]:
                            dp[i][j] = False
                        else:
                            if j - i < 3:
                                dp[i][j] = True
                            else:
                                dp[i][j] = dp[i + 1][j - 1]

                        # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                        if dp[i][j] and j - i + 1 > max_len:
                            max_len = j - i + 1
                            begin = i
                return s[begin:begin + max_len]


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
s = 'cbbd'
print(solution.longestPalindrome(s))
