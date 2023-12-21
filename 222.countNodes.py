# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
#  According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2ʰ nodes inclusive at the last level h.
#
#
#  Design an algorithm that runs in less than O(n) time complexity.
#
#
#  Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
#  Example 2:
#
#
# Input: root = []
# Output: 0
#
#
#  Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 5 * 10⁴].
#  0 <= Node.val <= 5 * 10⁴
#  The tree is guaranteed to be complete.
#
#
#  Related Topics Binary Search Bit Manipulation Tree Binary Tree 👍 8288 👎 468
#
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 0
        elif node.left and node.right:
            return 2 + self.count(node.left) + self.count(node.right)
        elif node.left or node.right:
            if node.left:
                return 1 + self.count(node.left)
            elif node.right:
                return 1 + self.count(node.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1+self.count(root) # include the root node


# leetcode submit region end(Prohibit modification and deletion)
