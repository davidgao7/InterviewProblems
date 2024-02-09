# Problem: Group Anagrams: given an array of strings strs, group the anagrams together. You can return the answer in any order.,
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping chars to list of anagrams
        # for every string we count the number of occurance of each char
        # and use it as key for the dictionary
        for s in strs:
            count = [0]*26  # a...z
            for c in s:
                # use ord to get the ascii value of the char
                count[ord(c)-ord('a')] += 1  # count the occurance of each char
            res[tuple(count)].append(s)  # list can't be used as key, so we use tuple


        return list(res.values())  # return the values of the dictionary
    # T: O(n * k)  S: O(n * k)  n is the length of the strs, k is the length of the longest string




if __name__ == "__main__":
    solution = Solution()
    print(
        solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )  # [["eat","tea","ate"],["tan","nat"],["bat"]]
