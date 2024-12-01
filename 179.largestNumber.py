"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109

Seen this question in a real interview before?
1/5
Yes
No
Accepted
666.8K
Submissions
1.7M
Acceptance Rate
40.4%
Topics
Array
String
Greedy
Sorting
Companies
0 - 3 months
Google
13
Amazon
10
Meta
6
Microsoft
5
Zoho
5
Bloomberg
3
Myntra
2
0 - 6 months
tcs
3
Accenture
3
Oracle
2
Graviton
2
Works Applications
2
6 months ago
Adobe
8
Apple
7
Salesforce
7
Yahoo
6
Uber
4
Goldman Sachs
3
ServiceNow
"""

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
        # return "".join(map(str, nums))


if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([10, 2]))
