# Given an input string s, reverse the order of the words.
#
#  A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
#  Return a string of the words in reverse order concatenated by a single space.
#
#
#  Note that s may contain leading or trailing spaces or multiple spaces
# between two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
#  Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
#  Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
#  Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
#  There is at least one word in s.
#
#
#
#  Follow-up: If the string data type is mutable in your language, can you
# solve it in-place with O(1) extra space?
#
#  Related Topics Two Pointers String 👍 7661 👎 4960


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        # two pointer
        # split the whole str into words list
        words = s.split()

        # reverse each words
        # using two pointers
        left, right = 0, len(words) - 1
        # reverse the words list
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # concat list elements into str
        return "".join(words)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = "a good   example"
    solution = Solution()
    print(solution.reverseWords(s))
