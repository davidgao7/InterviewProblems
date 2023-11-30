# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
#  Each letter in magazine can only be used once in ransomNote.
#
#
#  Example 1:
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#
#  Example 2:
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
#  Example 3:
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
#  Constraints:
#
#
#  1 <= ransomNote.length, magazine.length <= 10⁵
#  ransomNote and magazine consist of lowercase English letters.
#
#
#  Related Topics Hash Table String Counting 👍 4655 👎 472


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # every unique letter in magazine can only use once in magazine
        # only lower case letter
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1  # letter in magazine cannot be used more than once
            # NOTE: dict.get(xxx, 0) + 1 will return 0 if xxx is not in the dict !! not error
        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("aa", "aab"))
