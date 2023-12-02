# Given a string s and an integer k, reverse the first k characters for every 2
# k characters counting from the start of the string.
#
#  If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the first
# k characters and leave the other as original.
#
#
#  Example 1:
#  Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#  Example 2:
#  Input: s = "abcd", k = 2
# Output: "bacd"
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s consists of only lowercase English letters.
#  1 <= k <= 10⁴
#
#
#  Related Topics Two Pointers String 👍 1832 👎 3584


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # two pointers: i, j
        i = 0
        while i < len(s):
            j = i + k
            # reverse the k elements
            # [start:stop:step]
            # [::] is samilar to start=0 end=end of str
            # [:i] is same as [0:i], where ith index is exclusive
            s = s[:i] + s[i:j][::-1] + s[j:]
            # move the first pointer, skip the done part
            # NOTE:
            i = i + 2 * k
        return s


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    solution = Solution()
    print(solution.reverseStr(s, k))
