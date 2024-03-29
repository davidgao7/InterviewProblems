# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion. It is
# guaranteed that the new value does not exist in the original BST.
#
#  Notice that there may exist multiple valid ways for the insertion, as long
# as the tree remains a BST after insertion. You can return any of them.
#
#
#  Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
#
#
#
#  Example 2:
#
#
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
#
#
#  Example 3:
#
#
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree will be in the range [0, 10⁴].
#  -10⁸ <= Node.val <= 10⁸
#  All the values Node.val are unique.
#  -10⁸ <= val <= 10⁸
#  It's guaranteed that val does not exist in the original BST.
#
#
#  Related Topics Tree Binary Search Tree Binary Tree 👍 5586 👎 164
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            node = TreeNode(val)
            return node
        elif root.val > val:  # should in left tree
            if root.left is None:
                root.left = TreeNode(val)
            else:
                root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root.right, val)

        return root


# leetcode submit region end(Prohibit modification and deletion)
