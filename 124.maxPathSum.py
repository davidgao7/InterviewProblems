# 124. Binary Tree Maximum Path Sum
# Hard
# Topics
# Companies
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
#
#
# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

from typing import Optional


#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            # 1. base case
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            # left right max could be 0
            # print(f"compare left_max: {left_max} with 0")
            left_max = max(left_max, 0)
            # print(f"compare right_max: {right_max} with 0")
            right_max = max(right_max, 0)

            print(f"left_max: {left_max}, right_max: {right_max}")

            # 2. update the path sum
            # print(f"root.val: {root.val}, left_max: {left_max}, right_max: {right_max}")
            # NOTE: this is the final result we need to update
            res[0] = max(res[0], left_max + right_max + root.val)
            # print(f"self.max_sum: {self.max_sum}")
            # print("===========================")

            # 3. return the max path sum that can be extended to the parent node
            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]


if __name__ == "__main__":
    # root = [1,2,3]
    # Output: 6
    # root = TreeNode(1, TreeNode(2), TreeNode(3))
    s = Solution()
    # print(s.maxPathSum(root))
    # ==========================
    # root = [-10,9,20,null,null,15,7]
    # Output: 42
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.maxPathSum(root))
