# Given the root of a binary tree, return the sum of all left leaves.
#
#  A leaf is a node with no children. A left leaf is a leaf that is the left
# child of another node.
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 1
# 5 respectively.
#
#
#  Example 2:
#
#
# Input: root = [1]
# Output: 0
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 1000].
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 49
# 05 👎 282
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # end case
        # left sum is 0 when no left child
        # NOTE root just a node passing in, it is root for the first time pass in
        if root is None: return 0

        # need only return the sum of left tree and right tree, not leaf node value
        if root.left is None and root.right is None: return 0

        # post order L R N

        # get left tree sum (L)
        left_sum = self.sumOfLeftLeaves(root.left)

        # only recursive until the next left node is the leaf node, then you can
        # say we can start adding sum
        # NOTE: def of left leaf node: node left !=None and node left.left is None and node left.right is None
        if root.left is not None and root.left.left is None and root.left.right is None:
            left_sum = root.left.val

        # right
        right_sum = self.sumOfLeftLeaves(root.right)

        # mid(Node)
        mid_sum = left_sum + right_sum

        return mid_sum



# leetcode submit region end(Prohibit modification and deletion)
