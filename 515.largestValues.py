# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
#
#
#  Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
#
#
#  Example 2:
#
#
# Input: root = [1,2,3]
# Output: [1,3]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree will be in the range [0, 10⁴].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 35
# 03 👎 110
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # NOTE: use stack pop
        level_order = []  # track each level
        # recursive
        self.helper(root, 0, level_order)
        level_order = [max(l) for l in level_order]
        return level_order  # if there's nothing in the tree, we just return the empty level_order

    def helper(self, node, depth, level_horizontally_elements):
        # base case
        if not node:
            return  # return nothing since we already decleared a list for answer holder outside in function levelOrder
        # append level value
        # level_order: [[level1], [level2]...]
        # form a level list for this specific level
        if len(level_horizontally_elements) == depth:
            # prepare the level list to store the level tree elements
            level_horizontally_elements.append([])

        # store the level elements in the recursive
        level_horizontally_elements[depth].append(
            node.val
        )  # when recursive right part, will skip the if above since we append the left child, [[the initialized list when go through left part] is no longer empty]
        # [[1st level elements], [2nd level elements] ...]
        # perform the recursive to store both left child and right child
        self.helper(
            node.left, depth + 1, level_horizontally_elements
        )  # recursive left part, level_horizontally_elements appends left childs 1 level eleemnt
        self.helper(node.right, depth + 1, level_horizontally_elements)


# leetcode submit region end(Prohibit modification and deletion)
