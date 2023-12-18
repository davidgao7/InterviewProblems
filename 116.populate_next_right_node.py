# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following definition:
#
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#
#  Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
#  Initially, all next pointers are set to NULL.
#
#
#  Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#  Example 2:
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
#  The number of nodes in the tree is in the range [0, 2¹² - 1].
#  -1000 <= Node.val <= 1000
#
#
#
#  Follow-up:
#
#
#  You may only use constant extra space.
#  The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
#
#
#  Related Topics Linked List Tree Depth-First Search Breadth-First Search
# Binary Tree 👍 9378 👎 289
"""
  1          1 -> NULL
 / \  =>   /   \
2   3     2 ->  3 -> NULL
"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # from the linked list for this level
        self.helper(root, 0)
        return root

    def helper(self, node, depth ):
        # need to connect inplace

        if not node or not node.left:
            return

        # connect next level horitzontal
        # print(f'link {node.left.val}->{node.right.val}')
        node.left.next = node.right  # let next level's left point to right, everytime only care the minimum tree with 3 elements

        #  connect next level 2 subtree with different parents
        if node.next != None:
            # print(f'link {node.right.next.val} -> {node.next.left.val}')
            node.right.next = node.next.left

        # [[1st level elements], [2nd level elements]...]
        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    ex = Node(
        1,
        left=Node(2, left=Node(4), right=Node(5)),
        right=Node(3, left=Node(6), right=Node(7)),
    )
    s = Solution()
    res = s.connect(ex)
    print(res)
