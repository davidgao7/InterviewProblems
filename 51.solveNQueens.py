# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
#  Given an integer n, return all distinct solutions to the n-queens puzzle.
# You may return the answer in any order.
#
#  Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
#  Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 9
#
#
#  Related Topics Array Backtracking 👍 11827 👎 261
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        checkbox = [["."] * n for _ in range(n)]
        self.backtracking(checkbox, n, 0, result)
        return [["".join(row) for row in solution] for solution in result]

    def backtracking(self, checkbox, n, row_index, result):
        """
        :param checkbox: check plate current state
        :param n: n*n
        :param row_index: current row index
        :return:
        """

        # when all row choice in this column is complete, we've reached the leaf of the tree
        if row_index == n:
            print(checkbox)
            result.append(checkbox[:])  # add current path
            return

        # check current row 's each position is valid
        for i in range(0, n):
            if self.isValid(row_index, i, checkbox):
                # can put queen
                checkbox[row_index][i] = "Q"
                # check next row
                self.backtracking(checkbox, n, row_index + 1, result)
                # undo to go to another option/branch
                checkbox[row_index][i] = "."

    def isValid(self, row, col, checkbox):
        """
        check the curreent checkbox is valid
        condition should satisfy: row and col doesn't occur Q twice
        :param row:
        :param col:
        :param checkbox:
        :return: True or False
        """
        # check col
        for i in range(row):
            if checkbox[i][col] == "Q":
                return False

        # check 45 angle
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if checkbox[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # check 135
        k, l = row - 1, col - 1
        while k >= 0 and l < len(checkbox):
            if checkbox[k][l] == "Q":
                return False
            k -= 1
            l += 1

        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.solveNQueens(n))