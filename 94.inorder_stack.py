# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
#
#
#  Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
#  Example 2:
#
#
# Input: root = []
# Output: []
#
#
#  Example 3:
#
#
# Input: root = [1]
# Output: [1]
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
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 13009 👎 726
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    import queue

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store inorder traversal result
        stack = []  # Stack to assist in traversal
        curr = root  # Pointer to track the current node

        # Traverse the tree until current node is not None or stack is not empty
        while curr is not None or stack:
            # Traverse to the leftmost node of the current subtree
            while curr is not None:  # perform the recursion
                stack.append(curr)  # Push current node to stack
                curr = curr.left  # Move to the left child

            curr = stack.pop()  # Get the top node from stack
            res.append(curr.val)  # Append the value of current node to result list
            curr = curr.right  # Move to the right child to explore its subtree

        return res  # Return the inorder traversal result


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    tree = TreeNode(1)
    s = Solution()
    print(s.inorderTraversal(tree))
