"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # lengths of needle and haystack
        n_len = len(needle)
        h_len = len(haystack)

        # tranverse through the haystack
        for i in range(h_len - n_len + 1):
            # if the substring of haystack is equal to needle
            if haystack[i : i + n_len] == needle:
                return i

        # if not found, return -1
        return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))  # 0
print(s.strStr("leetcode", "leeto"))  # -1
print(s.strStr("hello", "ll"))  # 2
