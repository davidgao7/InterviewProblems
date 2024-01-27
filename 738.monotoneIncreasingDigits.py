# An integer has monotone increasing digits if and only if each pair of
# adjacent digits x and y satisfy x <= y.
#
#  Given an integer n, return the largest number that is less than or equal to
# n with monotone increasing digits.
#
#
#  Example 1:
#
#
# Input: n = 10
# Output: 9
#
#
#  Example 2:
#
#
# Input: n = 1234
# Output: 1234
#
#
#  Example 3:
#
#
# Input: n = 332
# Output: 299
#
#
#
#  Constraints:
#
#
#  0 <= n <= 10⁹
#
#
#  Related Topics Math Greedy 👍 1284 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 1. change n to string for looping each digit
        s= str(n)
        flag = len(s)
        l = len(s)-1

        # 2. start from the last digit,
        # if the digit before is larger than the current digit,
        # then the digit is not monotone increasing
        # we need to change the pervious digit (s[i-1]) to s[i-1]-1
        # the digit after s[i-1] should be 9
        # then it becomes the largest number that is less than or equal to n with monotone increasing digits
        for i in range(l, 0, -1):
            if s[i-1] > s[i]:
                # s[i-1]= str(int(s[i-1])-1)  not allow item assignment
                s = s[:i-1] + str(int(s[i-1])-1) + s[i:]
                flag = i

        # then we need to change the digits after the digit we changed to 9
        # for example, 3 32, after changing 3 to 2, we need to change 32 to 29
        for i in range(flag, len(s)):
            # s[i] = '9'
            s = s[:i] + '9' + s[i+1:]

        return int(s)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = 332
    s = Solution()
    print(s.monotoneIncreasingDigits(n))
