# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#  Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
#  Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
#
#
#  Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 100].
#  -100 <= Node.val <= 100
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 11
# 394 👎 792
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        cur_list = []
        self.helper(root, 0, cur_list)
        return cur_list

    def helper(self, node: Optional[TreeNode], level, cur_list):

        if not node:
            return

        if len(cur_list) == level:  # track the level
            cur_list.append(node.val)

        self.helper(node.right, level + 1, cur_list)
        # if right subtree doesn't exist, need go to next level to check
        self.helper(node.left, level + 1, cur_list)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    ex = TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(4)),
        right=TreeNode(
            3,
        ),
    )
    print(s.rightSideView(ex))

"""
    1
   /  \
  2    3
   \
    4
"""
