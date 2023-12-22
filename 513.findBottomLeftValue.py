# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
#
#
#  Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
#
#
#  Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 10⁴].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 31
# 67 👎 257
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # record the depth for every level
        self.max_depth = float('-inf')
        self.result = None
        self.tranversal(root, 0)

        return self.result

    def tranversal(self, node, depth):
        # end case
        # when goes down to the leaves , we can check the dpeth of the current level
        if node.left is None and node.right is None:
            if depth > self.max_depth:
                # update the max_depth and left node val
                self.max_depth = depth
                self.result = node.val

        # recursive left
        if node.left:
            # update the depth
            depth+=1
            self.tranversal(node.left, depth)
            # NOTE: when we go to the node right child, we need to use the current depth
            depth-=1

        # recursive right
        if node.right :
            depth+=1
            self.tranversal(node.right, depth)
            depth-=1
# leetcode submit region end(Prohibit modification and deletion)
