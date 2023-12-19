# Given a binary tree
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
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in Figure B.
# The serialized output is in level order as connected by the next pointers, with
# '#' signifying the end of each level.
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
#  The number of nodes in the tree is in the range [0, 6000].
#  -100 <= Node.val <= 100
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
# Binary Tree 👍 5659 👎 309


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


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
    def print_queue(self, root: list) -> str:
        res = ''
        for e in root:
            res += ',' + str(e.val)

        return res

    def connect(self, root: "Node") -> "Node":
        # from the linked list for this level
        if not root:
            return root

        # bfs, queue
        # setting up the queue
        q = [root]
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                print(f"pop {node.val}")

                # NOTE: connection happened in the first if statements
                if i < size - 1:  # if the queue has nodes after poping
                    print(f"link {node.val}->{q[0].val}")
                    # always point the left child to the right child since we add left first and pop the left first
                    node.next = q[0]
                # track the sub child of this node in the queue
                if node.left:
                    print(f"append subtree start at {node.left.val}")
                    q.append(node.left)
                if node.right:
                    print(f"append subtree start at {node.right.val}")
                    q.append(node.right)
                print(f"current queue: {self.print_queue(q)}")
                print("=======")

                # for next iteration, we will always deal with node on the same level if hasn't dealed yet

        return root


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    root = Node(
        1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, right=Node(7))
    )
    s = Solution()
    result = s.connect(root)
    print(result)
