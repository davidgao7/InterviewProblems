# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10⁻⁵ of the actual answer will
# be accepted.
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
#
#  Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 10⁴].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 50
# 79 👎 312
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 1. get number for each level
        level_order = []  # track each level
        # recursive
        self.helper(root, 0, level_order)
        # 2. calculate the avg for each level
        return [sum(x)/len(x) for x in level_order]

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
if __name__ == "__main__":
    s = Solution()
    # root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3,
    TreeNode(9), TreeNode(20,
            TreeNode(15), TreeNode(7))
    )
    res = s.averageOfLevels(root)
    print(res)