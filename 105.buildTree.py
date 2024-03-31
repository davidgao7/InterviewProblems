# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        result = self.helper(preorder, inorder)
        return result

    def helper(self, preorder: List[int], inorder: List[int]):

        # base case
        # if the preorder is empty, return None
        print(f"preorder: {preorder}")
        print(f"inorder: {inorder}")
        if not preorder or not inorder:
            return None

        # preorder: N L R
        root = TreeNode(preorder[0])
        # find the index of the root node in the inorder list
        root_idx = inorder.index(preorder[0])

        # left tree
        root.left = self.helper(preorder[1 : root_idx + 1], inorder[:root_idx])
        print("=========left=============")

        # right tree
        root.right = self.helper(preorder[root_idx + 1 :], inorder[root_idx + 1 :])
        print("=========right=============")

        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    result = s.buildTree(preorder, inorder)
    print(f"result: {result}")
