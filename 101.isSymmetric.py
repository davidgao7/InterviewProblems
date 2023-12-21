# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center).
#
#
#  Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 1000].
#  -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 14
# 685 👎 353
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.compare(root.left, root.right)

    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        # base case
        # 1. left / right is missing, cant compare
        if left is None and right is not None: return False
        if left is not None and right is None: return False
        if left is None and right is None: return True

        # 2.value is difference, return false
        if left.val != right.val: return False

        # 3. left right val equal, go next level
        # 3.1 compare outer node
        outside = self.compare(left.left, right.right)
        # 3.2 compare inner node
        inside = self.compare(left.right, right.left)

        return outside and inside  # both satisfy


if __name__ == '__main__':
    s = Solution()



# leetcode submit region end(Prohibit modification and deletion)
