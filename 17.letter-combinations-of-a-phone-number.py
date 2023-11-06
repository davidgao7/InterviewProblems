#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        
        if len(digits) == 0:
            return res
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in dic[next_digits[0]]:
                # get all possible combinations for the next digits
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()

    digits = "23"
    print(s.letterCombinations(digits))
