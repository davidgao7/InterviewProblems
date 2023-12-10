# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
#
#  Evaluate the expression. Return an integer that represents the value of the
# expression.
#
#  Note that:
#
#
#  The valid operators are '+', '-', '*', and '/'.
#  Each operand may be an integer or another expression.
#  The division between two integers always truncates toward zero.
#  There will not be any division by zero.
#  The input represents a valid arithmetic expression in a reverse polish
# notation.
#  The answer and all the intermediate calculations can be represented in a 32-
# bit integer.
#
#
#
#  Example 1:
#
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
#  Example 2:
#
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
#  Example 3:
#
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
#  Constraints:
#
#
#  1 <= tokens.length <= 10⁴
#  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
#
#
#  Related Topics Array Math Stack 👍 6753 👎 986

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            # 4 ops + other characters cases
            if c == "+": # if operation is + or * , you pop the previous number to do the operation
                stack.append(stack.pop() + stack.pop())
            elif c == "-":  # if operation is - or /, you have to use the second pop subtract the first pop
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":  # same as subtraction, you divide the second pop by the first pop
                a,b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            # if it's number, push into the stack
            else:
                stack.append(int(c))
            # print(stack)

        return stack[0]  # you've poped all the numbers

        # time complexity: O(n) loop the tokens


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(s.evalRPN(tokens))
