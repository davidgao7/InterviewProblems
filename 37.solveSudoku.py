# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
#  A sudoku solution must satisfy all of the following rules:
#
#
#  Each of the digits 1-9 must occur exactly once in each row.
#  Each of the digits 1-9 must occur exactly once in each column.
#  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-
# boxes of the grid.
#
#
#  The '.' character indicates empty cells.
#
#
#  Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5
# ",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".
# ",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".
# ","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5
# "],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4
# ","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3
# "],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],[
# "9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3",
# "4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is
# shown below:
#
#
#
#
#
#  Constraints:
#
#
#  board.length == 9
#  board[i].length == 9
#  board[i][j] is a digit or '.'.
#  It is guaranteed that the input board has only one solution.
#
#
#  Related Topics Array Hash Table Backtracking Matrix 👍 9158 👎 237
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)

    def printboard(self, board: List[List[str]]) -> None:
        for row in board:
            r = []
            for cell in row:
                r.append(cell)
            print(r)

    def backtrack(self, board: List[List[str]]) -> bool:
        """
        :param board:
        :return: T/F if find a solution
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.isvalid(i, j, k, board):
                            print(i, j)
                            board[i][j] = str(k)
                            # self.printboard(board)
                            # print('=============================')
                            # if found a solution, no need to search further
                            if self.backtrack(board): return True
                            else:
                                # else back track
                                # print('backtrack')
                                board[i][j] = "."
                    # if none of 9 numbers no work, not solvable
                    return False
            return True

    def isvalid(self, i:int, j:int, k:int, board:List[List[str]]) -> bool:
        # haven't put the k in yet
        # check column
        for n in range(0, len(board)):
            if board[n][j] == str(k):
                return False
        # check row
        for n in range(0, len(board[i])):
            if board[i][n] == str(k):
                return False
        # check the subSudoku(3x3)
        threebythree_startrow = (i // 3) * 3
        threebythree_startcol = (j // 3) * 3
        for i in range(threebythree_startrow, threebythree_startrow + 3):
            for j in range(threebythree_startcol, threebythree_startcol + 3):
                if board[i][j] == str(k):
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print('original:')
    s.printboard(board)
    print('====================')
    s.solveSudoku(board)
    for row in board:
        print(row)