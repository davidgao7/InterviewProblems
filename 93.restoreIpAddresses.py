# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
#
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
#
#
#  Given a string s containing only digits, return all possible valid IP
# addresses that can be formed by inserting dots into s. You are not allowed to reorder
# or remove any digits in s. You may return the valid IP addresses in any order.
#
#
#  Example 1:
#
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
#
#  Example 2:
#
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
#
#  Example 3:
#
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 20
#  s consists of digits only.
#
#
#  Related Topics String Backtracking 👍 5051 👎 776
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []  # legal strings
        self.backtracking(s, 0, 0, "", result)
        return result

    def backtracking(self, s, startIndex, point_num, current, result):
        """
        :param s:
        :param startIndex: start slicing point for next recursive call
        :param point_num: number of dot in ip
        :param current: track current separation with dots
        :param result: update result list for next recursive call
        :return:
        """
        # maximum of points in address is 3
        if point_num == 3:  # means has been split into 4 parts
            # still need to check the last string after the 3rd point
            if self.isvalid(s, startIndex, len(s) - 1):
                # if valid , need to add the 4th substr in
                current += s[startIndex:]
                result.append(current)
                # the depth of tree is 3
            return

        for i in range(startIndex, len(s)):
            # NOTE: 1st check if the [startIndex:i] substring is legal
            if self.isvalid(s, startIndex, i):
                # number choosing for each layer in the tree
                # check the 1st range str is valid
                sub = s[startIndex : i + 1]
                # current = current + sub + "."  # [startIndex, i]  # NOTE: need to put the current update inside the
                                                                    # backtracking method!!

                self.backtracking(
                    s, i + 1, point_num + 1, current + sub + '.', result  # get another chunk of str
                )  # since we add '.' into the str
                # backtracking, delete the insert dots
                # point_num -= 1
                # s = s[:startIndex] + s[startIndex + 1 : i + 1] + s[i + 1 + 1 :]
            else:
                break  # if is not leagal, end this loop back to upper recursive branch

    def isvalid(self, s, startIndex, endIndex):
        """
        check the string is valid
        1. 0 at sart?
        2. value > 255?
        :param s:
        :param startIndex:
        :param endIndex:
        :return:
        """
        if startIndex > endIndex:
            return False
        if (
            s[startIndex] == "0" and startIndex != endIndex
        ):  # if string length > 1 and leading 0, not valid
            return False

        res = 0
        for i in range(startIndex, endIndex + 1):
            # digit by digit get the str value

            if not s[i].isdigit():  # 遇到非数字字符不合法
                return False
            res = res * 10 + int(s[i])
            if res > 255:  # 如果大于255了不合法
                return False

        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
