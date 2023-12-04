# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
#
#
#  Example 1:
#
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#
#
#  Example 2:
#
#
# Input: s = "aba"
# Output: false
#
#
#  Example 3:
#
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc"
# twice.
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s consists of lowercase English letters.
#
#
#  Related Topics String String Matching 👍 6205 👎 493


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def get_next(self, next, s):
        next[0] = 0  # 记录匹配失败后next子串跳过元素的个数
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]

            if s[i] == s[j]:
                j += 1
            next[i] = j  # char at i, j no matching, replace current index with value of j

    def repeatedSubstringPattern(self, s: str) -> bool:
        # idea: KMP: when match the str, moving the ptr, if the ptr meets not match, move the ptr to next match
        # time complexity: O(m+n)
        if len(s) == 0:
            return False

        nex = [-1] * len(s)
        self.get_next(nex, s)
        l = len(s)

        # l % (l - (nex[l - 1])) == 0 means has common substring
        # 数组的长度正好可以被 (数组长度-最长相等前后缀的长度) 整除
        if nex[l - 1] != 0 and l % (l - (nex[l - 1])) == 0:
            return True

        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = "abcabcabcabc"
    solution = Solution()
    print(solution.repeatedSubstringPattern(s))