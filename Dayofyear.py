#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param date string字符串 YYYY-MM-DD
# @return int整型
#
class Solution:
    def dayOfYear(self, date):
        # write code here
        year, month, day = date.split('-')
        year, month, day = int(year), int(month), int(day)
        if month == 1:
            return day
        ans = 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, month + 1):
            if i < month:
                ans += days[i - 1]
        # add day
        ans += day
        return ans


s = Solution()
print(s.dayOfYear("1999-03-02"))
