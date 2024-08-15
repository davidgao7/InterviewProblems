/*
 * 73. Set Matrix Zeroes
Medium
Topics
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Accepted
1.6M
Submissions
2.7M
Acceptance Rate
57.0%
*/

import java.util.*;

class setZeros73 {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        boolean firstRow = false;
        boolean firstCol = false;
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                if(matrix[r][c] == 0){
                        // if find 0 at the first row or first column
                    if(r == 0) firstRow = true;
                    if(c == 0) firstCol = true;
                    matrix[0][c] = 0;
                    matrix[r][0] = 0;
                }
            }
        }
        for(int r = 1; r < row; r++){
            for(int c = 1; c < col; c++){
                if(matrix[0][c] == 0 || matrix[r][0] == 0){
                    matrix[r][c] = 0;
                }
            }
        }
        if(firstRow){
            for(int c = 0; c < col; c++){
                matrix[0][c] = 0;
            }
        }
        if(firstCol){
            for(int r = 0; r < row; r++){
                matrix[r][0] = 0;
            }
        }

    }
    public static void main(String[] args) {
            setZeros73 solution = new setZeros73();
        int[][] matrix = {{1,1,1},{1,0,1},{1,1,1}};
        solution.setZeroes(matrix);
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));  // [1, 0, 1], [0, 0, 0], [1, 0, 1] each row
        }
    }
}
