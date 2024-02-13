# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
#  Each row must contain the digits 1-9 without repetition.
#  Each column must contain the digits 1-9 without repetition.
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
#  Note:
#
#
#  A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
#  Only the filled cells need to be validated according to the mentioned rules.
#
#
#
#
#  Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
#  Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
#
#
#
#  Constraints:
#
#
#  board.length == 9
#  board[i].length == 9
#  board[i][j] is a digit 1-9 or '.'.
#
#
#  Related Topics Array Hash Table Matrix 👍 10293 👎 1080
from typing import List
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # detect duplicate in set
        cols_check = defaultdict(set)
        rows_check = defaultdict(set)
        squares_check = defaultdict(set)  # key: (i//3, j//3)

        for row in range(9):
            for col in range(9):
                if (
                    board[row][col] == "."
                ):  # leetcode submit region end(Prohibit modification and deletion)
                    continue
                if (
                    board[row][col] in rows_check[row]
                    or board[row][col] in cols_check[col]
                    or board[row][col] in squares_check[row // 3, col // 3]
                ):
                    return False

                cols_check[col].add(board[row][col])
                rows_check[row].add(board[row][col])
                squares_check[row // 3, col // 3].add(board[row][col])

        return True


if __name__ == "__main__":
    s = Solution()

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(s.isValidSudoku(board=board))
