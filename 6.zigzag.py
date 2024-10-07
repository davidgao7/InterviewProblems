"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge case: if numRows is 1, no zigzag pattern, return the original string
        if numRows == 1 or numRows >= len(s):
            return s

        # create a list of empty strings for each row
        rows = [""] * numRows
        current_row = 0
        direction = -1  # This will control the direction of traversal (down/up)

        # iterate over each chracter in the string
        for char in s:
            # add the character to the current row
            rows[current_row] += char
            print(f"current_row: {current_row}, \nchar: {char}")

            # change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            # move to the next row in the current direction
            current_row += direction

        # join all rows into a single string and return the result
        return "".join(rows)


if "__main__" == __name__:
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    print(sol.convert(s, numRows))
