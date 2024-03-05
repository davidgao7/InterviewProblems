class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case: if s is empty, return 0
        if len(s) == 0:
            return 0
        # two pointers, O(n) time complexity since loop string once
        l, r = 0, 0
        max_len = 0
        # use a set to store the characters in the sliding window
        char_set = set()

        # let pointer l and r loop through the entire string
        while l < len(s) and r < len(s):
            # if the char is not in set, add to set and update max_len
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            # if char is in the set, remove it from set and find another start point
            else:
                char_set.remove(s[l])
                l += 1
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbbb"))  # 1
    print(s.lengthOfLongestSubstring("pwwkew"))  # 3
