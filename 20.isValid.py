# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid.
#
#  An input string is valid if:
#
#
#  Open brackets must be closed by the same type of brackets.
#  Open brackets must be closed in the correct order.
#  Every close bracket has a corresponding open bracket of the same type.
#
#
#
#  Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
#  Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
#  Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s consists of parentheses only '()[]{}'.
#
#
#  Related Topics String Stack 👍 22779 👎 1586


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for i in range(0, len(s)):
            if s[i] == "(":
                stack.append(")")
            elif s[i] == "[":
                stack.append("]")
            elif s[i] == "{":
                stack.append("}")
            elif not stack and s[i] != stack[-1]:  # NOTE: if brackets didn't match and stack is not empty
                return False
            else:
                stack.pop()

        return True if not stack else False  # true if  matchs)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("(]"))
