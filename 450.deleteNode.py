# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of the BST.
#
#  Basically, the deletion can be divided into two stages:
#
#
#  Search for a node to remove.
#  If the node is found, delete the node.
#
#
#
#  Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
#
#
#
#  Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
#
#  Example 3:
#
#
# Input: root = [], key = 0
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 10⁴].
#  -10⁵ <= Node.val <= 10⁵
#  Each node has a unique value.
#  root is a valid binary search tree.
#  -10⁵ <= key <= 10⁵
#
#
#
#  Follow up: Could you solve it with time complexity O(height of tree)?
#
#  Related Topics Tree Binary Search Tree Binary Tree 👍 8648 👎 238
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1.base case: if no tree, return None
        if not root:
            return None

        if root.val == key:
            # 2. if we find the target node, we need to
            # 2.1. delete the node
            # 2.2. keep the tree connected
            # two cases: the node is the leaf node or parent node
            if not root.left and not root.right:
                return None  # the recursive connection will be none therefore 'delete' the node

            # connect the 'existing' tree
            elif not root.left:
                return root.right

            elif not root.right:
                return root.left

            # perform deletion
            else:
                # move the target left child to target right child's left child
                cur = root.right
                # go to the right child's left leaf, append the root's left sub tree
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right    # return the new right subtree

        # 3. recursively search the target key need to be deleted
        if root.val > key:
            # the key is on the left side of the tree, we will get the left tree result here
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            # the key is on the right side of the tree, we will get the right tree result here
            root.right = self.deleteNode(root.right, key)

        return root

# leetcode submit region end(Prohibit modification and deletion)
