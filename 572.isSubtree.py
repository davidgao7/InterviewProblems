# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        # check if the subtree is same as the current tree
        if self.isSameTree(root, subRoot):
            return True

        # if not, check the rest of the tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

        return False


if __name__ == "__main__":
    s = Solution()
    # Example 1
    # root = [3,4,5,1,2], subRoot = [4,1,2]
    # Output: true
    # Explanation: The subRoot is a subtree of the root tree.abs(a)
    # root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    # subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    root = TreeNode(1)
    subRoot = TreeNode(1)
    print(s.isSubtree(root, subRoot))
