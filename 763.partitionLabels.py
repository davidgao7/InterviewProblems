# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
#
#  Note that the partition is done so that after concatenating all the parts in
# order, the resultant string should be s.
#
#  Return a list of integers representing the size of these parts.
#
#
#  Example 1:
#
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.
#
#
#  Example 2:
#
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 500
#  s consists of lowercase English letters.
#
#
#  Related Topics Hash Table Two Pointers String Greedy 👍 10103 👎 374
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # record the last index of each letter
        hashed = [0] * 26  # 26 letters or just plenty spaces
        result = []
        left, right = 0, 0  # two pointers  record the length of the max substring
        for i in range(0, len(s)):
            # get the last index(most right) of each letter
            hashed[ord(s[i]) - ord('a')] = i
        for i in range(0, len(s)):
            # update the max distance when meet the same letter again
            right = max(right, hashed[ord(s[i]) - ord('a')])
            if i == right:  # find a section, all the letters won't appear again later
                result.append(right - left + 1)  # record number of the char
                left = right + 1  # update the left pointer

        return result
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))