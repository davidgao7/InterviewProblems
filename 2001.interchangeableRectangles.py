"""
You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.



Example 1:

Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.

Example 2:

Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.



Constraints:

    n == rectangles.length
    1 <= n <= 105
    rectangles[i].length == 2
    1 <= widthi, heighti <= 105

Seen this question in a real interview before?
1/5
Yes
No
Accepted
44.7K
Submissions
88.2K
Acceptance Rate
50.6%
Topics
Array
Hash Table
Math
Counting
Number Theory
Hint 1
Store the rectangle height and width ratio in a hashmap.
Hint 2
Traverse the ratios, and for each ratio, use the frequency of the ratio to add to the total pair count.
"""

from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}

        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)  # count if the ratio is the same

        # number of pairs
        res = 0

        for c in count.values():
            if c > 1:
                # because a pair has to be greater than 1
                res += (c * (c - 1)) // 2  # combination formula
                # n! / (n! * (n-k)!)
                #
        return res
