# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
#
#  Example 1:
#  Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
#  Example 2:
#  Input: s = "a"
# Output: [["a"]]
#
#
#  Constraints:
#
#
#  1 <= s.length <= 16
#  s contains only lowercase English letters.
#
#
#  Related Topics String Dynamic Programming Backtracking 👍 12067 👎 398
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backtrack(self, s:str, start_index:int, path:List[str],result:List[List[str]]) -> None:
        # if the start_index separate the end and empty, means we've found a solution
        if start_index>=len(s):
            result.append(path[:])  # remember to use path[:] to add a copy, or it will append empty []
            return

        # get the substring
        for i in range(start_index,len(s)):
            if self.is_Palindrome(s, start_index, i):
                # if the substring is the palindrome, add the substring
                # add this path
                path.append(s[start_index:i+1][:])
            else:
                continue

            # backtrack to find the palindrome start at i+1
            self.backtrack(s, i+1, path, result)
            # pop the previous edge, since this edge is not right
            path.pop(-1)

    def is_Palindrome(self, s, start_index:int, end_index:int):
        # two pointer
        j = end_index
        for i in range(start_index,end_index):
            if s[i] != s[j]: return False
            j -=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        self.backtrack(s, 0, path, result)
        return result


# leetcode submit region end(Prohibit modification and deletion)
