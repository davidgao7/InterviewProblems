from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row, col = 0, 0

        while row < len(matrix):

            if matrix[row][col] == target:
                return True
            if matrix[row][-1] < target:  # target is in below
                row += 1
            else:  # target is in the same row
                # binary search in this row
                left, right = 0, len(matrix[row]) - 1
                while left < right:
                    print(left, right)
                    mid = (left + right) // 2
                    # print(mid)

                    if matrix[row][mid] == target:
                        return True
                    if matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                # when left == right, check if the element is the target
                # we need to check the last element in the row
                if matrix[row][left] == target:
                    return True

                return False
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # matrix = [[1, 3]]
    target = 20
    print(s.searchMatrix(matrix, target))
