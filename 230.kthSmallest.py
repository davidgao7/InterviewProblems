# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        ptr = root
        inorder = []
        n = 0

        while inorder or ptr:
            #  print(f"length of inorder list: {len(inorder)}")
            # when you can keep going left for smallest or there are still tree nodes to visit
            while ptr:
                # N
                inorder.append(ptr)
                for i in inorder:
                    if i:
                        # print(i.val, end=" ")
                        pass
                    else:
                        # print(i, end=" ")
                        pass
                # print("\n=====================")
                # find the left most for smallest
                ptr = ptr.left

            # pop the smallest, get the second smallest
            # print("get the smallest")
            # print("pop the element")
            # print(f"inorder: {[i.val if i else None for i in inorder]}")
            ptr = inorder.pop()
            # print(f"length of list: {len(inorder)}")
            #
            # print(f"inorder after pop: {[i.val if i else None for i in inorder]}")
            # print(ptr.val)
            # recorder the current nth smallest
            n += 1
            # print(f"n: {n}, k: {k}")

            if n == k:
                return ptr.val

            # if left most has not reached kth smallest, go to right
            # print(f"n: {n}, k: {k}, n < k: {n < k}")
            ptr = ptr.right


if __name__ == "__main__":
    # root = TreeNode(3)
    # root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.left.right = TreeNode(2)
    # k = 1
    # print(Solution().kthSmallest(root, k))  # 1

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    print(Solution().kthSmallest(root, k))  # 3
