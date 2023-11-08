# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
#
#  Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
#  Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
#  Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
#  Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 3 * 10⁵
#  s consists of digits, '+', '-', '(', ')', and ' '.
#  s represents a valid expression.
#  '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#
#  '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#
#  There will be no two consecutive operators in the input.
#  Every number and running calculation will fit in a signed 32-bit integer.
#
#
#  Related Topics Math String Stack Recursion 👍 5917 👎 435


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        # NOTE: only + - and brackets
        # '()' means 1 recursive, recursive could be simulated using stack
        cur, res = 0, 0
        sign = 1
        stack = []  # for bracket case

        for char in s:
            # if it's a number more than 1 digit, get the number
            if char.isdigit():
                cur = cur * 10 + int(char)

            # '+'/'-' can be treated as addition of positive & negative numbers
            elif char in ["+", "-"]:
                res += sign * cur

                sign = 1 if char == "+" else -1

                cur = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)

                sign = 1
                res = 0
            elif char == ")":
                res += sign * cur

                res *= stack.pop()

                res += stack.pop()

                cur = 0

        return res + sign * cur

# T: O(n)
# S: O(n)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    sol = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    print(sol.calculate(s))
