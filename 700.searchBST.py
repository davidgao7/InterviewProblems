# You are given the root of a binary search tree (BST) and an integer val.
#
#  Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
#
#
#  Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
#
#  Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 5000].
#  1 <= Node.val <= 10⁷
#  root is a binary search tree.
#  1 <= val <= 10⁷
#
#
#  Related Topics Tree Binary Search Tree Binary Tree 👍 5705 👎 181
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # none tree or find the value
        if not root or root.val == val: return root

        # binary search
        if val < root.val:
            result= self.searchBST(root.left, val)
        else:
            result= self.searchBST(root.right, val)

        return result  # none if not in tree
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
t = TreeNode(4,
             left=TreeNode(2, TreeNode(1), TreeNode(3)),
             right=TreeNode(7))
r = s.searchBST(t, 2)
print(r)
