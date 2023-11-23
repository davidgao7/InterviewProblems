# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#  An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
#
#
#  Example 1:
#  Input: s = "anagram", t = "nagaram"
# Output: true
#
#  Example 2:
#  Input: s = "rat", t = "car"
# Output: false
#
#
#  Constraints:
#
#
#  1 <= s.length, t.length <= 5 * 10⁴
#  s and t consist of lowercase English letters.
#
#
#
#  Follow up: What if the inputs contain Unicode characters? How would you
# adapt your solution to such a case?
#
#  Related Topics Hash Table String Sorting 👍 10986 👎 343


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use collection Counter to find number of occurance of each digit
        from collections import Counter
        # NOTE: Elements are counted from an ITERABLE(will count each elem in list, each char for string, etc.)
        # or initialized from another mapping (or counter)
        a_count = Counter(s)
        b_count = Counter(t)

        return a_count==b_count  # only compare the counter result is same or not

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s,t))