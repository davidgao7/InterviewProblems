# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
#
#  In one step, you can delete exactly one character in either string.
#
#
#  Example 1:
#
#
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
#  Example 2:
#
#
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
#
#
#  Constraints:
#
#
#  1 <= word1.length, word2.length <= 500
#  word1 and word2 consist of only lowercase English letters.
#
#
#  Related Topics String Dynamic Programming 👍 5615 👎 83


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # 1. construct a dp array
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        # 2. fill the dp array from the bottom up
        # we are filling the dp array from the bottom up because we want to find the minimum number of steps to make the two strings the same
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):

                # self.print_matrix_table(dp)
                # print("=====")
                # if the first string is empty, then we have to remove all the characters from the second string
                if word1[j - 1] == word2[i - 1]:
                    # print(f"word1[{j}-1] == word2[{i}-1]")
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # print("dynamic programming")
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                # print(f"{i},{j} : {dp[i][j]}")
                # print("=====")
        return len(word1) + len(word2) - 2 * dp[-1][-1]  # note

    def print_matrix_table(self, matrix):
        for row in matrix:
            print(row)


# O(n*m) time | O(n*m) space
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance("sea", "eat"))  # 2
