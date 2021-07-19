class Solution:
    def reverse(self, x: int) -> int:
        x_use = x
        if x == 0:
            return 0
        if x < 0:
            x_use = -1*x

        x_string = str(x_use)
        x_string_reverse = x_string[::-1]

        answer = 0
        n_digits = len(x_string_reverse)
        for i in range(0, n_digits):
            if i == 0 and x_string_reverse[i] == '0':
                continue
            else:
                answer += int(x_string_reverse[i]) * 10 ** (n_digits - 1 - i)

        if x < 0:
            answer *= -1

        return answer if -2147483648 < answer < 2147483647 else 0


s = Solution()
x = 1534236469
x_reverse = s.reverse(x)
print('reverse of %s is %s' % (x, x_reverse))
