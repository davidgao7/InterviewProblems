# Given a binary tree, find its minimum depth.
#
#  The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
#  Note: A leaf is a node with no children.
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
#  Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 10⁵].
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 70
# 45 👎 1270
from typing import Optional

import numpy as np


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # base case: empty tree
        if not root:
            return 0

        # base case: only 1 node
        if not root.left and not root.right:
            return 1

        # if has left child or right child, calculate depth
        # in this case either left/right child has leaves or both have leaves
        if not root.left:
            # only has right subtree
            return self.minDepth(root.right) + 1

        if not root.right:
            return self.minDepth(root.left) + 1

        # if node has both left subtree and right subtree, we need to get the minimum depth
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1  # dp?

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    ex = TreeNode(
        3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    s = Solution()
    print(s.minDepth(ex))
