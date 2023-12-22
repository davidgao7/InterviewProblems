# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the path
# equals targetSum.
#
#  A leaf is a node with no children.
#
#
#  Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
#
#  Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
#
#  Example 3:
#
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 5000].
#  -1000 <= Node.val <= 1000
#  -1000 <= targetSum <= 1000
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 92
# 74 👎 1049
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        # subtract node val for along the path, if hit 0 sum, and it's a leaf node, then we find the path
        return self.tranverse(root, targetSum-root.val)  # we are at the root right now

    def tranverse(self, node, count):

        # preorder

        # 1. if we are at the leaf node, and the sum is 0, means we find the path and the total sum of this path is target
        if not node.left and not node.right and count==0: return True

        # 2. tranverse the path to check if sum is target,
        # once the sum is greater than target, we need to backtrack a level

        # left
        if node.left:
            count-=node.left.val
            if self.tranverse(node.left, count): return True
            # if not find the value for this left path, backtrack, since we are at this node, we still need to add this node val
            # and then go to another direction from this node
            count+= node.left.val  # cancel the first path val

        # right
        if node.right:
            count-=node.right.val
            if self.tranverse(node.right, count): return True
            count+= node.right.val

        # return false if on the leaf node and tranverse all the path
        return False








# leetcode submit region end(Prohibit modification and deletion)
