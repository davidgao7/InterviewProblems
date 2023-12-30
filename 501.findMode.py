# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
#
#  If the tree has more than one mode, return them in any order.
#
#  Assume a BST is defined as follows:
#
#
#  The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
#  The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
#  Both the left and right subtrees must also be binary search trees.
#
#
#
#  Example 1:
#
#
# Input: root = [1,null,2,2]
# Output: [2]
#
#
#  Example 2:
#
#
# Input: root = [0]
# Output: [0]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 10⁴].
#  -10⁵ <= Node.val <= 10⁵
#
#
#
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
#
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 3794
#  👎 766
from typing import Optional, List

import numpy as np


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        elem_count = {}
        result = []
        self.inorderTraversal(root, elem_count)
        max_req = max(elem_count.values())
        for k, v in elem_count.items():
            if v == max_req:
                result.append(k)

        return result  # small frequency -> more frequency

    def inorderTraversal(self, node: Optional[TreeNode], elem_count: dict) -> List[int]:
        if not node:
            return
        # L N R
        self.inorderTraversal(node.left, elem_count)
        if node.val not in elem_count.keys():
            elem_count[node.val]=0
        elem_count[node.val] += 1

        self.inorderTraversal(node.right, elem_count)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(1, right=TreeNode(2, left=TreeNode(2)))
    result = s.findMode(tree)
    print(result)
