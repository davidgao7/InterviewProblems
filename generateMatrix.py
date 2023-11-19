# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n² in spiral order.
#
#
#  Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 20
#
#
#  Related Topics Array Matrix Simulation 👍 6102 👎 247
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # not related to algorithm, pure coding test
        # generate n*n matrics filled with 1~n^2 clockwise

        result = [[0] * n for _ in range(n)]  # cant use numpy, float not accepted
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1

        for offset in range(
            1, loop + 1
        ):  # NOTE: for each loop, number filled position should go inside
            # n-offset: number to fill after ignore overlap number
            for i in range(starty, n - offset):  # left -> right,
                # print(startx, i)
                result[startx][i] = count  # x unchange, column change
                count += 1

            for i in range(startx, n - offset):  # up -> down for the right hand side
                # print(i, n-offset)
                result[i][n - offset] = count  # y unchange, row change
                count += 1

            for i in range(n - offset, starty, -1):  #
                # print(n-offset, i)
                result[n - offset][i] = count
                count += 1

            for i in range(n - offset, startx, -1):
                # print(i, starty)
                result[i][starty] = count
                count += 1

            # update the inner start point
            startx += 1
            starty += 1

        if n % 2 != 0:
            # print(mid, mid)
            result[mid][mid] = count
        return result.tolist()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))
