# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any order.
#
#
#  A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#  Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
#  Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
#  Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
#  Constraints:
#
#
#  0 <= digits.length <= 4
#  digits[i] is a digit in the range ['2', '9'].
#
#
#  Related Topics Hash Table String Backtracking 👍 17780 👎 931
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # construct number, letter mapping
        self.dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.result = []
        self.s = ''

        if len(digits) == 0:
            return self.result

        self.backtrack(digits, 0)
        return self.result

    def backtrack(self, digits, index):
        # barck track tree option start with a digit: digits[index]

        #  loop till the last digit
        if len(digits)==index:
            self.result.append(self.s)
            return

        digit = int(digits[index])   # get the current digit pressed
        letter = self.dic[str(digit)]

        # get the option , 3 or 4 possibilities user want
        for i in range(0,len(letter)):
            # for each possibility, get the next possible button pressed
            self.s += letter[i]
            # next down level, next digit number
            self.backtrack(digits, index+1)
            # when return back to previous level, need to pop the last option
            self.s = self.s[:-1]  # if not satisfy the end condition(fullfill the number of digits, we go to the next
            # branch (next last digit pressed))




# leetcode submit region end(Prohibit modification and deletion)
