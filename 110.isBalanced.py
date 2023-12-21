# Given a binary tree, determine if it is height-balanced.
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
#  Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 5000].
#  -10⁴ <= Node.val <= 10⁴
#
#
#  Related Topics Tree Depth-First Search Binary Tree 👍 10199 👎 608
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root) != -1  # -1 means not balanced

    def get_height(self, node: Optional[TreeNode]) -> int:
        # post order (LRN) , loop left, right tree first since we need to get the height of the left and right first
        if not node:
            return 0
        left_height = self.get_height(node.left)

        # left tree not balanced
        if left_height == -1:
            return -1

        right_height = self.get_height(node.right)
        if right_height == -1:
            return -1

        # not balanced, return -1
        if abs(left_height - right_height) > 1: return -1
        # the parent height is the maximum of its children + 1
        else: return max(left_height, right_height) + 1


# leetcode submit region end(Prohibit modification and deletion)
