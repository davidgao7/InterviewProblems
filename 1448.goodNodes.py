# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #  root node is always a good node
        #  microsft interview question
        if not root.left and not root.right:
            return 1

        # use dfs to traverse the tree
        def dfs(node, max_val):
            if not node:
                return 0

            # good node definition: the node is always greater
            if node.val >= max_val:
                max_val = node.val
                return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)
            else:
                # this tree is not good
                return dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)
