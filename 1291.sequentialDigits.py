"""
1291. Sequential Digits
Medium
Topics
Companies
Hint

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]



Constraints:

    10 <= low <= high <= 10^9

"""

from typing import List
from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1,10))  # 9 digits

        while queue:
            num = queue.popleft()

            # if num is within the range, add to result list
            if low <= num <= high:
                res.append(num)

            # if num exceeds high, break since any subsequent number will be also out of range
            if num > high:
                break

            # if the last digit is less than 9, compute the next sequential number
            # by appending the next digit (i.e. last_digit + 1) to num, and endqueue
            # this new number
            last_digit = num % 10
            if last_digit < 9:
                queue.append(num*10 + last_digit + 1)

        return res


if __name__ == "__main__":
    print(Solution().sequentialDigits(100, 300))  # [123, 234]
