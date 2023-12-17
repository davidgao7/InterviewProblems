# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
#  Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
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
#  The number of nodes in the tree is in the range [0, 2000].
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics Tree Breadth-First Search Binary Tree 👍 14670 👎 290
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # NOTE: use stack pop
        level_order = []  # track each level
        # recursive
        self.helper(root, 0, level_order)
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
        level_horizontally_elements[depth].append(node.val)  # when recursive right part, will skip the if above since we append the left child, [[the initialized list when go through left part] is no longer empty]
        # [[1st level elements], [2nd level elements] ...]
        # perform the recursive to store both left child and right child
        self.helper(node.left, depth+1, level_horizontally_elements)  # recursive left part, level_horizontally_elements appends left childs 1 level eleemnt
        self.helper(node.right, depth+1, level_horizontally_elements)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    # root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3,
    TreeNode(9), TreeNode(20,
            TreeNode(15), TreeNode(7))
    )
    res = s.levelOrder(root)
    print(res)
