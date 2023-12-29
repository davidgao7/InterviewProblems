# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
#
#
#  Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
#  Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [2, 10⁴].
#  0 <= Node.val <= 10⁵
#
#
#
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search
# Tree Binary Tree 👍 4205 👎 211
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.pre = None

    def getMinimumDifference_helper(self, node: Optional[TreeNode]):
        # inorder, sorted, track difference each traversal

        if node is None:
            return # helper didnt' return anythin

        # Left
        self.getMinimumDifference_helper(node.left)
        # node, compare min
        if self.pre is not None:
            self.min_diff = min(self.min_diff, abs(self.pre.val - node.val))
        # update the parent node
        self.pre = node
        # right
        self.getMinimumDifference_helper(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode])  -> int:
        self.getMinimumDifference_helper(root)
        return self.min_diff

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    node = TreeNode(
        4, left=TreeNode(2, TreeNode(1), TreeNode(3)), right=TreeNode(6)
    )
    s = Solution()
    print(s.getMinimumDifference(node))