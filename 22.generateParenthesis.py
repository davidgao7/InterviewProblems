# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open prenthesis if open < n
        # only add close prenthesis if close < open
        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
    # print(s.generateParenthesis(1))
    # print(s.generateParenthesis(2))
    # print(s.generateParenthesis(4))
    # print(s.generateParenthesis(5))
    # print(s.generateParenthesis(6))
    # print(s.generateParenthesis(7))
    # print(s.generateParenthesis(8))
