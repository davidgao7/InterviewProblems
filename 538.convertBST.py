# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus the
# sum of all keys greater than the original key in BST.
#
#  As a reminder, a binary search tree is a tree that satisfies these
# constraints:
#
#
#  The left subtree of a node contains only nodes with keys less than the
# node's key.
#  The right subtree of a node contains only nodes with keys greater than the
# node's key.
#  Both the left and right subtrees must also be binary search trees.
#
#
#
#  Example 1:
#
#
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
#  Example 2:
#
#
# Input: root = [0,null,1]
# Output: [1,null,1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 10⁴].
#  -10⁴ <= Node.val <= 10⁴
#  All the values in the tree are unique.
#  root is guaranteed to be a valid binary search tree.
#
#
#
#  Note: This question is the same as 1038: https://leetcode.com/problems/
# binary-search-tree-to-greater-sum-tree/
#
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 5084
#  👎 172
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # the question want original key plus the sum of all keys greater than the original key in BST for each  node
        # the question want original key plus the sum of all keys greater than the original key in BST for each  node
        self.pre = 0

        def traverse(node):
            # traverse order: R N L , reverse of the inorder to add from leaves
            # just like an array, add array from back:
            # origin: [1,2,3]
            # result: [(3+2)+1,3+2,3]
            # in bst: sum of xx GREATER than xx, therefore start from right tree to left tree: R N L which is reverse
            # of the inorder traversal
            if not node:
                return

            traverse(node.right)
            node.val += self.pre  # increment each node val
            self.pre = node.val
            traverse(node.left)

        traverse(root)
        return root




# leetcode submit region end(Prohibit modification and deletion)
