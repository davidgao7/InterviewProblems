# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
#
#  Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
#  Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums is sorted in a strictly increasing order.
#
#
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 10595 👎 532
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, nums, left, right) -> Optional[TreeNode]:
        # include left and right

        # illegal interval
        if left > right: return None

        # if len is even, we get the left one
        mid = left + (right-left)//2

        # struct bst
        root = TreeNode(nums[mid])

        # recursive struct left tree
        # [1,2,3, mid, 4,5,6]
        #   left        right
        root.left = self.traversal(nums, left, mid-1)  # ignore the right corner
        root.right = self.traversal(nums, mid+1, right)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums)-1)
        return root

# leetcode submit region end(Prohibit modification and deletion)
