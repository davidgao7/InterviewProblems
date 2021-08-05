# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
#
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#      1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
#  进阶：
#
#  你可以运用递归和迭代两种方法解决这个问题吗？
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 1475 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return Solution.helper(self, root, root)

    def helper(self, left, right):
        if left is None and right is None:
            return True  # reach the bottom
        elif left is None and right is not None:
            return False  # one of them is not empty will be false
        elif left is not None and right is None:
            return False
        elif left.val == right.val:
            return Solution.helper(self, left.left, right.right) \
                   and Solution.helper(self, left.right, right.left)  # 内侧

    # leetcode submit region end(Prohibit modification and deletion)


# in order: L N R
# pre order: N L R
# post order: L R N

T = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    ),  # left child
    right=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    )  # right child
)  # 二叉树 [1,2,2,3,4,4,3] (symmetric)
s = Solution()
print(s.isSymmetric(T))  # should print True
