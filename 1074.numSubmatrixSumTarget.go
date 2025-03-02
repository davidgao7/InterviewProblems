/*
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0



Constraints:

    1 <= matrix.length <= 100
    1 <= matrix[0].length <= 100
    -1000 <= matrix[i][j] <= 1000
    -10^8 <= target <= 10^8

*/

package main

import "fmt"

func numSubmatrixSumTarget(matrix [][]int, target int) int {
	// Check if the matrix is empty
	if len(matrix) == 0 {
		return 0
	}

	// Get the dimensions of the matrix
	rows, cols := len(matrix), len(matrix[0])

	// Initialize the sub_sum matrix with the same dimensions as the input matrix
	sub_sum := make([][]int, rows)
	for i := range sub_sum {
		sub_sum[i] = make([]int, cols)
	}

	// Compute the cumulative sums for the sub_sum matrix
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			top := 0
			left := 0
			top_left := 0

			if r > 0 {
				top = sub_sum[r-1][c]
			}
			if c > 0 {
				left = sub_sum[r][c-1]
			}
			if r > 0 && c > 0 {
				top_left = sub_sum[r-1][c-1]
			}

			sub_sum[r][c] = matrix[r][c] + top + left - top_left
		}
	}

	res := 0

	// Iterate over all possible submatrices
	for r1 := 0; r1 < rows; r1++ {
		for r2 := r1; r2 < rows; r2++ {
			count := make(map[int]int)
			count[0] = 1
			cur_sum := 0
			for c := 0; c < cols; c++ {
				if r1 > 0 {
					cur_sum = sub_sum[r2][c] - sub_sum[r1-1][c]
				} else {
					cur_sum = sub_sum[r2][c]
				}
				diff := cur_sum - target
				res += count[diff]
				count[cur_sum]++
			}
		}
	}

	return res
}

func main() {
	matrix := [][]int{{0, 1, 0}, {1, 1, 1}, {0, 1, 0}}
	fmt.Println(numSubmatrixSumTarget(matrix, 0)) // 4
}
