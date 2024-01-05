# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
#
#  You may return the answer in any order.
#
#
#  Example 1:
#
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
#
#
#  Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
#
#  Constraints:
#
#
#  1 <= n <= 20
#  1 <= k <= n
#
#
#  Related Topics Backtracking 👍 7953 👎 208
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backtrack(self, n, k, path,result,start_index):
        # if we choose k elements already, push the answer
        if len(path) == k:
            result.append(path[:])  # [:] create a shallow copy of the list
            print(f'current result: {result}')
            return  # backtrack

        end = n-(k-len(path))+1+1  # include the end
        for i in range(start_index, end):  # optimization to not loop redundant path
        # for i in range(start_index, n + 1):  # before purnue the tree
            path.append(i)  # record current start index
            self.backtrack(n, k, path, result, i + 1)
            path.pop()  # remove the index which is done

    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []  # store one path
        result = []  # store collection of result paths
        self.backtrack(n, k,path,result, 1)
        return result


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution()
    print(s.combine(n,k))