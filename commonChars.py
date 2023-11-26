# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the answer
# in any order.
#
#
#  Example 1:
#  Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
#
#  Example 2:
#  Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
#  Constraints:
#
#
#  1 <= words.length <= 100
#  1 <= words[i].length <= 100
#  words[i] consists of lowercase English letters.
#
#
#  Related Topics Array Hash Table String 👍 3384 👎 275
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import collections

        tmp = collections.Counter(words[0])
        l = []
        for i in range(1, len(words)):
            # 使用 & 取交集
            tmp = tmp & collections.Counter(words[i])

        # 剩下的就是每个单词都出现的字符（键），个数（值）
        for j in tmp:
            v = tmp[j]
            while v:
                l.append(j)
                v -= 1
        return l


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    # Input: words = ["bella", "label", "roller"]
    # Output: ["e","l","l"]
    words = ["bella", "label", "roller"]
    s = Solution()
    print(s.commonChars(words))
