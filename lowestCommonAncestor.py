# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        return self.helper(root, o1, o2).val  # 需要返回值而不是object

    def helper(self, root, o1, o2):
        # bottom up lookup
        # post order : L R N
        # common ancestor: node.left=o1 and node.right=o2 or inverse
        # we can check L=o1,R=o2, then take the Node N using post order traversal

        # base case
        # 如果在root找到o1 or o2 or null, 说明此时root为祖先
        if root == None or root.val == o1 or root.val == o2:
            return root

        # 左右subtree两个方向一起找,看看在左subtree还是右subtree
        left = self.helper(root.left, o1, o2)  # L
        right = self.helper(root.right, o1, o2)  # R

        # 如果其中一边有，recursive的值要通过非Null的来返回，所以return非Null值
        # NOTE：not left <===> left == None
        if not left: return right
        if not right: return left

        #         if left == None: return right
        #         if right == None: return left

        # 如果都没有，就返回啥都没有
        # elif not left and not right: 这代表两个都是空，说明没做到，本身就是空的，return就行
        return root


