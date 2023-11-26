# Write an algorithm to determine if a number n is happy.
#
#  A happy number is a number defined by the following process:
#
#
#  Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
#  Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
#  Those numbers for which this process ends in 1 are happy.
#
#
#  Return true if n is a happy number, and false if not.
#
#
#  Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
#
#
#  Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
#  Constraints:
#
#
#  1 <= n <= 2³¹ - 1
#
#
#  Related Topics Hash Table Math Two Pointers 👍 9736 👎 1303


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        # Repeat the process until the number equals 1 (where it will stay),
        # or it loops endlessly in a cycle which does not include 1.
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True

            # if occurs before, means it step into endless loop
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r**2
        return new_num


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s=Solution()
    n=2
    print(s.isHappy(n))