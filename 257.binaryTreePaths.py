# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
#  A leaf is a node with no children.
#
#
#  Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
#
#  Example 2:
#
#
# Input: root = [1]
# Output: ["1"]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 100].
#  -100 <= Node.val <= 100
#
#
#  Related Topics String Backtracking Tree Depth-First Search Binary Tree 👍 632
# 0 👎 272
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(
        self, node: Optional[TreeNode], path: List[int], result_path: List[str]
    ):
        # preorder tranversal N L R
        path.append(node.val)  # N

        # if goes to the end of child node, we can add this path
        if not node.left and not node.right:
            path_str = ""
            for p in range(len(path)-1):  # skip the last node when printing the '->'
                path_str += str(path[p])
                path_str += "->"
            path_str += str(path[len(path) - 1])
            result_path.append(path_str)
            return

        # left child
        if node.left:
            self.traverse(node.left, path, result_path)
            path.pop()

        # right child
        if node.right:
            self.traverse(node.right, path, result_path)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.traverse(root, path, result)
        return result


# leetcode submit region end(Prohibit modification and deletion)
