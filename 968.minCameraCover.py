# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
#
#  Return the minimum number of cameras needed to monitor all nodes of the tree.
#
#
#
#  Example 1:
#
#
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
#  Example 2:
#
#
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree.
#  The above image shows one of the valid configurations of camera placement.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 1000].
#  Node.val == 0
#
#
#  Related Topics Dynamic Programming Tree Depth-First Search Binary Tree 👍 518
# 2 👎 69
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = [0]
        # 0: no camera, no cover
        if self.traversal(root, result) == 0:
            result[0] += 1
        return result[0]

    def traversal(self, root, result):
        # empty node, has covered
        if root is None:
            return 2

        left = self.traversal(root.left, result)
        right = self.traversal(root.right, result)

        # 1. 左右都有覆盖
        if left == 2 and right == 2:
            return 0

        # 2. left and right are covered
        # left 0 right 0 左右节点无覆盖
        #  left == 1 && right == 0 左节点有摄像头，右节点无覆盖
        #  left == 0 && right == 1 左节点有无覆盖，右节点摄像头
        #  left == 0 && right == 2 左节点无覆盖，右节点覆盖
        #  left == 2 && right == 0 左节点覆盖，右节点无覆盖
        if left == 0 or right == 0:
            result[0] += 1
            return 1

        # 3. left == 1 && right == 2 左节点有摄像头，右节点有覆盖
        #    left == 2 && right == 1 左节点有覆盖，右节点有摄像头
        #    left == 1 && right == 1 左右节点都有摄像头
        else:
            return 2


# leetcode submit region end(Prohibit modification and deletion)
