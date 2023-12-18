# Given an n-ary tree, return the level order traversal of its nodes' values.
#
#  Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
#
#
#  Example 1:
#
#
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
#
#
#  Example 2:
#
#
#
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,
# null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#
#
#
#  Constraints:
#
#
#  The height of the n-ary tree is less than or equal to 1000
#  The total number of nodes is between [0, 10⁴]
#
#
#  Related Topics Tree Breadth-First Search 👍 3555 👎 135


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level_order = []
        self.helper(root, 0, level_order)
        return level_order

    def helper(self, node, depth, level_horizontally_elements):
        if not node:
            return
        if len(level_horizontally_elements) == depth:
            level_horizontally_elements.append([])

        level_horizontally_elements[depth].append(node.val)
        for child in node.children:
            self.helper(child, depth + 1, level_horizontally_elements)

# leetcode submit region end(Prohibit modification and deletion)
