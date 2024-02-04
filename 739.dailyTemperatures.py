# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the iᵗʰ day to get a warmer temperature. If there is no future day for
# which this is possible, keep answer[i] == 0 instead.
#
#
#  Example 1:
#  Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#
#  Example 2:
#  Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#
#  Example 3:
#  Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
#  Constraints:
#
#
#  1 <= temperatures.length <= 10⁵
#  30 <= temperatures[i] <= 100
#
#
#  Related Topics Array Stack Monotonic Stack 👍 12771 👎 297
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)  # initialize the result array with 0s
        for i, t in enumerate(temperatures):
            if i==0:
                continue
            # loop elemnt is less than the top of the stack
            # add into the stack
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                # loop element is greater than the top of the stack
                # pop the stack and update the result array
                # until the loop element is less than the top of the stack
                while stack and temperatures[i] > temperatures[stack[-1]]:  # stack is not empty and the loop element is greater than the top of the stack
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]